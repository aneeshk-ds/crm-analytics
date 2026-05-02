# CRM Analytics

AI-powered CRM analytics for managing leads, customers, support signals, and sales pipelines. The current application is a Streamlit MVP called **Dealium26** that helps non-technical CRM users ask natural-language questions and get customer segments, churn-risk signals, workflow recommendations, explainability, downloadable reports, and audit logs.

## What This Project Does

Dealium26 provides a demo-first CRM assistant with:

- India-focused mock customer data generation.
- Natural-language CRM queries in English, Hindi, and Telugu.
- Intent routing for support, sales, marketing, and general CRM questions.
- Customer filtering by city, churn risk, unresolved tickets, and high-value/low-engagement segments.
- Risk banding and next-best-action suggestions.
- Workflow actions for support, sales, and marketing teams.
- Approval-aware audit log generation.
- Downloadable CSV exports for query results and audit rows.
- Session history inside the Streamlit UI.

## Project Structure

```text
.
├── README.md
└── dealium26
    ├── app.py
    ├── requirements.txt
    ├── docs
    ├── src
    │   ├── data
    │   ├── governance
    │   ├── intelligence
    │   ├── nlp
    │   ├── query
    │   ├── response
    │   ├── ui
    │   └── workflows
    └── tests
```

## Prerequisites

- Python 3.9 or newer.
- Git.
- A terminal from the repository root.

The app currently runs locally without an OpenAI API key. `.env.example` includes placeholders for future API-backed features.

## Local Setup

From the repository root:

```bash
cd dealium26
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt pytest
```

If you are reopening an existing setup, activate the virtual environment:

```bash
cd dealium26
source .venv/bin/activate
```

## Run The App

From `dealium26/` with the virtual environment activated:

```bash
streamlit run app.py --server.address 127.0.0.1 --server.port 8501 --server.headless true --browser.gatherUsageStats false
```

Open the app in your browser:

```text
http://127.0.0.1:8501
```

To stop the app, press `Ctrl+C` in the terminal running Streamlit.

## Test The Project

From `dealium26/` with the virtual environment activated:

```bash
python -m pytest
```

Expected result:

```text
12 passed
```

## Quick Smoke Test

After starting the app, try one of these queries:

```text
Show high-value customers with low engagement in Hyderabad
Show churn customers in Hyderabad
Show unresolved ticket issues
Find hot leads for follow-up
```

You should see:

- Customer count and data quality metrics.
- Detected intent, language, and filters.
- A summary response.
- Next-best-action recommendation.
- Workflow actions with approval checkboxes.
- A customer results table.
- CSV download buttons.

## Notes

- The app generates mock customer data locally under ignored runtime folders.
- `.venv/`, cache files, `.env`, and generated data are intentionally ignored by Git.
- Streamlit may show a non-blocking warning about replacing `use_container_width` with `width`; the app still runs.
