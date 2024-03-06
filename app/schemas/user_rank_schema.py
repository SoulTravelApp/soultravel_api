def user_rank_serializer(rank) -> dict:
    return {
        "id": str(rank["_id"]),
        "user_id": rank["user_id"],
        "rank_id": rank["rank_id"],
        "ini_vig": rank["ini_vig"],
        "fim_vig": rank["fim_vig"],
        "updated_at": rank["updated_at"],
        "created_at": rank["created_at"],
        "usr_adm": rank["usr_adm"],
    }


def user_ranks_serializer(user_ranks) -> list:
    return [user_rank_serializer(user_rank) for user_rank in user_ranks]
