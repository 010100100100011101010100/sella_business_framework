# Autonomous Business Framework — Playground & Test Repo

This repository is the dedicated playground and workspace for creating business assets, prototypes, client-side dashboards, sites, landing pages, and delivery artifacts under the Autonomous Business Framework.

## Structure

```
test-repo/
├── dashboards/      Client-side static dashboards (HTML/CSS/JS, no build step, Carbon design system)
├── sites/           One-page offers, landing pages, and credibility sites
├── data/            JSON data contract files (prospects.json, touches.json, metrics.json, etc.)
├── deliveries/      Demonstration artifacts, free samples, and client deliverables
├── scripts/         Automation pipelines, sample generators, and QA scripts
└── README.md        This guide
```

## Operating Principles
- **No servers / client-side only**: Dashboards read flat JSON files from `data/`. No database, no auth backend.
- **Sell before build (G2)**: Build demonstrations and prototypes that prove value immediately.
- **Truth constraint (G3)**: Real, verified data and measurements only; models marked explicitly as models.
- **Client data protection**: No PII in metrics files; strict 30-day client data deletion policies.
