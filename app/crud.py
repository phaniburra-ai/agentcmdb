import json
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

def _dump(v):
    return json.dumps(v or [])

def _load(v):
    try:
        return json.loads(v or "[]")
    except Exception:
        return []

def agent_to_schema(agent: models.Agent) -> schemas.AgentOut:
    return schemas.AgentOut(
        id=agent.id,
        name=agent.name,
        description=agent.description,
        owner=agent.owner,
        business_unit=agent.business_unit,
        environment=agent.environment,
        framework=agent.framework,
        model_provider=agent.model_provider,
        model_name=agent.model_name,
        risk_level=agent.risk_level,
        lifecycle_state=agent.lifecycle_state,
        criticality=agent.criticality,
        data_sources=_load(agent.data_sources_json),
        tools=_load(agent.tools_json),
        actions=_load(agent.actions_json),
        tags=_load(agent.tags_json),
        created_at=agent.created_at,
        updated_at=agent.updated_at,
    )

def create_agent(db: Session, payload: schemas.AgentCreate):
    agent = models.Agent(
        name=payload.name,
        description=payload.description,
        owner=payload.owner,
        business_unit=payload.business_unit,
        environment=payload.environment,
        framework=payload.framework,
        model_provider=payload.model_provider,
        model_name=payload.model_name,
        risk_level=payload.risk_level,
        lifecycle_state=payload.lifecycle_state,
        criticality=payload.criticality,
        data_sources_json=_dump(payload.data_sources),
        tools_json=_dump(payload.tools),
        actions_json=_dump(payload.actions),
        tags_json=_dump(payload.tags),
    )
    db.add(agent)
    db.commit()
    db.refresh(agent)
    return agent

def update_agent(db: Session, agent: models.Agent, payload: schemas.AgentUpdate):
    data = payload.model_dump(exclude_unset=True)
    list_fields = {"data_sources": "data_sources_json", "tools": "tools_json", "actions": "actions_json", "tags": "tags_json"}
    for k, v in data.items():
        if k in list_fields:
            setattr(agent, list_fields[k], _dump(v))
        else:
            setattr(agent, k, v)
    agent.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(agent)
    return agent

def add_event(db: Session, agent_id: int, payload: schemas.EventCreate):
    event = models.AgentEvent(agent_id=agent_id, **payload.model_dump())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def add_policy(db: Session, agent_id: int, payload: schemas.PolicyCreate):
    policy = models.AgentPolicy(agent_id=agent_id, **payload.model_dump())
    db.add(policy)
    db.commit()
    db.refresh(policy)
    return policy

def cost_summary(db: Session):
    rows = (
        db.query(
            models.Agent.id,
            models.Agent.name,
            func.coalesce(func.sum(models.AgentEvent.input_tokens), 0),
            func.coalesce(func.sum(models.AgentEvent.output_tokens), 0),
            func.coalesce(func.sum(models.AgentEvent.cost_usd), 0.0),
            func.count(models.AgentEvent.id),
        )
        .outerjoin(models.AgentEvent, models.Agent.id == models.AgentEvent.agent_id)
        .group_by(models.Agent.id)
        .all()
    )
    return [
        schemas.CostSummary(
            agent_id=r[0], agent_name=r[1], total_input_tokens=r[2],
            total_output_tokens=r[3], total_cost_usd=round(float(r[4]), 4), event_count=r[5]
        )
        for r in rows
    ]
