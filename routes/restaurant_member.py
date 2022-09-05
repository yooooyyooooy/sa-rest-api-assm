from bson import ObjectId
from configs.db import db
from core.json_response import FailureJSONResponse, SuccessJSONResponse
from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models.restaurant_member import RestaurantMemberModel, UpdateRestaurantMemberModel
from schemas.restaurant_member import (
    RestaurantMemberModelEntity,
    RestaurantMemberModelsEntity,
)

router = APIRouter(prefix="/restaurant-member")


@router.get("/", response_class=JSONResponse)
async def find_all_members():
    members = RestaurantMemberModelsEntity(db["restaurant-member"].find())
    return SuccessJSONResponse(status_code=status.HTTP_200_OK, content=members)


@router.get("/{id}", response_class=JSONResponse)
async def find_member_by_id(id: str):
    if not ObjectId.is_valid(id):
        return FailureJSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content="invalid object id",
        )

    res = db["restaurant-member"].find_one({"_id": ObjectId(id)})

    if res:
        member = RestaurantMemberModelEntity(res)
        return SuccessJSONResponse(status_code=status.HTTP_200_OK, content=member)
    else:
        return FailureJSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content="member not found"
        )


@router.post("/", response_class=JSONResponse)
async def create_user(
    member: RestaurantMemberModel = Body(
        ..., examples=RestaurantMemberModel.Config.schema_extra["examples"]
    ),
):
    new_member_id = (
        db["restaurant-member"].insert_one(jsonable_encoder(member))
    ).inserted_id

    new_member = RestaurantMemberModelEntity(
        db["restaurant-member"].find_one({"_id": ObjectId(new_member_id)})
    )

    return SuccessJSONResponse(status_code=status.HTTP_201_CREATED, content=new_member)


@router.put("/{id}", response_class=JSONResponse)
async def update_member(
    id: str,
    to_be_updated_member: UpdateRestaurantMemberModel = Body(
        ..., examples=UpdateRestaurantMemberModel.Config.schema_extra["examples"]
    ),
):
    if not ObjectId.is_valid(id):
        return FailureJSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content="invalid object id",
        )

    new_member_info = {
        k: v for k, v in jsonable_encoder(to_be_updated_member).items() if v is not None
    }

    db["restaurant-member"].find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": new_member_info}
    )

    res = db["restaurant-member"].find_one({"_id": ObjectId(id)})
    if res:
        updated_member = RestaurantMemberModelEntity(res)
        return SuccessJSONResponse(
            status_code=status.HTTP_200_OK, content=updated_member
        )
    else:
        return FailureJSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content="member not found"
        )


@router.delete("/{id}", response_class=JSONResponse)
async def delete_member(id: str):
    if not ObjectId.is_valid(id):
        return FailureJSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content="invalid object id",
        )

    res = db["restaurant-member"].find_one_and_delete({"_id": ObjectId(id)})

    if res:
        deleted_member = RestaurantMemberModelEntity(res)
        return SuccessJSONResponse(
            status_code=status.HTTP_200_OK, content=deleted_member
        )
    else:
        return FailureJSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, content="member not found"
        )
