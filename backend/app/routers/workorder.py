from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.schemas.workorder import WorkOrder, WorkOrderCreate, WorkOrderUpdate
from backend.app.crud.workorder import (
    get_workorder,
    get_all_workorders,
    create_workorder,
    update_workorder,
    delete_workorder as delete_workorder_record
)

router = APIRouter()

@router.get("/workorder/{id}", response_model=WorkOrder)
def read_workorder(id: int, db: Session = Depends(get_db)):
    workorder = get_workorder(db, id)

    if workorder is None:
        raise HTTPException(status_code=404, detail="Work Order not found")

    return workorder


@router.get("/", response_model=List[WorkOrder])
def read_workorders(first_n: Optional[int] = None, db: Session = Depends(get_db)):
    workorders = get_all_workorders(db)
    return workorders[:first_n] if first_n else workorders


@router.post("/workorder/{id}", response_model=WorkOrder)
def add_workorder(workorder: WorkOrderCreate, db: Session = Depends(get_db)):
    return create_workorder(db, workorder)


@router.put("/workorder/{id}", response_model=WorkOrder)
def put_workorder(id: int, workorder: WorkOrderUpdate, db: Session = Depends(get_db)):
    updated_workorder = update_workorder(db, int, workorder)

    if updated_workorder is None:
        raise HTTPException(status_code=404, detail="Work Order not found")

    return updated_workorder


@router.delete("/workorder/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_workorder(id: int, db: Session = Depends(get_db)) -> None:
    deleted = delete_workorder_record(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Work Order not found")