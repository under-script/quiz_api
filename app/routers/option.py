from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db
from app.models import Option, Question
from app.schemas import OptionOut, OptionIn

router = APIRouter(prefix="/options", tags=["options"])


@router.post("/", status_code=201, response_model=OptionOut)
def option_create(option: OptionIn, db: Depends = Depends(get_db)):
    query = db.query(Option).filter(Option.title == option.title)
    if query.first() is not None:
        raise HTTPException(status_code=409, detail=f"This option \"{option.tItle}\" is already exists.")

    query = db.query(Question).filter(Question.question_id == option.question_id)
    question = query.first()

    if not question:
        raise HTTPException(status_code=404, detail="Question has not found")

    option = Option(**option.dict())
    db.add(option)
    db.commit()
    db.refresh(option)
    return option


@router.get("/{option_id}", status_code=status.HTTP_200_OK, response_model=OptionOut)
def delete_option(option_id: int, db: Session = Depends(get_db)):
    query = db.query(Option).filter(Option.option_id == option_id)
    option = query.first()

    if not option:
        raise HTTPException(status_code=404, detail="Option has not found")
    return option


@router.put('/{option_id}', status_code=201, response_model=OptionOut)
def update_my_option(option_id: int, option_data: OptionIn, db: Depends = Depends(get_db)):
    query = db.query(Option).filter(Option.option_id == option_id)
    option = query.first()

    if not option:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Option does not exists!')
    query.update(option_data.dict(), synchronize_session=False)

    db.commit()
    return option


@router.delete("/{option_id}", status_code=status.HTTP_202_ACCEPTED)
def delete_option(option_id: int, db: Session = Depends(get_db)):
    query = db.query(Option).filter(Option.option_id == option_id)
    option = query.first()

    if not option:
        raise HTTPException(status_code=404, detail="Option has not found")
    option.delete()
    db.commit()
    return {"message": "Option has been deleted"}


@router.get('/all', response_model=list[OptionOut])
def option_list(db: Session = Depends(get_db)):
    option_list = db.query(Option).all()
    return option_list
