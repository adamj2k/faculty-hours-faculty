from sqlalchemy import ForeignKey  # noqa
from sqlalchemy import TIMESTAMP, Column, Computed, Integer, String, text

from .database import Base


class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
    last_name = Column(String)
    email = Column(String)
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class Lecture(Base):
    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100))
    study_year = Column(Integer)
    semester = Column(Integer)
    hours_lectures = Column(Integer, server_default="30")
    groups_lectures = Column(Integer, server_default="1", nullable=True)
    sum_lectures_hours = Column(Integer, Computed("hours_lectures * groups_lectures"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100))
    study_year = Column(Integer)
    semester = Column(Integer)
    hours_exercises = Column(Integer, server_default="30")
    groups_exercises = Column(Integer, server_default="1", nullable=True)
    sum_exercises_hours = Column(
        Integer, Computed("hours_exercises * groups_exercises")
    )
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
