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


class Title(BaseModel):
    title: str


class Date(BaseModel):
    added_date: datetime


class Master(Title, Date):
    pass


class QuizIn(Title):
    pass


class QuizOut(Master):
    quiz_id: int


class QuestionIn(Title):
    quiz_id: int


class QuestionOut(QuestionIn, Date):
    question_id: int


class OptionIn(Title):
    question_id: int
    is_correct_answer: bool


class OptionOut(OptionIn, Date):
    option_id: int


class Token(BaseModel):
    access_token: str
    token_type: str
