from pydantic import BaseModel
from datetime import datetime

class UserScore(BaseModel):
    user_id: str
    forum_contribuitions: int
    trips_amount: int
    created_at: datetime