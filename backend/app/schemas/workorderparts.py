from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

class WorkOrderParts(BaseModel):

    workorder_id: int
    part_id:      int
    quantity:     int = Field(gt=0, description="Quantity of parts used for the given work order")


class WorkOrderPartsCreate(BaseModel):

    part_id:  int
    quantity: int = Field(gt=0, description="Quantity of parts used for the given work order")


class WorkOrderPartsResponse(BaseModel):
    workorder_id: int
    part_id:      int
    part_name:    str
    unit_price:   Decimal
    quantity:     int

    model_config = {"from_attributes": True}


class WorkOrderPartsUpdate(BaseModel):

    workorder_id: Optional[int] = Field(None)
    part_id:      Optional[int] = Field(None)
    quantity:     Optional[int] = Field(None)