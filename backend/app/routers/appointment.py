from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.schemas.appointment import Appointment, AppointmentCreate, AppointmentUpdate
from backend.app.crud.appointment import (
    get_appointment,
    get_all_appointments,
    create_appointment,
    update_appointment,
    delete_appointment as delete_appointment_record
)

router = APIRouter()

@router.get("/appointment/{id}", response_model=Appointment)
def read_appointment(id: int, db: Session = Depends(get_db)):
    appointment = get_appointment(db, id)

    if appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")

    return appointment


@router.get("/", response_model=List[Appointment])
def read_appointments(first_n: Optional[int] = None, db: Session = Depends(get_db)):
    appointments = get_all_appointments(db)
    return appointments[:first_n] if first_n else appointments


@router.post("/car/{id}", response_model=Appointment)
def add_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    return create_appointment(db, appointment)


@router.put("/appointment/{id}", response_model=Appointment)
def put_appointment(id: int, appointment: AppointmentUpdate, db: Session = Depends(get_db)):
    updated_appointment = update_appointment(db, id, appointment)

    if updated_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")


@router.delete("/car/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_appointment(id: int, db: Session = Depends(get_db)) -> None:
    deleted = delete_appointment_record(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Appointment not found")