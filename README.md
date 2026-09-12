# MySQL SQL Agent with LangChain, Gemini & LangSmith

An autonomous natural-language-to-SQL agent that queries MySQL databases using Google Gemini, orchestrated with LangChain and monitored via LangSmith.

## Features
- **Zero-Shot / Tool-Calling SQL Execution:** Translates plain English into dialect-compliant MySQL statements.
- **Safety Safeguards:** Rejects destructive write operations (`INSERT`, `UPDATE`, `DELETE`, `DROP`).
- **Observability:** Automatic tracing of token costs, intermediate thoughts, and raw SQL queries via LangSmith.
- **Dual Interfaces:** Command-line runner (`app.py`) and Web Chat UI (`streamlit_app.py`).

---

## 1. Setup

### Clone and Create Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt