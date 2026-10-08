from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from enum import Enum

class Status(Enum):

    Unpaid =         'UNPAID'
    Paid =           'PAID'
    Partially_Paid = 'PARTIALLY_PAID'


class Method(Enum):

    Cash =          'CASH'
    Card =          'CARD'
    Bank_Transfer = 'BANK_TRANSFER'


class Invoice(BaseModel):

    id:             int =      Field(...,   description="Unique identifier of the invoice")
    workorder_id:   int =      Field(...,   description="Number corresponding to the invoice's work order identifier")
    issue_date:     datetime = Field(...,   description="Date and time on which the invoice was issued")
    total_price:    Decimal =  Field(gt=0,  decimal_places=2, description="Combined price of mechanic's labor and all parts that were used")
    payment_status: Status =   Field(default=Status.Unpaid,   description="Status which represents whether the customer has paid the invoice or not")
    payment_method: Method =   Field(default=Method.Cash,     description="Which method the customer used to pay the invoice")
    created_at:     datetime = Field(...,   description="Date and time on which the invoice's entry was created")


class InvoiceCreate(BaseModel):

    id:             int =      Field(...,   description="Unique identifier of the invoice")
    workorder_id:   int =      Field(...,   description="Number corresponding to the invoice's work order identifier")
    issue_date:     datetime = Field(...,   description="Date and time on which the invoice was issued")
    total_price:    Decimal =  Field(gt=0,  decimal_places=2, description="Combined price of mechanic's labor and all parts that were used")
    payment_status: Status =   Field(default=Status.Unpaid,   description="Status which represents whether the customer has paid the invoice or not")
    payment_method: Method =   Field(default=Method.Cash,     description="Which method the customer used to pay the invoice")


class InvoiceResponse():

    id:             int =      Field(...,   description="Unique identifier of the invoice")
    workorder_id:   int =      Field(...,   description="Number corresponding to the invoice's work order identifier")
    issue_date:     datetime = Field(...,   description="Date and time on which the invoice was issued")
    total_price:    Decimal =  Field(gt=0,  decimal_places=2, description="Combined price of mechanic's labor and all parts that were used")
    payment_status: Status =   Field(default=Status.Unpaid,   description="Status which represents whether the customer has paid the invoice or not")
    payment_method: Method =   Field(default=Method.Cash,     description="Which method the customer used to pay the invoice")
    created_at:     datetime = Field(...,   description="Date and time on which the invoice's entry was created")

    model_config = {"from_attributes": True}