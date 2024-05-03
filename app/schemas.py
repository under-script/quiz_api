from datetime import datetime

from pydantic import BaseModel


class QuestionCreate(BaseModel):
    tItle: str


class QuestionOutput(QuestionCreate):
    question_id: int
    added_date: datetime


class OptionCreate(BaseModel):
    question_id: int
    tItle: str
    is_correct: bool


class OptionOutput(OptionCreate):
    added_date: datetime
