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


class Master(BaseModel):
    title: str
    added_date: datetime


class QuizIn(BaseModel):
    title: str


class QuizOut(Master):
    quiz_id: int


class QuestionIn(Master):
    quiz_id: int
    title: str


class QuestionOut(Master):
    question_id: int


class OptionIn(Master):
    question_id: int
    is_correct_answer: bool


class OptionOut(OptionIn):
    option_id: int


class Token(BaseModel):
    access_token: str
    token_type: str
