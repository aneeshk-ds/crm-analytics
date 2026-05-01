import pandas as pd
import streamlit as st

from src.data.generator import save_mock_dataset
from src.data.loader import load_customers
from src.data.validators import basic_quality_report
from src.governance.audit_log import build_audit_entry
from src.governance.guardrails import requires_approval
from src.governance.session_store import add_history, get_history
from src.intelligence.next_best_action import suggest_action
from src.intelligence.risk_scoring import add_risk_band
from src.nlp.clarification import clarification_prompt, needs_clarification
from src.nlp.intent_router import route_intent
from src.nlp.normalize_query import normalize_query
from src.query.query_builder import build_filters
from src.query.query_executor import execute_customer_query
from src.response.explainability import build_explanation
from src.response.export import to_csv_bytes
from src.response.formatter import summarize_results
from src.response.multilingual_output import render_summary
from src.ui.layout import render_header, render_sidebar
from src.workflows.marketing import build_marketing_actions
from src.workflows.presets import PRESET_QUERIES
from src.workflows.sales import build_sales_actions
from src.workflows.support import build_support_actions


def _workflow_actions(intent: str, result):
    if intent == "support":
        return build_support_actions(result)
    if intent == "sales":
        return build_sales_actions(result)
    if intent == "marketing":
        return build_marketing_actions(result)
    return ["No specific workflow selected; refine query for support/sales/marketing actions."]


def main() -> None:
    st.set_page_config(page_title="Dealium26", page_icon="📊", layout="wide")
    render_sidebar()
    render_header()

    dataset_path = save_mock_dataset("dealium26/data/processed")
    customers = add_risk_band(load_customers(dataset_path))

    st.subheader("Natural Language CRM Assistant")
    industry = st.selectbox("Industry scenario", list(PRESET_QUERIES.keys()))
    preset = PRESET_QUERIES[industry]
    user_query = st.text_input(
        "Ask in English, Hindi, or Telugu",
        value=preset,
        placeholder="Example: Show high-value customers with low engagement in Hyderabad",
    )

    c1, c2, c3 = st.columns(3)
    quality = basic_quality_report(customers)
    with c1:
        st.metric("Customers", len(customers))
    with c2:
        st.metric("Data quality (missing %)", f"{quality['missing_ratio'] * 100:.1f}%")
    with c3:
        st.metric("Stale profiles (%)", f"{quality['stale_ratio'] * 100:.1f}%")

    if user_query:
        if needs_clarification(user_query):
            st.warning(clarification_prompt())
            return

        normalized = normalize_query(user_query)
        intent = route_intent(user_query)
        filters = build_filters(normalized)
        result = execute_customer_query(customers, filters)

        summary = summarize_results(result)
        output = render_summary(summary, str(normalized["language"]))
        explanation = build_explanation(filters, intent)
        action = suggest_action(intent, int((result["risk_band"] == "high").sum()) if not result.empty else 0)
        workflow_actions = _workflow_actions(intent, result)

        add_history(
            {
                "query": user_query,
                "industry": industry,
                "intent": intent,
                "result_count": int(len(result)),
                "language": normalized["language"],
            }
        )

        st.caption(f"Intent: {intent} | Language: {normalized['language']} | Filters: {filters or 'none'}")
        st.success(output)
        st.info(f"Next best action: {action}")

        st.markdown("#### Workflow actions")
        audit_rows = []
        for item in workflow_actions:
            approval_needed = requires_approval(item)
            approved = st.checkbox(f"Approve: {item}", value=not approval_needed, key=f"approve_{hash(item)}")
            entry = build_audit_entry(user_query, intent, item, approved)
            audit_rows.append(entry)
            status = "✅ approved" if approved else "⏳ pending approval"
            st.write(f"- {status} | {entry['timestamp_utc']}")

        with st.expander("Why this answer"):
            for line in explanation:
                st.write(f"- {line}")

        st.dataframe(result, use_container_width=True)

        col_dl1, col_dl2 = st.columns(2)
        with col_dl1:
            st.download_button(
                label="Download results CSV",
                data=to_csv_bytes(result),
                file_name="dealium26_results.csv",
                mime="text/csv",
            )
        with col_dl2:
            audit_df = pd.DataFrame(audit_rows)
            st.download_button(
                label="Download audit CSV",
                data=to_csv_bytes(audit_df),
                file_name="dealium26_audit.csv",
                mime="text/csv",
            )

    with st.expander("Session history"):
        history = get_history()
        if history:
            st.dataframe(pd.DataFrame(history), use_container_width=True)
        else:
            st.caption("No queries yet.")

    st.markdown("---")
    st.caption("MVP v5: downloadable reports + session history.")


if __name__ == "__main__":
    main()
