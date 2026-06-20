# AgentCMDB 🚀
### System of Record + Control Plane for Enterprise AI Agents

AgentCMDB is the **ServiceNow for AI Agents** — a system of record, governance layer, and control plane for managing AI agents at enterprise scale.

---

## 🧠 Why AgentCMDB?

Enterprises are rapidly deploying AI agents across workflows, tools, and platforms.

But there’s a growing problem:

## ❗ The Problem

- No central inventory of AI agents  
- Ownership is unclear  
- Governance is inconsistent  
- Costs are invisible  
- Failures are hard to trace  

This creates **“Agent Sprawl”** — similar to shadow IT, but harder to control.

---

## ✅ The Solution

AgentCMDB provides:

- 🧾 A **CMDB for AI agents**
- 🔍 Full **visibility across all agents**
- 🔐 Governance and policy enforcement
- 💰 Cost tracking and optimization
- 🧭 A centralized **AI control plane**

---

## 🎯 Positioning

Built for the era of AI agents — just as:

- ServiceNow manages IT assets  
- Salesforce manages customer data  

👉 **AgentCMDB manages AI agents**

---

## 👥 Who is this for?

- CIO / CTO → enterprise AI visibility & governance  
- Platform teams → AI infrastructure & lifecycle  
- Developers → agent registry & control  
- Risk / compliance teams → guardrails & audit  

---

## 🎯 Key Capabilities

### 🧾 Agent Registry (CMDB)
- Inventory of all AI agents
- Ownership, metadata, dependencies
- Risk classification + lifecycle state

### 🔍 Agent Discovery
- Register agents from:
  - LangChain / LangGraph  
  - CrewAI  
  - Copilot / APIs  
  - CI/CD pipelines  

### 🧭 Control Tower (UI)
- View all agents across the organization  
- Monitor workflows, failures, activity  
- Track agent health and usage  

### 🔄 Lifecycle Management
- Dev → Test → Prod workflows  
- Versioning + rollback  
- Approval workflows (enterprise)  

### 🔐 Governance + Policy Engine
- Data access control  
- Agent permissions  
- Runtime guardrails  

### 💰 Cost & FinOps for AI
- Token usage tracking  
- Cost per agent / workflow  
- ROI visibility  

---

## 🧪 Example Scenario

A company has:
- 120 AI agents across finance, HR, and customer support  
- Built using LangGraph, Copilot, APIs  

With AgentCMDB:

✅ All agents are automatically registered  
✅ Ownership and risk are defined  
✅ Cost and usage are centrally tracked  
✅ Policy violations trigger alerts  

👉 Outcome:
- Governance  
- Cost control  
- Production readiness  

---

## 🏗️ Architecture

AgentCMDB acts as a centralized control layer between AI agents and enterprise workflows.
```
AI Agents → AgentCMDB → Control Plane → Governance → Business Outcomes

Frontend (Control Tower UI)
        │
        ▼
Agent Control Plane
- Lifecycle
- Governance
- Cost
- Observability

        │
        ▼
Agent Registry (CMDB)
        │
        ▼
Agent Runtime
(LangChain, CrewAI, APIs, Copilot)
```
---
## ⚡ Quick Start

### Prerequisites
- Python 3.10+
- Docker (optional)

---

### Run locally

git clone https://github.com/your-org/agentcmdb  
cd agentcmdb/backend  

pip install -r requirements.txt  
uvicorn app.main:app --reload  

Open:  
http://localhost:8000  

---

### Run with Docker

docker compose up --build  

---

## 🔌 API & SDK

### SDK Example

from agentcmdb import register_agent

register_agent(
    name="Fraud Detection Agent",
    owner="Risk Team",
    framework="LangGraph",
    model_provider="Azure OpenAI",
    risk_level="critical"
)

---

### API Example

POST /api/agents

{
  "name": "Invoice Processing Agent",
  "owner": "Finance Team",
  "environment": "prod",
  "risk_level": "high"
}

AgentCMDB provides APIs to:
- Register and discover agents  
- Track events and activity  
- Attach governance policies  
- Monitor cost and usage  

---

## 🛣️ Roadmap

### Phase 1 (MVP)
- Agent registry (CMDB)  
- Discovery API  
- Basic control UI  

### Phase 2
- Governance + RBAC  
- Lifecycle workflows (Dev → Test → Prod)  
- Cost tracking and analytics  

### Phase 3
- Agent marketplace  
- Policy enforcement engine  
- Enterprise integrations (ServiceNow, Salesforce, Azure, etc.)  

---

## 🏢 Open Core Model

| Feature | OSS | Enterprise |
|--------|-----|------------|
| Agent registry | ✅ | ✅ |
| API | ✅ | ✅ |
| Discovery | ✅ | ✅ |
| Basic UI | ✅ | ✅ |
| RBAC | ❌ | ✅ |
| Policy enforcement | ❌ | ✅ |
| SSO / Identity | ❌ | ✅ |
| Advanced analytics | ❌ | ✅ |

---

## 🚀 Vision

AgentCMDB aims to become the **standard system of record and control plane for enterprise AI agents**.

As organizations scale AI adoption, agents will become critical digital assets — requiring the same level of governance, visibility, and lifecycle management as:

- IT infrastructure (ServiceNow)  
- Customer data platforms (Salesforce)  

👉 AgentCMDB defines this new category for the AI era.


