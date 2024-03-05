from fastapi import FastAPI
from mangum import Mangum
from pydantic import BaseModel
from typing import Union

app = FastAPI()
handler = Mangum(app)

class PostUserRequest(BaseModel):
    username: str
    email: str
    designation: Union[str, None] = None
    organization: Union[str, None] = None

@app.post("/user")
def create_user(request: PostUserRequest):
    return {"statusCode": 200, "message": "User created successfully", "item": request}