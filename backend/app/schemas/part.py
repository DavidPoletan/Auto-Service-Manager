from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

class Part(BaseModel):

    id:                int =      Field(...,  description="Unique identifier of the part")
    name:              str =      Field(...,  max_length=100,   description="Name of the part")
    manufacturer:      str =      Field(None, max_length=100,   description="Manufacturer of the part")
    part_number:       str =      Field(None, max_length=50,    description="Unique number of the part given by the manufacturer")
    unit_price:        Decimal =  Field(gt=0, decimal_places=2, description="Price of a single unit of the part")
    quantity_in_stock: int =      Field(...,  description="Number of units of the part that are currently available")
    minimum_stock:     int =      Field(None, description="Smallest amount of part's units that can be left in stock before resupplying")
    created_at:        datetime = Field(...,  description="Date and time on which the part's entry was created")
    updated_at:        datetime = Field(None, description="Date and time on which the part's entry was updated")


class PartCreate(BaseModel):

    id:                int =      Field(...,  description="Unique identifier of the part")
    name:              str =      Field(...,  max_length=100,   description="Name of the part")
    manufacturer:      str =      Field(None, max_length=100,   description="Manufacturer of the part")
    part_number:       str =      Field(None, max_length=50,    description="Unique number of the part given by the manufacturer")
    unit_price:        Decimal =  Field(gt=0, decimal_places=2, description="Price of a single unit of the part")
    quantity_in_stock: int =      Field(...,  description="Number of units of the part that are currently available")
    minimum_stock:     int =      Field(None, description="Smallest amount of part's units that can be left in stock before resupplying")


class PartResponse(BaseModel):

    id:                int =      Field(...,  description="Unique identifier of the part")
    name:              str =      Field(...,  max_length=100,   description="Name of the part")
    manufacturer:      str =      Field(None, max_length=100,   description="Manufacturer of the part")
    part_number:       str =      Field(None, max_length=50,    description="Unique number of the part given by the manufacturer")
    unit_price:        Decimal =  Field(gt=0, decimal_places=2, description="Price of a single unit of the part")
    quantity_in_stock: int =      Field(...,  description="Number of units of the part that are currently available")
    minimum_stock:     int =      Field(None, description="Smallest amount of part's units that can be left in stock before resupplying")
    created_at:        datetime = Field(...,  description="Date and time on which the part's entry was created")
    updated_at:        datetime = Field(None, description="Date and time on which the part's entry was updated")

    model_config = {"from_attributes": True}


class PartUpdate(BaseModel):

    name:              Optional[str] =      Field(None, max_length=100,   description="Name of the part")
    manufacturer:      Optional[str] =      Field(None, max_length=100,   description="Manufacturer of the part")
    part_number:       Optional[str] =      Field(None, max_length=50,    description="Unique number of the part given by the manufacturer")
    unit_price:        Optional[Decimal] =  Field(gt=0, decimal_places=2, description="Price of a single unit of the part")
    quantity_in_stock: Optional[int] =      Field(None, description="Number of units of the part that are currently available")
    minimum_stock:     Optional[int] =      Field(None, description="Smallest amount of part's units that can be left in stock before resupplying")
    updated_at:        Optional[datetime] = Field(None, description="Date and time on which the part's entry was updated")