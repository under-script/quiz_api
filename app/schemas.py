from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    user_name: str


class UserIn(User):
    password: str


class UserOut(User):
    user_id: int
    is_super_user: bool
    date_joined: datetime


class QuizIn(BaseModel):
    title: str


class QuizOut(QuizIn):
    quiz_id: int
    added_date: datetime


class QuestionIn(BaseModel):
    quiz_id: int
    title: str


class QuestionOut(QuestionIn):
    added_date: datetime


class OptionIn(BaseModel):
    question_id: int
    title: str
    is_correct_answer: bool


class OptionOut(OptionIn):
    option_id: int
    added_date: datetime


class Token(BaseModel):
    access_token: str
    token_type: str


class ResultIn(BaseModel):
    question_id: int
    option_id: int


class ResultOut(BaseModel):
    results: list[ResultIn]
