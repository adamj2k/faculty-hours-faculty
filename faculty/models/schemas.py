from typing import List

from pydantic import BaseModel, EmailStr, Field, computed_field


class Teacher(BaseModel):
    id: int
    name: str
    last_name: str
    email: EmailStr


class ListTeachers(BaseModel):
    teachers: List[Teacher]


class TeacherResponse(BaseModel):
    teacher: Teacher


class Lecture(BaseModel):
    id: int
    name: str
    study_year: int = Field(ge=1, le=5)
    semester: int = Field(ge=1, le=2)
    hours_lectures: int
    groups_lectures: int
    teacher_id: int

    @computed_field
    def sum_lectures_hours(self) -> int:
        return self.hours_lectures * self.groups_lectures


class ListLectures(BaseModel):
    lectures: list[Lecture]


class LectureResponse(BaseModel):
    lecture: Lecture


class Exercise(BaseModel):
    id: int
    name: str
    study_year: int = Field(ge=1, le=5)
    semester: int = Field(ge=1, le=2)
    hours_exercises: int
    groups_exercises: int
    teacher_id: int

    @computed_field
    def sum_exercises_hours(self) -> int:
        return self.hours_exercises * self.groups_exercises


class ListExercises(BaseModel):
    exercises: list[Exercise]


class ExerciseResponse(BaseModel):
    exercise: Exercise
