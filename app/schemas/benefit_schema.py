def benefit_serializer(benefit) -> dict:
    return {
        "id": str(benefit["_id"]),
        "title": benefit["title"],
        "subtitle": benefit["subtitle"],
        "description": benefit["description"],
        "expire_date": benefit["expire_date"],
        "updated_at": benefit["updated_at"],
        "created_at": benefit["created_at"],
        "usr_adm": benefit["usr_adm"],
    }

def benefits_serializer(benefits) -> list:
    return [benefit_serializer(benefit) for benefit in benefits]