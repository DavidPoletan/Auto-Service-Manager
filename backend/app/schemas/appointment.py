from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from enum import Enum

class Status(Enum):

    Scheduled =   'SCHEDULED'
    In_Progress = 'IN_PROGRESS'
    Completed =   'COMPLETED'
    Cancelled =   'CANCELLED'


class Appointment(BaseModel):

    id:               int =      Field(...,  description="Unique identifier of the appointment")
    car_id:           int =      Field(...,  description="Number corresponding to the identifier of the car that will be brought for the appointment")
    appointment_date: datetime = Field(...,  description="Date and time on which the appointment will take place")
    status:           Status =   Field(default=Status.Scheduled, description="Current status of the appointment")
    notes:            str =      Field(None, description="Information that could be of use")
    created_at:       datetime = Field(...,  description="Date and time on which the appointment was created")
    updated_at:       datetime = Field(None, description="Date and time on which the appointment was updated")


class AppointmentCreate(BaseModel):

    id:               int =      Field(..., description="Unique identifier of the appointment")
    car_id:           int =      Field(..., description="Number corresponding to the identifier of the car that will be brought for the appointment")
    appointment_date: datetime = Field(..., description="Date and time on which the appointment will take place")
    status:           Status =   Field(default=Status.Scheduled, description="Current status of the appointment")
    notes:            str =      Field(None, description="Information that could be of use")


class AppointmentResponse(BaseModel):

    id:               int =      Field(..., description="Unique identifier of the appointment")
    car_id:           int =      Field(..., description="Number corresponding to the identifier of the car that will be brought for the appointment")
    appointment_date: datetime = Field(..., description="Date and time on which the appointment will take place")
    status:           Status =   Field(default=Status.Scheduled, description="Current status of the appointment")
    notes:            str =      Field(None, description="Information that could be of use")
    created_at:       datetime = Field(...,  description="Date and time on which the appointment was created")
    updated_at:       datetime = Field(None, description="Date and time on which the appointment was updated")

    model_config = {"from_attributes": True}


class AppointmentUpdate(BaseModel):

    car_id:           Optional[int] =      Field(None, description="Number corresponding to the identifier of the car that will be brought for the appointment")
    appointment_date: Optional[datetime] = Field(None, description="Date and time on which the appointment will take place")
    status:           Optional[Status] =   Field(None, description="Current status of the appointment")
    notes:            Optional[str] =      Field(None, description="Information that could be of use")
    updated_at:       Optional[datetime] = Field(None, description="Date and time on which the appointment was updated")