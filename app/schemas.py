from datetime import datetime
from pydantic import BaseModel, Field

class AgentBase(BaseModel):
    name: str
    description: str | None = None
    owner: str
    business_unit: str | None = None
    environment: str = "dev"
    framework: str | None = None
    model_provider: str | None = None
    model_name: str | None = None
    risk_level: str = Field(default="medium", pattern="^(low|medium|high|critical)$")
    lifecycle_state: str = Field(default="draft", pattern="^(draft|dev|test|active|suspended|retired)$")
    criticality: str = Field(default="medium", pattern="^(low|medium|high|critical)$")
    data_sources: list[str] = []
    tools: list[str] = []
    actions: list[str] = []
    tags: list[str] = []

class AgentCreate(AgentBase):
    pass

class AgentUpdate(BaseModel):
    description: str | None = None
    owner: str | None = None
    business_unit: str | None = None
    environment: str | None = None
    framework: str | None = None
    model_provider: str | None = None
    model_name: str | None = None
    risk_level: str | None = None
    lifecycle_state: str | None = None
    criticality: str | None = None
    data_sources: list[str] | None = None
    tools: list[str] | None = None
    actions: list[str] | None = None
    tags: list[str] | None = None

class AgentOut(AgentBase):
    id: int
    created_at: datetime
    updated_at: datetime
    class Config:
        from_attributes = True

class EventCreate(BaseModel):
    event_type: str
    message: str | None = None
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0
    status: str = "info"

class EventOut(EventCreate):
    id: int
    agent_id: int
    created_at: datetime
    class Config:
        from_attributes = True

class PolicyCreate(BaseModel):
    policy_name: str
    policy_type: str = "governance"
    rule: str
    enforcement_mode: str = "monitor"

class PolicyOut(PolicyCreate):
    id: int
    agent_id: int
    created_at: datetime
    class Config:
        from_attributes = True

class CostSummary(BaseModel):
    agent_id: int
    agent_name: str
    total_input_tokens: int
    total_output_tokens: int
    total_cost_usd: float
    event_count: int
