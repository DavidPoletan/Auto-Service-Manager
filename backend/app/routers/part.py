from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlalchemy.orm import Session
from backend.app.database import get_db
from backend.app.schemas.part import Part, PartCreate, PartUpdate
from backend.app.crud.part import (
    get_part,
    get_all_parts,
    create_part,
    update_part,
    delete_part as delete_part_record
)

router = APIRouter()

@router.get("/part/{id}", response_model=Part)
def read_part(id: int, db: Session = Depends(get_db)):
    part = get_part(db, id)

    if part is None:
        raise HTTPException(status_code=404, detail="Part not found")

    return part


@router.get("/", response_model=List[Part])
def read_parts(first_n: Optional[int] = None, db: Session = Depends(get_db)):
    parts = get_all_parts(db)
    return parts[:first_n] if first_n else parts


@router.post("/part/{id}", response_model=Part)
def add_part(part: PartCreate, db: Session = Depends(get_db)):
    return create_part(db, part)


@router.put("/part/{id}", response_model=Part)
def put_part(id: int, part: PartUpdate, db: Session = Depends(get_db)):
    updated_part = update_part(db, id, part)

    if updated_part is None:
        raise HTTPException(status_code=404, detail="Part not found")

    return updated_part


@router.delete("/part/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_part(id: int, db: Session = Depends(get_db)) -> None:
    deleted = delete_part_record(db, id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Part not found")