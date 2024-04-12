from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from . import models
from .database import engine, get_db
from .schemas import Teacher, Teachers

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


@router.get("/teachers", response_model=Teachers)
def teachers_list(db: Session = Depends(get_db)):
    all_teachers = jsonable_encoder(db.query(models.Teacher).all())
    return JSONResponse({"teachers": all_teachers})


@router.post("/create-teacher")
def create_teacher(teacher: Teacher, db: Session = Depends(get_db)):
    new_teacher = models.Teacher(**teacher.model_dump())
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return new_teacher


@router.delete("/delete-teacher/{id}")
def delete_teacher(
    id: int, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT
):
    delete_teacher = db.query(models.Teacher).filter(models.Teacher.id == id)
    if delete_teacher == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher with such id not found",
        )
    else:
        delete_teacher.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
