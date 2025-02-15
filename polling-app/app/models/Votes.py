from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from uuid import UUID

class VoterCreate(BaseModel):
    """The Voter write model"""
    email: EmailStr

class Voter(VoterCreate):
    """The Voter read model"""
    voted_at: datetime = Field(default_factory=datetime.now)

class Vote(BaseModel):
    """The Vote read model"""
    poll_id: UUID
    choice_id: UUID
    voter: Voter
    
class VoteById(BaseModel):
    choice_id: UUID
    voter: VoterCreate

class VoteByLabel(BaseModel):
    choice_label: int
    voter: VoterCreate