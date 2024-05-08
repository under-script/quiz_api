from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean

from app.database import Base, engine


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    is_super_user = Column(Boolean, default=False)
    user_name = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    date_joined = Column(DateTime, default=datetime.utcnow)


class Quiz(Base):
    __tablename__ = 'quizzes'
    quiz_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    added_date = Column(DateTime, default=datetime.utcnow)


class Question(Base):
    __tablename__ = 'questions'
    question_id = Column(Integer, primary_key=True)
    quiz_id = Column(Integer, ForeignKey('quizzes.quiz_id'))
    title = Column(String, unique=True, nullable=False)
    added_date = Column(DateTime, default=datetime.utcnow)


class Option(Base):
    __tablename__ = 'options'
    option_id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey('questions.question_id'))
    title = Column(String, unique=True, nullable=False)
    is_correct_answer = Column(Boolean, default=False)
    added_date = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(bind=engine)
