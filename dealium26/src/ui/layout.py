import streamlit as st


def render_sidebar() -> None:
    with st.sidebar:
        st.title("Dealium26")
        st.caption("CRM NLP Assistant (Demo-first)")
        theme = st.selectbox("Theme", ["System", "Light", "Dark"], index=0)
        st.session_state["theme"] = theme
        st.markdown("### Industries")
        for item in [
            "Retail & E-commerce",
            "Real Estate",
            "Manufacturing / Trading / B2B",
            "Education & Coaching",
            "Healthcare & Wellness",
            "Logistics / Transport / Travel",
            "Service Businesses & Agencies",
            "Home Services & Construction",
            "Hospitality & Events",
        ]:
            st.write(f"- {item}")


def render_header() -> None:
    st.title("Dealium26")
    st.write("Displayable CRM assistant for non-technical teams using natural language.")
