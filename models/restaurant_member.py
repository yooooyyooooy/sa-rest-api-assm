from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class RestaurantMemberModel(BaseModel):
    name: str = Field(title="member's name")
    address: str = Field(title="member's address")
    phone_no: str = Field(title="member's phone number")
    email: EmailStr = Field(title="member's email")
    start_date: datetime = Field(
        default_factory=datetime.utcnow,
        title="member's start date",
    )

    class Config:
        schema_extra = {
            "examples": {
                "valid_1": {
                    "summary": "Valid Example 1",
                    "value": {
                        "name": "Pmm Clark",
                        "address": "Pmm Clark's address",
                        "phone_no": "Pmm Clark's phone no.",
                        "email": "pmmclark@gmail.com",
                    },
                },
                "valid_2": {
                    "summary": "Valid Example 2",
                    "value": {
                        "name": "Master Yoooy",
                        "address": "Master Yoooy's address",
                        "phone_no": "Master Yoooy's phone no.",
                        "email": "masteryooooy@gmail.com",
                    },
                },
                "invalid_email": {
                    "summary": "Invalid Example 1",
                    "description": "Invalid email",
                    "value": {
                        "name": "Master Yoooy",
                        "address": "Master Yoooy's address",
                        "phone_no": "Master Yoooy's phone no.",
                        "email": "wrong email format",
                    },
                },
            }
        }


class UpdateRestaurantMemberModel(BaseModel):
    name: Optional[str] = Field(title="member's name")
    address: Optional[str] = Field(title="member's address")
    phone_no: Optional[str] = Field(title="member's phone number")
    email: Optional[EmailStr] = Field(title="member's email")

    class Config:
        schema_extra = {
            "examples": {
                "valid_1": {
                    "summary": "Valid Example 1",
                    "value": {
                        "name": "Pmm Clark's new name",
                        "address": "Pmm Clark's new address",
                        "phone_no": "Pmm Clark's new phone no.",
                        "email": "pmmclark@gmail.com",
                    },
                },
                "valid_2": {
                    "summary": "Valid Example 2",
                    "value": {
                        "name": "Master Yoda",
                        "address": "Master Yoda's address",
                        "email": "masteryoda@gmail.com",
                    },
                },
                "invalid_email": {
                    "summary": "Invalid Example 1",
                    "description": "Invalid email",
                    "value": {
                        "name": "Master Yoooy",
                        "email": "wrong email format",
                    },
                },
            }
        }
