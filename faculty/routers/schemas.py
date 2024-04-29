from pydantic import BaseModel, EmailStr, Field, computed_field


class Teacher(BaseModel):
    id: int
    name: str
    last_name: str
    email: EmailStr


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


class Teachers(Teacher):
    teachers: list[Teacher]


class Lectures(Lecture):
    lectures: list[Lecture]


class Exercises(Exercise):
    exercises: list[Exercise]
