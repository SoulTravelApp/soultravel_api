from pydantic import BaseModel
from datetime import datetime


class Badge(BaseModel):
    title: str
    subtitle: str
    image: str
    description: str
    ini_vig: datetime
    fim_vig: datetime
    updated_at: datetime
    created_at: datetime
    usr_adm: str
