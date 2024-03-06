from pydantic import BaseModel
from datetime import datetime


class Rank(BaseModel):
    title: str
    subtitle: str
    image: str
    description: str
    min_score: int
    ini_vig: datetime
    fim_vig: datetime
    updated_at: datetime
    created_at: datetime
    usr_adm: str
