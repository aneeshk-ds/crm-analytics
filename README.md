# CRM Analytics — Dealium26

AI-powered Streamlit CRM assistant for non-technical users. Ask questions in plain English, Hindi, or Telugu and get customer segments, churn-risk signals, workflow recommendations, and downloadable reports.

---

## What it does

- Natural-language CRM queries (English, Hindi, Telugu)
- Intent routing for support, sales, marketing, and general CRM
- Customer filtering: city, churn risk, unresolved tickets, high-value and low-engagement segments
- Risk banding and next-best-action suggestions
- Explainability panel — shows why a recommendation was made
- Downloadable reports and audit logs
- India-focused mock customer data (auto-generated)

---

## Stack

| Layer | Library |
|---|---|
| App framework | Streamlit |
| Language | Python 3 |
| ML | scikit-learn (K-Means clustering, churn scoring) |
| NLP | Intent router with multilingual support |
| Data | Auto-generated India-focused mock dataset |

---

## Run locally

```bash
cd dealium26
pip install -r requirements.txt
streamlit run app.py
```

Copy `.env.example` to `.env` and fill in any API keys if using live NLP.

---

## Project structure

```
dealium26/
  app.py          # Streamlit entry point
  src/            # Intent routing, ML, data generation
  tests/          # Unit tests
  docs/           # Architecture notes
```
