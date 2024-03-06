def rank_serializer(rank) -> dict:
    return {
        "id": str(rank["_id"]),
        "title": rank["title"],
        "subtitle": rank["subtitle"],
        "description": rank["description"],
        "min_score": rank["min_score"],
        "image": rank["image"],
        "ini_vig": rank["ini_vig"],
        "fim_vig": rank["fim_vig"],
        "updated_at": rank["updated_at"],
        "created_at": rank["created_at"],
        "usr_adm": rank["usr_adm"],
    }


def ranks_serializer(ranks) -> list:
    return [rank_serializer(rank) for rank in ranks]
