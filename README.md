# 🤖 AI-Powered Adaptive Learning Platform

A real-time, data-driven career synchronization engine that cross-references user technical profiles against current industry frameworks. The platform assesses skill gaps, dynamically visualizes market supply-vs-demand trends, and compiles a modular, downloadable learning blueprint.

🎯 **Live Deployment Link:** [Click Here to View the App](https://ailearningplatform-bybhuvan.streamlit.app)

---

## ⚡ Core Technical Features

* **Dynamic Profile Structuring:** Captures multi-tier candidate profiles including baseline skill matrices and target career domains.
* **Predictive Market Diagnosis:** Uses semantic LLM evaluation to index real-time market demand statuses, average entry salary brackets, and localized hiring velocity.
* **Automated Skill-Gap Analytics:** Intersects current user capabilities against technical benchmarks to issue tactical warnings regarding legacy stack vulnerabilities.
* **Interactive Data Visualization:** Maps generative data frames directly into synchronized Streamlit line charts showing job volume ratios vs. applicant density trends.
* **Offline Document Serialization:** Formats runtime in-memory session arrays into an integrated, localized text blueprint downloadable instantly via browser sandboxes.

---

## 🏗️ System Architecture & Data Flow

The application utilizes a decoupled, three-tier micro-architecture optimized for lightweight execution and zero computational overhead on the client side:

```text
[ Streamlit UI Frontend ] ➔ Captures Inputs ➔ Initiates Session Memory State
       │
       ▼ (Passes Parameters)
[ Core AI Translation Layer (ai_engine.py) ] ➔ Establishes Client Authentication
       │
       ▼ (Strict JSON Schema Constraints)
[ LLM Cognitive Engine (Gemini 2.5 Flash) ] ➔ Generates Structured Response
       │
       ▼ (Safe Validation & Error Fallbacks)
[ Pandas DataFrame Parsing Engine ] ➔ Renders Interactive Web Charts & Tables
