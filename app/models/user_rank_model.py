from pydantic import BaseModel
from datetime import datetime


class UserRank(BaseModel):
    user_id: str
    rank_id: str
    ini_vig: datetime
    fim_vig: datetime
    updated_at: datetime
    created_at: datetime
    usr_adm: str
