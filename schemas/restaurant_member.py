import json

from fastapi.encoders import jsonable_encoder


def RestaurantMemberModelEntity(item) -> json:
    return jsonable_encoder(
        {
            "id": str(item["_id"]),
            "name": item["name"],
            "address": item["address"],
            "phoneNo": item["phone_no"],
            "email": item["email"],
            "startDate": item["start_date"],
        }
    )


def RestaurantMemberModelsEntity(entity) -> list:
    return [RestaurantMemberModelEntity(item) for item in entity]
