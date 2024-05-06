from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean

from app.database import Base, engine


class Meta:
    added_date = Column(DateTime, default=datetime.utcnow)


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    is_super_user = Column(Boolean, default=False)
    user_name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    date_joined = Column(DateTime, default=datetime.utcnow)


class Quiz(Base, Meta):
    __tablename__ = 'quizzes'
    quiz_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)


class Question(Base, Meta):
    __tablename__ = 'questions'
    question_id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quizs.quiz_id'))
    title = Column(String, unique=True, nullable=False)


class Option(Base, Meta):
    __tablename__ = 'options'
    option_id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.question_id'))
    title = Column(String, unique=True, nullable=False)
    is_correct = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
