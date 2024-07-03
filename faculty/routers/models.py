from sqlalchemy import ForeignKey  # noqa
from sqlalchemy import TIMESTAMP, Column, Integer, String, Table, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from faculty.routers.database import Base

Base = declarative_base()

association_table_exercise_teacher = Table(
    "association_exercise_teacher",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teachers.id")),
    Column("exercise_id", Integer, ForeignKey("exercises.id")),
)

Base = declarative_base()

association_table_exercise_teacher = Table(
    "association_exercise_teacher",
    Base.metadata,
    Column("teacher_id", Integer, ForeignKey("teachers.id")),
    Column("exercise_id", Integer, ForeignKey("exercises.id")),
)


class Teacher(Base):
    """
    Class Teacher representing a teacher with:
    - id, name, last_name and email.
    """

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
    exercise = relationship(
        "Exercise",
        secondary=association_table_exercise_teacher,
        back_populates="teacher",
    )


class Lecture(Base):
    """
    Class Lecture representing a lecture with his name, number of hours,
    groups and study year. Has relation with class Teacher.
    """

    __tablename__ = "lectures"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100))
    study_year = Column(Integer)
    semester = Column(Integer)
    hours_lectures = Column(Integer, server_default="30")
    groups_lectures = Column(Integer, server_default="1", nullable=True)
    sum_lectures_hours = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )


class Exercise(Base):
    """
    Class Exercises representing an exercise with his name, number of hours,
    number of groups and calculation sum of hours of all groups.
    Has many to many relation with class Teacher.
    """

    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(100))
    study_year = Column(Integer)
    semester = Column(Integer)
    hours_exercises = Column(Integer, server_default="30")
    groups_exercises = Column(Integer, server_default="1", nullable=True)
    sum_exercises_hours = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    created_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    updated_at = Column(
        TIMESTAMP(timezone=True), nullable=False, server_default=text("now()")
    )
    teacher = relationship(
        "Teacher",
        secondary=association_table_exercise_teacher,
        back_populates="exercise",
    )
