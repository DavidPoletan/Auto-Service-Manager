from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class Car(BaseModel):

    id:                  int =      Field(...,  description="Unique identifier of the car (Used in database, not to be confused with VIN)")
    customer_id:         int =      Field(...,  description="Number which corresponds with the identifier of the customer who owns the car")
    brand:               str =      Field(...,  max_length=50,    description="Brand of the car")
    model:               str =      Field(...,  max_length=50,    description="Model of the car")
    year:                int =      Field(...,  ge=1900, le=2027, description="Car's year of manufacturing")
    vin:                 str =      Field(None, max_length=17,    description="Unique vehicle identification number of the car given by the manufacturer")
    registration_number: str =      Field(None, max_length=20,    description="Unique registration number of the car given by the government")
    color:               str =      Field(None, max_length=30,    description="Color of the car's body")
    mileage:             int =      Field(None, description="Total distance the car has driven for a given point in time")
    fuel_type:           str =      Field(None, max_length=20, description="Type of fuel that the car's engine runs on")
    transmission:        str =      Field(None, max_length=20, description="Type of transmission that's used in the car")
    created_at:          datetime = Field(...,  description="Date and time on which the car's entry was created")
    updated_at:          datetime = Field(None, description="Date and time on which the car's entry was updated")


class CarCreate(BaseModel):

    id:                  int = Field(...,  description="Unique identifier of the car (Used in database, not to be confused with VIN)")
    customer_id:         int = Field(...,  description="Number which corresponds with the identifier of the customer who owns the car")
    brand:               str = Field(...,  max_length=50,    description="Brand of the car")
    model:               str = Field(...,  max_length=50,    description="Model of the car")
    year:                int = Field(...,  ge=1900, le=2027, description="Car's year of manufacturing")
    vin:                 str = Field(None, max_length=17,    description="Unique vehicle identification number of the car given by the manufacturer")
    registration_number: str = Field(None, max_length=20,    description="Unique registration number of the car given by the government")
    color:               str = Field(None, max_length=30,    description="Color of the car's body")
    mileage:             int = Field(None, description="Total distance the car has driven for a given point in time")
    fuel_type:           str = Field(None, max_length=20, description="Type of fuel that the car's engine runs on")
    transmission:        str = Field(None, max_length=20, description="Type of transmission that's used in the car")


class CarResponse(BaseModel):

    id:                  int =      Field(...,  description="Unique identifier of the car (Used in database, not to be confused with VIN)")
    customer_id:         int =      Field(...,  description="Number which corresponds with the identifier of the customer who owns the car")
    brand:               str =      Field(...,  max_length=50,    description="Brand of the car")
    model:               str =      Field(...,  max_length=50,    description="Model of the car")
    year:                int =      Field(...,  ge=1900, le=2027, description="Car's year of manufacturing")
    vin:                 str =      Field(None, max_length=17,    description="Unique vehicle identification number of the car given by the manufacturer")
    registration_number: str =      Field(None, max_length=20,    description="Unique registration number of the car given by the government")
    color:               str =      Field(None, max_length=30,    description="Color of the car's body")
    mileage:             int =      Field(None, description="Total distance the car has driven for a given point in time")
    fuel_type:           str =      Field(None, max_length=20, description="Type of fuel that the car's engine runs on")
    transmission:        str =      Field(None, max_length=20, description="Type of transmission that's used in the car")
    created_at:          datetime = Field(...,  description="Date and time on which the car's entry was created")
    updated_at:          datetime = Field(None, description="Date and time on which the car's entry was updated")

    model_config = {"from_attributes": True}


class CarUpdate(BaseModel):

    brand:               Optional[str] =      Field(None, max_length=50,    description="Brand of the car")
    model:               Optional[str] =      Field(None, max_length=50,    description="Model of the car")
    year:                Optional[int] =      Field(None, ge=1900, le=2027, description="Car's year of manufacturing")
    vin:                 Optional[str] =      Field(None, max_length=17,    description="Unique vehicle identification number of the car given by the manufacturer")
    registration_number: Optional[str] =      Field(None, max_length=20,    description="Unique registration number of the car given by the government")
    color:               Optional[str] =      Field(None, max_length=30,    description="Color of the car's body")
    mileage:             Optional[int] =      Field(None, description="Total distance the car has driven for a given point in time")
    fuel_type:           Optional[str] =      Field(None, max_length=20, description="Type of fuel that the car's engine runs on")
    transmission:        Optional[str] =      Field(None, max_length=20, description="Type of transmission that's used in the car")
    updated_at:          Optional[datetime] = Field(None, description="Date and time on which the car's entry was updated")