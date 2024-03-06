from fastapi import APIRouter

from app.models.user_score_model import UserScore
from app.config.database import user_score_collection

from app.schemas.user_score_schema import user_scores_serializer
from bson import ObjectId

user_score_api_router = APIRouter(prefix="/user/score", tags=["User_Score"])


# retrieve
@user_score_api_router.get("/")
async def get_user_score():
    user_scores = user_scores_serializer(user_score_collection.find())
    return user_scores


@user_score_api_router.get("/{id}")
async def get_user_score(id: str):
    return user_scores_serializer(user_score_collection.find_one({"_id": ObjectId(id)}))


# post
@user_score_api_router.post("/")
async def create_user_score(user_score: UserScore):
    _id = user_score_collection.insert_one(dict(user_score))
    return user_scores_serializer(user_score_collection.find({"_id": _id.inserted_id}))


# update
@user_score_api_router.put("/{id}")
async def update_user_score(id: str, user_score: UserScore):
    user_score_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user_score)}
    )
    return user_scores_serializer(user_score_collection.find({"_id": ObjectId(id)}))


# delete
@user_score_api_router.delete("/{id}")
async def delete_user_score(id: str):
    user_score_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
