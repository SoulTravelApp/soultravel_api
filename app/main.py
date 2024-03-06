from fastapi import FastAPI
from mangum import Mangum
from app.routes.user_score_route import user_score_api_router
from app.routes.benefit_route import benefit_api_router

app = FastAPI()

app.include_router(user_score_api_router)
app.include_router(benefit_api_router)

@app.get("/")
async def health():
    return {"message": "Hello Soultravel API is working"}

handler = Mangum(app)