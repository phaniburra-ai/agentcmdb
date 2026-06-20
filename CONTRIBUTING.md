# Contributing to AgentCMDB

Thank you for your interest in contributing to AgentCMDB — the system of record and control plane for enterprise AI agents.

We welcome contributions from developers, architects, enterprise AI practitioners, and anyone passionate about bringing governance and visibility to AI agent ecosystems.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Pull Request Guidelines](#pull-request-guidelines)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Community](#community)

---

## Code of Conduct

This project follows a simple principle: **be respectful, be constructive, be helpful.**

We are building infrastructure for the enterprise AI era. All contributors are expected to engage professionally and inclusively.

---

## How Can I Contribute?

### 🐛 Bug Reports
Found something broken? Open an issue with clear reproduction steps.

### 💡 Feature Suggestions
Have an idea for a new capability? Open a feature request issue and describe the use case.

### 📝 Documentation
Improve README clarity, add examples, fix typos, or write tutorials.

### 🔧 Code Contributions
Fix bugs, implement roadmap features, improve test coverage, or optimize performance.

### 🧪 Testing
Write unit tests, integration tests, or share real-world usage scenarios.

### 🎨 UI/UX
Improve the Control Tower UI — design, usability, and accessibility contributions welcome.

---

## Getting Started

### Prerequisites

- Python 3.10+
- Git
- Docker (optional but recommended)

### Fork and Clone

```bash
# Fork the repo on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/agentcmdb.git
cd agentcmdb
```

### Set Up Local Environment

```bash
# Backend setup
cd backend
pip install -r requirements.txt

# Run locally
uvicorn app.main:app --reload

# Open in browser
http://localhost:8000
```

### Run with Docker

```bash
docker compose up --build
```

---

## Development Workflow

### 1. Create a Branch

Always work on a feature branch — never commit directly to `main`.

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/your-bug-fix
```

### Branch Naming Convention

| Type | Format | Example |
|------|--------|---------|
| Feature | `feature/short-description` | `feature/agent-discovery-api` |
| Bug fix | `fix/short-description` | `fix/registry-duplicate-check` |
| Documentation | `docs/short-description` | `docs/quickstart-guide` |
| Refactor | `refactor/short-description` | `refactor/cost-tracking-module` |

### 2. Make Your Changes

- Keep commits small and focused
- Write clear commit messages (see below)
- Add or update tests where relevant
- Update documentation if behavior changes

### Commit Message Format

```
type: short description (max 72 chars)

Optional longer explanation of what and why (not how).
```

**Types:**
- `feat:` — new feature
- `fix:` — bug fix
- `docs:` — documentation only
- `refactor:` — code restructure, no behavior change
- `test:` — adding or fixing tests
- `chore:` — maintenance tasks

**Examples:**
```
feat: add cost tracking per agent workflow
fix: resolve duplicate agent registration on restart
docs: add SDK usage examples to README
```

### 3. Push and Open a Pull Request

```bash
git push origin feature/your-feature-name
```

Then open a Pull Request on GitHub against the `main` branch.

---

## Pull Request Guidelines

### Before Submitting

- [ ] Code runs locally without errors
- [ ] Tests pass (if applicable)
- [ ] README or docs updated if behavior changed
- [ ] PR description clearly explains what and why
- [ ] Branch is up to date with `main`

### PR Description Template

```markdown
## What does this PR do?
[Brief description]

## Why is this change needed?
[Context and motivation]

## How was it tested?
[Steps to verify]

## Related Issues
Closes #[issue number]
```

### Review Process

- All PRs require at least one review before merging
- Maintainers aim to review PRs within 5 business days
- Please respond to review feedback within a reasonable timeframe
- Be open to discussion — the goal is the best outcome for the project

---

## Reporting Bugs

Open a GitHub Issue and include:

1. **Summary** — what happened vs what you expected
2. **Steps to reproduce** — clear, numbered steps
3. **Environment** — OS, Python version, Docker version
4. **Logs or error output** — paste relevant logs
5. **Screenshots** — if UI related

**Issue title format:**
```
[BUG] Short description of the problem
```

---

## Suggesting Features

Open a GitHub Issue with:

1. **Use case** — what problem does this solve?
2. **Proposed solution** — how would it work?
3. **Alternatives considered** — other approaches you thought of
4. **Enterprise context** — is this relevant for enterprise deployments?

**Issue title format:**
```
[FEATURE] Short description of the capability
```

---

## Areas Actively Seeking Contributions

Based on the current roadmap, these areas are high priority:

### Phase 2 (Active)
- Governance + RBAC implementation
- Lifecycle workflow engine (Dev → Test → Prod)
- Cost tracking and analytics dashboard

### Phase 3 (Upcoming)
- Policy enforcement engine
- ServiceNow integration
- Salesforce integration
- Azure AI integration
- Agent marketplace framework

### Always Welcome
- Framework integrations (LangChain, LangGraph, CrewAI, AutoGen)
- Model provider connectors (Azure OpenAI, Anthropic Claude, Google Gemini, Meta Llama)
- Documentation and tutorials
- Performance improvements
- Security hardening

---

## Community

- **Website:** [agentcmdb.com](https://agentcmdb.com)
- **Platform:** [aifactorydesignplatform.com](https://aifactorydesignplatform.com)
- **LinkedIn:** [Phani Burra](https://www.linkedin.com/in/phaniburra/)
- **GitHub Issues:** For bugs and feature requests

---

## Recognition

All contributors will be acknowledged in the project. Significant contributors may be invited to join as project maintainers.

We are building the **standard system of record for enterprise AI agents** — and every contribution, large or small, moves that vision forward.

Thank you for being part of this.

---

*AgentCMDB — System of Record + Control Plane for Enterprise AI Agents*
