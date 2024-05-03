from fastapi import FastAPI
from app.routers.question import router as question_router
from app.routers.option import router as option_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(question_router)
app.include_router(option_router)
