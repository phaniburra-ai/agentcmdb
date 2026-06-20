from datetime import datetime
from sqlalchemy import String, DateTime, Text, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .db import Base

class Agent(Base):
    __tablename__ = "agents"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), index=True)
    description: Mapped[str | None] = mapped_column(Text, default=None)
    owner: Mapped[str] = mapped_column(String(200), index=True)
    business_unit: Mapped[str | None] = mapped_column(String(120), default=None)
    environment: Mapped[str] = mapped_column(String(50), default="dev")
    framework: Mapped[str | None] = mapped_column(String(120), default=None)
    model_provider: Mapped[str | None] = mapped_column(String(120), default=None)
    model_name: Mapped[str | None] = mapped_column(String(120), default=None)
    risk_level: Mapped[str] = mapped_column(String(50), default="medium")
    lifecycle_state: Mapped[str] = mapped_column(String(50), default="draft")
    criticality: Mapped[str] = mapped_column(String(50), default="medium")
    data_sources_json: Mapped[str] = mapped_column(Text, default="[]")
    tools_json: Mapped[str] = mapped_column(Text, default="[]")
    actions_json: Mapped[str] = mapped_column(Text, default="[]")
    tags_json: Mapped[str] = mapped_column(Text, default="[]")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    events: Mapped[list["AgentEvent"]] = relationship(back_populates="agent", cascade="all, delete-orphan")
    policies: Mapped[list["AgentPolicy"]] = relationship(back_populates="agent", cascade="all, delete-orphan")

class AgentEvent(Base):
    __tablename__ = "agent_events"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"), index=True)
    event_type: Mapped[str] = mapped_column(String(100), index=True)
    message: Mapped[str | None] = mapped_column(Text, default=None)
    input_tokens: Mapped[int] = mapped_column(default=0)
    output_tokens: Mapped[int] = mapped_column(default=0)
    cost_usd: Mapped[float] = mapped_column(Float, default=0.0)
    status: Mapped[str] = mapped_column(String(50), default="info")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    agent: Mapped[Agent] = relationship(back_populates="events")

class AgentPolicy(Base):
    __tablename__ = "agent_policies"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    agent_id: Mapped[int] = mapped_column(ForeignKey("agents.id"), index=True)
    policy_name: Mapped[str] = mapped_column(String(200), index=True)
    policy_type: Mapped[str] = mapped_column(String(100), default="governance")
    rule: Mapped[str] = mapped_column(Text)
    enforcement_mode: Mapped[str] = mapped_column(String(50), default="monitor")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    agent: Mapped[Agent] = relationship(back_populates="policies")
