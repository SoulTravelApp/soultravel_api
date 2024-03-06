from pydantic import BaseModel
from datetime import datetime


class Benefit(BaseModel):
    title: str
    subtitle: str
    description: str
    expire_date: datetime
    updated_at: datetime
    created_at: datetime
    usr_adm: str
