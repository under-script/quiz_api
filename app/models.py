from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean

from app.database import Base


class Question(Base):
    __tablename__ = 'questions'
    question_id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, unique=True, nullable=False)
    added_date = Column(DateTime, default=datetime.utcnow)


class Option(Base):
    __tablename__ = 'options'
    option_id = Column(Integer, primary_key=True, nullable=False)
    question_id = Column(Integer, ForeignKey('question.question_id'), nullable=False)
    title = Column(String, unique=True, nullable=False)
    is_correct = Column(Boolean, default=False)
    added_date = Column(DateTime, default=datetime.utcnow)
