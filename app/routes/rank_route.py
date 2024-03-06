from fastapi import APIRouter

from app.models.rank_model import Rank
from app.config.database import rank_collection

from app.schemas.rank_schema import ranks_serializer
from bson import ObjectId

rank_api_router = APIRouter(prefix="/rank", tags=["Rank"])


# retrieve
@rank_api_router.get("/")
async def get_rank():
    ranks = ranks_serializer(rank_collection.find())
    return ranks


@rank_api_router.get("/{id}")
async def get_rank(id: str):
    return ranks_serializer(rank_collection.find_one({"_id": ObjectId(id)}))


# post
@rank_api_router.post("/")
async def create_rank(rank: Rank):
    _id = rank_collection.insert_one(dict(rank))
    return ranks_serializer(rank_collection.find({"_id": _id.inserted_id}))


# update
@rank_api_router.put("/{id}")
async def update_rank(id: str, rank: Rank):
    rank_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(rank)}
    )
    return ranks_serializer(rank_collection.find({"_id": ObjectId(id)}))


# delete
@rank_api_router.delete("/{id}")
async def delete_rank(id: str):
    rank_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
