from pydantic import BaseModel
from datetime import datetime

class UserBenefit(BaseModel):
    user_id: str
    benefit_id: str
    ini_vig: str
    fim_vig: datetime
    updated_at: datetime
    created_at: datetime
    usr_adm: str