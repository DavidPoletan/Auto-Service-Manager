from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from enum import Enum

class Role(Enum):

    Admin =        'ADMIN'
    Receptionist = 'RECEPTIONIST'
    Mechanic =     'MECHANIC'


class User(BaseModel):

    id:            int =      Field(..., description="Unique identifer of the user")
    username:      str =      Field(..., max_length=50,  description="Username (duh)")
    email:         str =      Field(..., max_length=255, description="Email address of the user")
    passwird_hash: str =      Field(..., description="Hash value of the user's password")
    first_name:    str =      Field(..., max_length=50, description="First name of the user")
    last_name:     str =      Field(..., max_length=50, description="Last name of the user")
    role:          Role =     Field(default=Role.Admin, description="Role that was given to the user")
    active:        bool =     Field(default=True, description="Status of user's activity")
    created_at:    datetime = Field(...,  description="Date and time on which the user was created")
    updated_at:    datetime = Field(None, description="Date and time on which the user was updated")


class UserCreate(BaseModel):

    id:            int =  Field(..., description="Unique identifer of the user")
    username:      str =  Field(..., max_length=50,  description="Username (duh)")
    email:         str =  Field(..., max_length=255, description="Email address of the user")
    passwird_hash: str =  Field(..., description="Hash value of the user's password")
    first_name:    str =  Field(..., max_length=50, description="First name of the user")
    last_name:     str =  Field(..., max_length=50, description="Last name of the user")
    role:          Role = Field(default=Role.Admin, description="Role that was given to the user")
    active:        bool = Field(default=True, description="Status of user's activity")


class UserResponse(BaseModel):

    id:            int =      Field(..., description="Unique identifer of the user")
    username:      str =      Field(..., max_length=50,  description="Username (duh)")
    email:         str =      Field(..., max_length=255, description="Email address of the user")
    passwird_hash: str =      Field(..., description="Hash value of the user's password")
    first_name:    str =      Field(..., max_length=50, description="First name of the user")
    last_name:     str =      Field(..., max_length=50, description="Last name of the user")
    role:          Role =     Field(default=Role.Admin, description="Role that was given to the user")
    active:        bool =     Field(default=True, description="Status of user's activity")
    created_at:    datetime = Field(...,  description="Date and time on which the user was created")
    updated_at:    datetime = Field(None, description="Date and time on which the user was updated")

    model_config = {"from_attributes": True}


class UserUpdate(BaseModel):

    username:      Optional[str] =      Field(None, max_length=50,  description="Username (duh)")
    email:         Optional[str] =      Field(None, max_length=255, description="Email address of the user")
    passwird_hash: Optional[str] =      Field(None, description="Hash value of the user's password")
    first_name:    Optional[str] =      Field(None, max_length=50, description="First name of the user")
    last_name:     Optional[str] =      Field(None, max_length=50, description="Last name of the user")
    role:          Optional[Role] =     Field(None, description="Role that was given to the user")
    active:        Optional[bool] =     Field(default=True, description="Status of user's activity")
    updated_at:    Optional[datetime] = Field(None, description="Date and time on which the user was updated")