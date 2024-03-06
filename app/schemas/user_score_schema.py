def user_score_serializer(user_score) -> dict:
    return {
        "id": str(user_score["_id"]),
        "user_id": user_score["user_id"],
        "forum_contribuitions": user_score["forum_contribuitions"],
        "trips_amount": user_score["trips_amount"],
        "created_at": user_score["created_at"],
    }

def user_scores_serializer(user_scores) -> list:
    return [user_score_serializer(user_score) for user_score in user_scores]