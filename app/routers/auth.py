from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.models import User
from app.schemas import Token
from app.database import get_db
from services import oauth2
from services.utils import verify

router = APIRouter(tags=['auth'])


@router.post('/login', status_code=200, response_model=Token)
def login(user: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    query = db.query(User).filter(User.user_name == user.username).first()

    if not query:
        raise HTTPException(status_code=409, detail="Invalid User username")

    if not verify(user.password, query.password):
        raise HTTPException(status_code=409, detail="Invalid User password")

    access_token = oauth2.create_access_token(data={'user_id': query.user_id})

    return {
        "access_token": access_token,
        "token_type": "Bearer"
    }
