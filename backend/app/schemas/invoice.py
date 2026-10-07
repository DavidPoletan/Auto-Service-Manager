from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

class Invoice(BaseModel):

    id:             int =      Field(...,   description="Unique identifier of the invoice")
    workorder_id:   int =      Field(...,   description="Number corresponding to the invoice's work order identifier")
    issue_date:     datetime = Field(...,   description="Date and time on which the invoice was issued")
    total_price:    Decimal =  Field(gt=0,  decimal_places=2, description="Combined price of mechanic's labor and all parts that were used")
    payment_status: str =      Field(...,   max_length=20,    description="Status which represents whether the customer has paid the invoice or not")
    payment_method: str =      Field(None,  max_length=20,    description="Which method the customer used to pay the invoice")
    created_at:     datetime = Field(...,   description="Date and time on which the invoice's entry was created")


class InvoiceCreate(BaseModel):

    id:             int =      Field(...,   description="Unique identifier of the invoice")
    workorder_id:   int =      Field(...,   description="Number corresponding to the invoice's work order identifier")
    issue_date:     datetime = Field(...,   description="Date and time on which the invoice was issued")
    total_price:    Decimal =  Field(gt=0,  decimal_places=2, description="Combined price of mechanic's labor and all parts that were used")
    payment_status: str =      Field(...,   max_length=20,    description="Status which represents whether the customer has paid the invoice or not")
    payment_method: str =      Field(None,  max_length=20,    description="Which method the customer used to pay the invoice")


class InvoiceResponse():

    id:             int =      Field(...,   description="Unique identifier of the invoice")
    workorder_id:   int =      Field(...,   description="Number corresponding to the invoice's work order identifier")
    issue_date:     datetime = Field(...,   description="Date and time on which the invoice was issued")
    total_price:    Decimal =  Field(gt=0,  decimal_places=2, description="Combined price of mechanic's labor and all parts that were used")
    payment_status: str =      Field(...,   max_length=20,    description="Status which represents whether the customer has paid the invoice or not")
    payment_method: str =      Field(None,  max_length=20,    description="Which method the customer used to pay the invoice")
    created_at:     datetime = Field(...,   description="Date and time on which the invoice's entry was created")

    model_config = {"from_attributes": True}