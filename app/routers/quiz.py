from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db
from app.models import Quiz
from app.schemas import QuizOut, QuizIn

router = APIRouter(prefix="/quizzes", tags=["quizzes"])


@router.post("/", status_code=201, response_model=QuizOut)
def quiz_create(quiz: QuizIn, db: Depends = Depends(get_db)):
    query = db.query(Quiz).filter(Quiz.title == quiz.title)
    if query.first() is not None:
        raise HTTPException(status_code=409, detail=f"This quiz \"{quiz.tItle}\" is already exists.")

    quiz = Quiz(**quiz.dict())
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz


@router.get("/{quiz_id}", status_code=status.HTTP_200_OK, response_model=QuizOut)
def delete_quiz(quiz_id: int, db: Session = Depends(get_db)):
    query = db.query(Quiz).filter(Quiz.quiz_id == quiz_id)
    quiz = query.first()

    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz has not found")
    return quiz


@router.put('/{quiz_id}', status_code=201, response_model=QuizOut)
def update_my_quiz(quiz_id: int, quiz_data: QuizIn, db: Depends = Depends(get_db)):
    query = db.query(Quiz).filter(Quiz.quiz_id == quiz_id)
    quiz = query.first()

    if not quiz:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Quiz does not exists!')
    query.update(quiz_data.dict(), synchronize_session=False)

    db.commit()
    return quiz


@router.delete("/{quiz_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_quiz(quiz_id: int, db: Session = Depends(get_db)):
    query = db.query(Quiz).filter(Quiz.quiz_id == quiz_id)
    quiz = query.first()

    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz has not found")
    quiz.delete()
    db.commit()
    return {"message": "Quiz has been deleted"}


@router.get('/all', response_model=list[QuizOut])
def quiz_list(db: Session = Depends(get_db)):
    quiz_list = db.query(Quiz).all()
    return quiz_list
