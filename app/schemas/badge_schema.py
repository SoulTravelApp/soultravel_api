def badge_serializer(badge) -> dict:
    return {
        "id": str(badge["_id"]),
        "title": badge["title"],
        "subtitle": badge["subtitle"],
        "description": badge["description"],
        "image": badge["image"],
        "ini_vig": badge["ini_vig"],
        "fim_vig": badge["fim_vig"],
        "updated_at": badge["updated_at"],
        "created_at": badge["created_at"],
        "usr_adm": badge["usr_adm"],
    }


def badges_serializer(badges) -> list:
    return [badge_serializer(badge) for badge in badges]
