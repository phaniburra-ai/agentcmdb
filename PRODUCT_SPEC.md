# AgentCMDB Product Specification

## Vision
Create the enterprise system of record and operational control plane for AI agents, similar to how ServiceNow CMDB and ITSM manage IT assets and operational workflows.

## Primary users
- CIO / CTO: estate visibility and governance.
- CISO / Risk: policy, access, audit, and runtime controls.
- Platform Engineering: reusable agent registry and deployment readiness.
- Business Owners: understand value, cost, ownership, and adoption.
- Developers: discover reusable agents and register new ones.

## Core entities

### Agent
An autonomous or semi-autonomous AI software asset that can reason, call tools, access data, and execute workflows.

### Agent Registry
The authoritative system of record for agent identity, ownership, lifecycle, dependencies, and risk.

### Agent Event
Runtime or governance telemetry from an agent, such as execution, failure, policy violation, escalation, or cost event.

### Agent Policy
A rule attached to an agent or group of agents that governs access, behavior, compliance, or deployment.

## MVP workflows

1. Register an AI agent.
2. Search agent inventory.
3. Review ownership, risk, data access, tools, and actions.
4. Log runtime events.
5. Attach governance policies.
6. Review cost by agent.

## Enterprise workflows

1. Automated discovery from frameworks and platforms.
2. Risk scoring based on data access, autonomy, and criticality.
3. Approval workflow before production deployment.
4. Runtime policy enforcement.
5. Incident creation when agent fails or violates policy.
6. Cost chargeback to business unit.
7. Agent retirement and decommissioning.

## Open-core boundaries

### Open source
- Registry
- API
- Discovery endpoint
- Events
- Simple UI
- Cost summary

### Enterprise
- SSO
- RBAC
- Approval workflows
- Policy-as-code
- Connectors
- Audit exports
- Runtime guardrails
- Advanced analytics
