def user_benefit_serializer(benefit) -> dict:
    return {
        "id": str(benefit["_id"]),
        "user_id": benefit["user_id"],
        "benefit_id": benefit["benefit_id"],
        "ini_vig": benefit["ini_vig"],
        "fim_vig": benefit["fim_vig"],
        "updated_at": benefit["updated_at"],
        "created_at": benefit["created_at"],
        "usr_adm": benefit["usr_adm"],
    }

def user_benefits_serializer(user_benefits) -> list:
    return [user_benefit_serializer(user_benefit) for user_benefit in user_benefits]