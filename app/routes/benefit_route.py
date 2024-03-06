from fastapi import APIRouter

from app.models.benefit_model import Benefit
from app.config.database import benefit_collection

from app.schemas.benefit_schema import benefits_serializer
from bson import ObjectId

benefit_api_router = APIRouter(prefix="/benefit", tags=["Benefit"])


# retrieve
@benefit_api_router.get("/")
async def get_benefit():
    benefits = benefits_serializer(benefit_collection.find())
    return benefits


@benefit_api_router.get("/{id}")
async def get_benefit(id: str):
    return benefits_serializer(benefit_collection.find_one({"_id": ObjectId(id)}))


# post
@benefit_api_router.post("/")
async def create_benefit(benefit: Benefit):
    _id = benefit_collection.insert_one(dict(benefit))
    return benefits_serializer(benefit_collection.find({"_id": _id.inserted_id}))


# update
@benefit_api_router.put("/{id}")
async def update_benefit(id: str, benefit: Benefit):
    benefit_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(benefit)}
    )
    return benefits_serializer(benefit_collection.find({"_id": ObjectId(id)}))


# delete
@benefit_api_router.delete("/{id}")
async def delete_benefit(id: str):
    benefit_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
