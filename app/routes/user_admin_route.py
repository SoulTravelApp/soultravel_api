from fastapi import APIRouter

from app.models.user_admin_model import UserAdmin
from app.config.database import user_admin_collection

from app.schemas.user_admin_schema import user_admins_serializer
from bson import ObjectId

user_admin_api_router = APIRouter(prefix="/user/admin", tags=["User_Admin"])


# retrieve
@user_admin_api_router.get("/")
async def get_user_admin():
    admins = user_admins_serializer(user_admin_collection.find())
    return admins


@user_admin_api_router.get("/{id}")
async def get_user_admin(id: str):
    return user_admins_serializer(
        user_admin_collection.find_one({"_id": ObjectId(id)})
    )


# post
@user_admin_api_router.post("/")
async def create_user_admin(admin: UserAdmin):
    _id = user_admin_collection.insert_one(dict(admin))
    return user_admins_serializer(
        user_admin_collection.find({"_id": _id.inserted_id})
    )


# update
@user_admin_api_router.put("/{id}")
async def update_user_admin(id: str, admin: UserAdmin):
    user_admin_collection.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(admin)}
    )
    return user_admins_serializer(user_admin_collection.find({"_id": ObjectId(id)}))


# delete
@user_admin_api_router.delete("/{id}")
async def delete_user_admin(id: str):
    user_admin_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok"}
