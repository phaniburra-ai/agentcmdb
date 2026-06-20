from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from .db import Base, engine, get_db
from .security import require_api_key
from . import models, schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AgentCMDB MVP",
    description="System of record and control plane starter for enterprise AI agents.",
    version="0.1.0",
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def web_console():
    return FileResponse("static/index.html")

@app.get("/api/health")
def health():
    return {"status": "ok", "product": "AgentCMDB", "version": "0.1.0"}

@app.post("/api/agents", response_model=schemas.AgentOut, dependencies=[Depends(require_api_key)])
def create_agent(payload: schemas.AgentCreate, db: Session = Depends(get_db)):
    return crud.agent_to_schema(crud.create_agent(db, payload))

@app.get("/api/agents", response_model=list[schemas.AgentOut])
def list_agents(q: str | None = None, owner: str | None = None, risk_level: str | None = None, db: Session = Depends(get_db)):
    query = db.query(models.Agent)
    if q:
        query = query.filter(models.Agent.name.ilike(f"%{q}%"))
    if owner:
        query = query.filter(models.Agent.owner.ilike(f"%{owner}%"))
    if risk_level:
        query = query.filter(models.Agent.risk_level == risk_level)
    return [crud.agent_to_schema(a) for a in query.order_by(models.Agent.updated_at.desc()).all()]

@app.get("/api/agents/{agent_id}", response_model=schemas.AgentOut)
def get_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.get(models.Agent, agent_id)
    if not agent:
        raise HTTPException(404, "Agent not found")
    return crud.agent_to_schema(agent)

@app.patch("/api/agents/{agent_id}", response_model=schemas.AgentOut, dependencies=[Depends(require_api_key)])
def update_agent(agent_id: int, payload: schemas.AgentUpdate, db: Session = Depends(get_db)):
    agent = db.get(models.Agent, agent_id)
    if not agent:
        raise HTTPException(404, "Agent not found")
    return crud.agent_to_schema(crud.update_agent(db, agent, payload))

@app.delete("/api/agents/{agent_id}", dependencies=[Depends(require_api_key)])
def delete_agent(agent_id: int, db: Session = Depends(get_db)):
    agent = db.get(models.Agent, agent_id)
    if not agent:
        raise HTTPException(404, "Agent not found")
    db.delete(agent)
    db.commit()
    return {"deleted": True, "agent_id": agent_id}

@app.post("/api/discovery/register", response_model=schemas.AgentOut, dependencies=[Depends(require_api_key)])
def discovery_register(payload: schemas.AgentCreate, db: Session = Depends(get_db)):
    # Starter discovery behavior: create a new registry item.
    # Future: de-duplicate by source fingerprint, framework ID, repo, or runtime endpoint.
    return crud.agent_to_schema(crud.create_agent(db, payload))

@app.post("/api/agents/{agent_id}/events", response_model=schemas.EventOut, dependencies=[Depends(require_api_key)])
def add_event(agent_id: int, payload: schemas.EventCreate, db: Session = Depends(get_db)):
    if not db.get(models.Agent, agent_id):
        raise HTTPException(404, "Agent not found")
    return crud.add_event(db, agent_id, payload)

@app.get("/api/agents/{agent_id}/events", response_model=list[schemas.EventOut])
def list_events(agent_id: int, db: Session = Depends(get_db)):
    return db.query(models.AgentEvent).filter(models.AgentEvent.agent_id == agent_id).order_by(models.AgentEvent.created_at.desc()).all()

@app.post("/api/agents/{agent_id}/policies", response_model=schemas.PolicyOut, dependencies=[Depends(require_api_key)])
def add_policy(agent_id: int, payload: schemas.PolicyCreate, db: Session = Depends(get_db)):
    if not db.get(models.Agent, agent_id):
        raise HTTPException(404, "Agent not found")
    return crud.add_policy(db, agent_id, payload)

@app.get("/api/agents/{agent_id}/policies", response_model=list[schemas.PolicyOut])
def list_policies(agent_id: int, db: Session = Depends(get_db)):
    return db.query(models.AgentPolicy).filter(models.AgentPolicy.agent_id == agent_id).order_by(models.AgentPolicy.created_at.desc()).all()

@app.get("/api/costs/summary", response_model=list[schemas.CostSummary])
def get_cost_summary(db: Session = Depends(get_db)):
    return crud.cost_summary(db)
