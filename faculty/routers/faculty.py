from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session

from faculty.routers.database import engine, get_db
from faculty.routers.schemas import (
    Exercise,
    Lecture,
    ListExercises,
    ListLectures,
    ListTeachers,
    Teacher,
)

from . import models

router = APIRouter()

models.Base.metadata.create_all(bind=engine)


@router.get("/teacher/{id}", response_model=Teacher)
async def get_teacher(id: int, db: Session = Depends(get_db)):
    """
    Retrieves a teacher from the database by ID.

    **Parameters**:
    - id: int, the ID of the teacher to retrieve

    **Returns**:
    - Teacher: the teacher object retrieved from the database
    """
    teacher = db.query(models.Teacher).filter(models.Teacher.id == id).first()
    if teacher == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Teacher not found"
        )
    return teacher


@router.get("/teacher/list", response_model=ListTeachers)
async def get_teachers(db: Session = Depends(get_db)):
    all_teachers = db.query(models.Teacher).all()
    return {"teachers": all_teachers}


@router.post(
    "/teacher/create", status_code=status.HTTP_201_CREATED, response_model=Teacher
)
async def create_teacher(teacher_data: Teacher, db: Session = Depends(get_db)):
    new_teacher = models.Teacher(**teacher_data.model_dump())
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return new_teacher


@router.delete("/teacher/delete/{id}")
async def delete_teacher(
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


@router.put("/teacher/update/{id}", response_model=Teacher)
async def update_teacher(id: int, teacher: Teacher, db: Session = Depends(get_db)):
    update_teacher = db.query(models.Teacher).filter(models.Teacher.id == id)
    update_teacher.first()
    if update_teacher == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher with such id not found",
        )
    else:
        update_teacher.update(teacher.model_dump(), synchronize_session=False)
        db.commit()
    return update_teacher.first()


@router.get("/lecture/{id}", response_model=Lecture)
async def get_lecture(id: int, db: Session = Depends(get_db)):
    lecture = db.query(models.Lecture).filter(models.Lecture.id == id).first()
    if lecture == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Lecture not found"
        )
    return lecture


@router.get("/lecture/list", response_model=ListLectures)
async def get_lectures(db: Session = Depends(get_db)):
    all_lectures = db.query(models.Lecture).all()
    return {"lectures": all_lectures}


@router.post(
    "/lecture/create", status_code=status.HTTP_201_CREATED, response_model=Lecture
)
async def create_lecture(lecture: Lecture, db: Session = Depends(get_db)):
    new_lecture = models.Lecture(**lecture.model_dump())
    db.add(new_lecture)
    db.commit()
    db.refresh(new_lecture)

    return new_lecture


@router.delete("/lecture/delete/{id}")
async def delete_lecture(
    id: int, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT
):
    delete_lecture = db.query(models.Lecture).filter(models.Lecture.id == id)
    if delete_lecture == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Lecture with such id not found",
        )
    else:
        delete_lecture.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get("/exercise/{id}", response_model=Exercise)
async def get_exercise(id: int, db: Session = Depends(get_db)):
    exercise = db.query(models.Exercise).filter(models.Exercise.id == id).first()
    if exercise == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Exercise not found"
        )
    return exercise


@router.get("/exercises", response_model=ListExercises)
async def get_exercises(db: Session = Depends(get_db)):
    all_exercises = db.query(models.Exercise).all()
    return {"exercises": all_exercises}


@router.post(
    "/exercise/create", status_code=status.HTTP_201_CREATED, response_model=Exercise
)
async def create_exercise(exercise: Exercise, db: Session = Depends(get_db)):
    new_exercise = models.Exercise(**exercise.model_dump())
    db.add(new_exercise)
    db.commit()
    db.refresh(new_exercise)

    return new_exercise


@router.delete("/exercise/delete/{id}")
async def delete_exercise(
    id: int, db: Session = Depends(get_db), status_code=status.HTTP_204_NO_CONTENT
):
    delete_exercise = db.query(models.Exercise).filter(models.Exercise.id == id)
    if delete_exercise == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Exercise with such id not found",
        )
    else:
        delete_exercise.delete(synchronize_session=False)
        db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
