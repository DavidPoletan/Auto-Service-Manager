from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class Customer(BaseModel):

    id:         int =      Field(...,  description="Unique identifier of the customer")
    first_name: str =      Field(...,  max_length=50,  description="First name of the customer")
    last_name:  str =      Field(...,  max_length=50,  description="Last name of the customer")
    phone:      str =      Field(None, max_length=30,  description="Phone number of the customer")
    email:      str =      Field(None, max_length=255, description="Email address of the customer")
    address:    str =      Field(None, description="Address of residence of the customer")
    created_at: datetime = Field(...,  description="Date and time on which the customer's entry was created")
    updated_at: datetime = Field(None, description="Date and time on which the customer's entry was updated")


class CustomerCreate(BaseModel):

    id:         int = Field(...,  description="Unique identifier of the customer")
    first_name: str = Field(...,  max_length=50,  description="First name of the customer")
    last_name:  str = Field(...,  max_length=50,  description="Last name of the customer")
    phone:      str = Field(None, max_length=30,  description="Phone number of the customer")
    email:      str = Field(None, max_length=255, description="Email address of the customer")
    address:    str = Field(None, description="Address of residence of the customer")


class CustomerResponse(BaseModel):

    id:         int =      Field(...,  description="Unique identifier of the customer")
    first_name: str =      Field(...,  max_length=50,  description="First name of the customer")
    last_name:  str =      Field(...,  max_length=50,  description="Last name of the customer")
    phone:      str =      Field(None, max_length=30,  description="Phone number of the customer")
    email:      str =      Field(None, max_length=255, description="Email address of the customer")
    address:    str =      Field(None, description="Address of residence of the customer")
    created_at: datetime = Field(...,  description="Date and time on which the customer's entry was created")
    updated_at: datetime = Field(None, description="Date and time on which the customer's entry was updated")

    model_config = {"from_attributes": True}


class CustomerUpdate(BaseModel):

    first_name: Optional[str] =      Field(None, max_length=50,  description="First name of the customer")
    last_name:  Optional[str] =      Field(None, max_length=50,  description="Last name of the customer")
    phone:      Optional[str] =      Field(None, max_length=30,  description="Phone number of the customer")
    email:      Optional[str] =      Field(None, max_length=255, description="Email address of the customer")
    address:    Optional[str] =      Field(None, description="Address of residence of the customer")
    updated_at: Optional[datetime] = Field(None, description="Date and time on which the customer's entry was updated")