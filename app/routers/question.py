from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db
from app.models import Question
from app.schemas import QuestionIn, QuestionOut

router = APIRouter(prefix="/questions", tags=["questions"])


@router.post("/", status_code=201, response_model=QuestionOut)
def question_create(question: QuestionIn, db: Depends = Depends(get_db)):
    query = db.query(Question).filter(Question.title == question.title)
    if query.first() is not None:
        raise HTTPException(status_code=409, detail=f"This question \"{question.tItle}\" is already exists.")

    question = Question(**question.dict())
    db.add(question)
    db.commit()
    db.refresh(question)
    return question


@router.get("/{question_id}", status_code=status.HTTP_200_OK, response_model=QuestionOut)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    query = db.query(Question).filter(Question.question_id == question_id)
    question = query.first()

    if not question:
        raise HTTPException(status_code=404, detail="Question has not found")
    return question


@router.put('/{question_id}', status_code=201, response_model=QuestionOut)
def update_my_question(question_id: int, question_data: QuestionIn, db: Depends = Depends(get_db)):
    query = db.query(Question).filter(Question.question_id == question_id)
    question = query.first()

    if not question:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Question does not exists!')
    query.update(question_data.dict(), synchronize_session=False)

    db.commit()
    return question


@router.delete("/{question_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    query = db.query(Question).filter(Question.question_id == question_id)
    question = query.first()

    if not question:
        raise HTTPException(status_code=404, detail="Question has not found")
    question.delete()
    db.commit()
    return {"message": "Question has been deleted"}


@router.get('/all', response_model=list[QuestionOut])
def question_list(db: Session = Depends(get_db)):
    question_list = db.query(Question).all()
    return question_list
