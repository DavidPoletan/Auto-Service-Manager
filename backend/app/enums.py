from enum import Enum

class UserRole(str, Enum):

    Admin =        'ADMIN'
    Receptionist = 'RECEPTIONIST'
    Mechanic =     'MECHANIC'


class InvoiceStatus(str, Enum):

    Unpaid =         'UNPAID'
    Paid =           'PAID'
    Partially_Paid = 'PARTIALLY_PAID'


class InvoiceMethod(str, Enum):

    Cash =          'CASH'
    Card =          'CARD'
    Bank_Transfer = 'BANK_TRANSFER'


class AppointmentStatus(str, Enum):

    Scheduled =   'SCHEDULED'
    In_Progress = 'IN_PROGRESS'
    Completed =   'COMPLETED'
    Cancelled =   'CANCELLED'


class WorkOrderStatus(str, Enum):

    Open =        'OPEN'
    In_Progress = 'IN_PROGRESS'
    Completed =   'COMPLETED'