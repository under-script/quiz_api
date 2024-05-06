from fastapi import APIRouter, Depends, HTTPException

from app.models import User
from app.database import get_db
from app.schemas import UserOut, UserIn
from services.oauth2 import get_current_user
from services.utils import password_hash
from starlette import status

router = APIRouter(prefix="/profile", tags=["profile"])


@router.post("/", status_code=201, response_model=UserOut)
def user_sign_up(user: UserIn, db: Depends = Depends(get_db)):
    query = db.query(User).filter(User.user_name == user.user_name)
    if query.first() is not None:
        raise HTTPException(status_code=409, detail=f"This {user.user_name} is already registered.")

    user.password = password_hash(user.password)
    user = User(**user.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.get('/', response_model=UserOut)
def get_me(user: UserOut = Depends(get_current_user)):
    return user


@router.put('/', status_code=status.HTTP_202_ACCEPTED, response_model=UserOut)
def update_my_profile(user_name: str, user: UserOut = Depends(get_current_user), db: Depends = Depends(get_db)):
    user.user_name = user_name

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.delete('/', status_code=status.HTTP_202_ACCEPTED)
def delete_my_profile(user: UserOut = Depends(get_current_user), db: Depends = Depends(get_db)):
    user.delete()
    db.commit()
    return {
        "Your profile has been deleted"
    }
