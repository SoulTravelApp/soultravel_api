from fastapi import FastAPI
from mangum import Mangum
from app.routes.user_score_route import user_score_api_router
from app.routes.benefit_route import benefit_api_router
from app.routes.user_benefit_route import user_benefit_api_router
from app.routes.user_rank_route import user_rank_api_router
from app.routes.user_admin_route import user_admin_api_router
from app.routes.badge_route import badge_api_router
from app.routes.rank_route import rank_api_router

app = FastAPI()

app.include_router(badge_api_router)
app.include_router(benefit_api_router)
app.include_router(rank_api_router)
app.include_router(user_admin_api_router)
app.include_router(user_benefit_api_router)
app.include_router(user_rank_api_router)
app.include_router(user_score_api_router)


@app.get("/", tags=['Health'])
async def health():
    return {"message": "Hello Soultravel API is working"}


handler = Mangum(app)
