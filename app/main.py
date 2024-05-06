from fastapi import FastAPI
from app.routers.quiz import router as quiz_router
from app.routers.question import router as question_router
from app.routers.option import router as option_router
from app.routers.profile import router as user_router
from app.routers.auth import router as auth_router

app = FastAPI()


@app.get("/")
async def root():
    return


app.include_router(user_router)
app.include_router(auth_router)
app.include_router(quiz_router)
app.include_router(question_router)
app.include_router(option_router)
