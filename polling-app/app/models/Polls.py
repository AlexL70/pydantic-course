from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List, Optional
from datetime import datetime, timezone


class Poll(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str = Field(min_length=5, max_length=50)
    options: List[str]
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    expires_at: Optional[datetime] = None