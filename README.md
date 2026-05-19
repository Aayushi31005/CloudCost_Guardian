# CloudCost Guardian

![Python](https://img.shields.io/badge/backend-Python-blue)
![FastAPI](https://img.shields.io/badge/API-FastAPI-green)
![React](https://img.shields.io/badge/frontend-React-blue)
![TypeScript](https://img.shields.io/badge/language-TypeScript-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A preventive cloud cost monitoring prototype that detects potential overspend **before cloud budgets are exceeded**.

CloudCost Guardian models cloud cost governance as a **deterministic backend pipeline** that converts usage telemetry into early, explainable alerts.

Instead of reacting to billing dashboards after spending occurs, the system continuously evaluates usage against budget policies and warns engineers **before unexpected cloud bills appear**.

**CloudCost Guardian** is a deterministic backend pipeline that ingests cloud usage events, estimates costs using configuration-driven pricing rules, aggregates spend across policy windows, evaluates budget policies, and emits preventive alerts before potential cloud overspend occurs.

---

## The Idea

The idea for this project came from a discussion in a **Cloud Architecture & Services lecture** where we talked about a common problem engineers face in real-world systems: **unexpected cloud bills**.

Sometimes a compute instance is left running.

Sometimes a script scales infrastructure unintentionally.

Sometimes a development environment is forgotten.

These small mistakes can accumulate **large cloud bills**.

Existing cloud tools usually notify users **after spending limits are exceeded**.

CloudCost Guardian explores a different approach:

> Detect cost risks early and warn developers **before the budget is crossed**.

---

## Key Features

- Deterministic cost estimation engine
- Configuration-driven pricing rules
- Policy-based budget enforcement
- Preventive alert stages (approaching / projected / exceeded)
- Real-time monitoring dashboard
- Service-level cost tracking (EC2 / S3)
- Historical analytics (daily / weekly / monthly)
- Simulator-driven telemetry ingestion
- **Real-time popup notifications for cost alerts**

---

## System Architecture

The system processes usage telemetry through a deterministic pipeline.

```
Usage Simulator
      ↓
Usage Collection Engine
      ↓
Cost Estimation Engine
      ↓
Cost Aggregation Engine
      ↓
Policy Evaluation Engine
      ↓
Alert Engine
      ↓
Monitoring Dashboard
```

Each stage performs a single transformation, keeping the system modular and easy to reason about.

---

## Preventive Alert Model

Unlike traditional cloud billing alerts that trigger after overspend occurs, CloudCost Guardian emits **preventive alerts**.

| Stage | Condition |
|------|------|
| Approaching | Spend ≥ warning threshold |
| Projected | Current usage may exceed the budget |
| Exceeded | Budget limit crossed |

Alerts are shown in:

- the dashboard alert panel
- **real-time popup notifications**

---

## Dashboard Features

The monitoring dashboard provides visibility into the cost pipeline.

Features include:

- Daily / Weekly / Monthly spend metrics
- Service-level cost tracking
- Cost trend visualization
- Budget configuration controls
- Simulator control panel
- Preventive alert display
- Real-time notification alerts

  The frontend acts primarily as a monitoring and visualization layer, while the core system behavior and business logic remain backend-driven.

---

## Technology Stack

### Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Pytest
- YAML configuration

### Frontend

- React
- TypeScript
- TailwindCSS
- Recharts
- React Hot Toast (notification alerts)

---

## Simulator Mode

Because the prototype does not integrate with real cloud provider APIs, the system includes a **usage simulator**.

The simulator:

- generates usage events every few seconds
- simulates EC2 and S3 workloads
- drives the entire monitoring pipeline

This allows the system to behave similarly to real telemetry ingestion.
The simulator was intentionally designed to mimic real telemetry ingestion while avoiding dependency on external cloud APIs during the prototype phase.

---

## Running the Project

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## Screenshots

### Dashboard Overview
![Dashboard](screenshots/dashboard.png)

### Cost Trend Analytics
![Trend](screenshots/trend.png)

### Budget Configuration
![Budget](screenshots/budget.png)

### Alert System
![Alerts](screenshots/alerts.png)

### Real-Time Alert Notification
![Notification](screenshots/notification.png)

---

## Reliability and System Refinements

Several reliability and correctness improvements were implemented during development, including:

- dashboard crash prevention using React error boundaries
- service-specific budget persistence
- cumulative EC2 free-tier billing correction
- dynamic policy reload behavior
- weekly analytics support
- simulator thread stability improvements
- real-time toast notifications for alerts
- corrected daily / weekly / monthly aggregation logic

These refinements improved both system correctness and monitoring realism.

---

## Project Scope

CloudCost Guardian is intentionally scoped as a **prototype**.

The goal of this project is to explore backend system design for preventive cloud cost monitoring.

Out of scope:

- real cloud provider integrations
- authentication systems
- multi-tenant infrastructure
- distributed ingestion pipelines

---



## Future Improvements

Potential future extensions include:

- real AWS / Azure / GCP usage ingestion
- Slack / PagerDuty alert integrations
- anomaly detection for unusual spending patterns
- distributed event ingestion pipelines
- team-level cost attribution
- CI/CD cost guardrails

---

## License

This project is licensed under the **MIT License**.

See the LICENSE file for details.

---

## Author

Developed by **Aayushi Narang**

Software Engineering Project
Cloud Systems / Backend Architecture
