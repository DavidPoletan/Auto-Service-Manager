from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

class WorkOrder(BaseModel):

    id:                  int =      Field(...,  description="Unique identifier of the work order")
    appointment_id:      int =      Field(...,  description="Number which corresponds with the identifier of the work order's appointment")
    mechanic_id:         int =      Field(None, description="Number which corresponds with the identifier of the mechanic (user) who took the work order")
    problem_description: str =      Field(...,  description="Description of the problem that was given by the customer")
    labor_cost:          Decimal =  Field(gt=0, decimal_places=2, description="Cost of the labor that the mechanic has performed")
    status:              str =      Field(...,  max_length=20,    description="Current status of the work order")
    odometer:            int =      Field(None, description="Distance the car has driven by the time of the appointment")
    diagnosis:           str =      Field(None, description="Description of the diagnosis given by the mechanic")
    work_performed:      str =      Field(None, description="Description of the work that the mechanic has performed")
    recommendations:     str =      Field(None, description="Recommendations for the work that should be done in the future")
    opened_at:           datetime = Field(...,  description="Date and time on which the work order was opened")
    completed_at:        datetime = Field(None, description="Date and time on which the work order was completed")
    created_at:          datetime = Field(...,  description="Date and time on which the work order was created")
    updated_at:          datetime = Field(None, description="Date and time on which the work order was updated")


class WorkOrderCreate(BaseModel):

    id:                  int =      Field(...,  description="Unique identifier of the work order")
    appointment_id:      int =      Field(...,  description="Number which corresponds with the identifier of the work order's appointment")
    mechanic_id:         int =      Field(None, description="Number which corresponds with the identifier of the mechanic (user) who took the work order")
    problem_description: str =      Field(...,  description="Description of the problem that was given by the customer")
    labor_cost:          Decimal =  Field(gt=0, decimal_places=2, description="Cost of the labor that the mechanic has performed")
    status:              str =      Field(...,  max_length=20,    description="Current status of the work order")
    odometer:            int =      Field(None, description="Distance the car has driven by the time of the appointment")
    diagnosis:           str =      Field(None, description="Description of the diagnosis given by the mechanic")
    work_performed:      str =      Field(None, description="Description of the work that the mechanic has performed")
    recommendations:     str =      Field(None, description="Recommendations for the work that should be done in the future")
    opened_at:           datetime = Field(...,  description="Date and time on which the work order was opened")
    completed_at:        datetime = Field(None, description="Date and time on which the work order was completed")


class WorkOrderResponse(BaseModel):

    id:                  int =      Field(...,  description="Unique identifier of the work order")
    appointment_id:      int =      Field(...,  description="Number which corresponds with the identifier of the work order's appointment")
    mechanic_id:         int =      Field(None, description="Number which corresponds with the identifier of the mechanic (user) who took the work order")
    problem_description: str =      Field(...,  description="Description of the problem that was given by the customer")
    labor_cost:          Decimal =  Field(gt=0, decimal_places=2, description="Cost of the labor that the mechanic has performed")
    status:              str =      Field(...,  max_length=20,    description="Current status of the work order")
    odometer:            int =      Field(None, description="Distance the car has driven by the time of the appointment")
    diagnosis:           str =      Field(None, description="Description of the diagnosis given by the mechanic")
    work_performed:      str =      Field(None, description="Description of the work that the mechanic has performed")
    recommendations:     str =      Field(None, description="Recommendations for the work that should be done in the future")
    opened_at:           datetime = Field(...,  description="Date and time on which the work order was opened")
    completed_at:        datetime = Field(None, description="Date and time on which the work order was completed")
    created_at:          datetime = Field(...,  description="Date and time on which the work order's entry was created")
    updated_at:          datetime = Field(None, description="Date and time on which the work order was updated")

    model_config = {"from_attributes": True}


class WorkOrderUpdate(BaseModel):

    mechanic_id:         Optional[int] =      Field(None, description="Number which corresponds with the identifier of the mechanic (user) who took the work order")
    problem_description: Optional[str] =      Field(None,  description="Description of the problem that was given by the customer")
    labor_cost:          Optional[Decimal] =  Field(gt=0, decimal_places=2, description="Cost of the labor that the mechanic has performed")
    status:              Optional[str] =      Field(None,  max_length=20,    description="Current status of the work order")
    odometer:            Optional[int] =      Field(None, description="Distance the car has driven by the time of the appointment")
    diagnosis:           Optional[str] =      Field(None, description="Description of the diagnosis given by the mechanic")
    work_performed:      Optional[str] =      Field(None, description="Description of the work that the mechanic has performed")
    recommendations:     Optional[str] =      Field(None, description="Recommendations for the work that should be done in the future")
    opened_at:           Optional[datetime] = Field(None,  description="Date and time on which the work order was opened")
    completed_at:        Optional[datetime] = Field(None, description="Date and time on which the work order was completed")
    updated_at:          Optional[datetime] = Field(None, description="Date and time on which the work order was updated")