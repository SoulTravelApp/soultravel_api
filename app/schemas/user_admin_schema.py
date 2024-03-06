def user_admin_serializer(admin) -> dict:
    return {
        "id": str(admin["_id"]),
        "user_id": admin["user_id"],
        "ini_vig": admin["ini_vig"],
        "fim_vig": admin["fim_vig"],
        "updated_at": admin["updated_at"],
        "created_at": admin["created_at"],
        "usr_adm": admin["usr_adm"],
    }


def user_admins_serializer(admins) -> list:
    return [user_admin_serializer(admin) for admin in admins]
