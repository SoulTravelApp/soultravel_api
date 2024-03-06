from fastapi import APIRouter

from app.models.user_rank_model import UserRank
from app.config.database import user_rank_collection

from app.schemas.user_rank_schema import user_ranks_serializer
from bson import ObjectId

user_rank_api_router = APIRouter(prefix="/user/rank", tags=["User_Rank"])


# retrieve
@user_rank_api_router.get("/")
async def get_user_rank():
    ranks = user_ranks_serializer(user_rank_collection.find())
    return ranks


@user_rank_api_router.get("/{id}")
async def get_user_rank(id: str):
    return user_ranks_serializer(
        user_rank_collection.find_one({"_id": ObjectId(id)})
    )


# post
@user_rank_api_router.post("/")
async def create_user_rank(rank: UserRank):
    _id = user_rank_collection.insert_one(dict(rank))
    return user_ranks_serializer(
        user_rank_collection.find({"_id": _id.inserted_id})
    )


# update
@user_rank_api_router.put("/{id}")
async def update_user_rank(id: str, rank: UserRank):
    user_rank_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(rank)}
    )
    return user_ranks_serializer(user_rank_collection.find({"_id": ObjectId(id)}))


# delete
@user_rank_api_router.delete("/{id}")
async def delete_user_rank(id: str):
    user_rank_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
