from fastapi import APIRouter

from app.models.user_benefit_model import UserBenefit
from app.config.database import user_benefit_collection

from app.schemas.user_benefit_schema import user_benefits_serializer
from bson import ObjectId

user_benefit_api_router = APIRouter(prefix='/user/benefit', tags=["User_Benefit"])

# retrieve
@user_benefit_api_router.get("/")
async def get_user_benefit():
    benefits = user_benefits_serializer(user_benefit_collection.find())
    return benefits

@user_benefit_api_router.get("/{id}")
async def get_user_benefit(id: str):
    return user_benefits_serializer(user_benefit_collection.find_one({"_id": ObjectId(id)}))


# post
@user_benefit_api_router.post("/")
async def create_user_benefit(benefit: UserBenefit):
    _id = user_benefit_collection.insert_one(dict(benefit))
    return user_benefits_serializer(user_benefit_collection.find({"_id": _id.inserted_id}))


# update
@user_benefit_api_router.put("/{id}")
async def update_user_benefit(id: str, benefit: UserBenefit):
    user_benefit_collection.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(benefit)
    })
    return user_benefits_serializer(user_benefit_collection.find({"_id": ObjectId(id)}))

# delete
@user_benefit_api_router.delete("/{id}")
async def delete_user_benefit(id: str):
    user_benefit_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}