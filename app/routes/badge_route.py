from fastapi import APIRouter

from app.models.badge_model import Badge
from app.config.database import badge_collection

from app.schemas.badge_schema import badges_serializer
from bson import ObjectId

badge_api_router = APIRouter(prefix="/badge", tags=["Badge"])


# retrieve
@badge_api_router.get("/")
async def get_badge():
    badges = badges_serializer(badge_collection.find())
    return badges


@badge_api_router.get("/{id}")
async def get_badge(id: str):
    return badges_serializer(badge_collection.find_one({"_id": ObjectId(id)}))


# post
@badge_api_router.post("/")
async def create_badge(badge: Badge):
    _id = badge_collection.insert_one(dict(badge))
    return badges_serializer(badge_collection.find({"_id": _id.inserted_id}))


# update
@badge_api_router.put("/{id}")
async def update_badge(id: str, badge: Badge):
    badge_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(badge)}
    )
    return badges_serializer(badge_collection.find({"_id": ObjectId(id)}))


# delete
@badge_api_router.delete("/{id}")
async def delete_badge(id: str):
    badge_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
