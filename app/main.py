import uvicorn
from fastapi import FastAPI
from sqladmin import Admin, ModelView

from app.database import engine
from app.models import User, Quiz, Question, Option
from app.routers.auth import router as auth_router
from app.routers.option import router as option_router
from app.routers.profile import router as user_router
from app.routers.question import router as question_router
from app.routers.quiz import router as quiz_router

app = FastAPI()


@app.get("/")
async def root():
    return


app.include_router(user_router)
app.include_router(auth_router)
app.include_router(quiz_router)
app.include_router(question_router)
app.include_router(option_router)

admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [
        User.user_id,
        User.is_super_user,
        User.user_name,
        User.password,
        User.date_joined
    ]


class QuizAdmin(ModelView, model=Quiz):
    column_list = [
        Quiz.quiz_id,
        Quiz.title,
        Quiz.added_date,
    ]


class QuestionAdmin(ModelView, model=Question):
    column_list = [
        Question.question_id,
        Question.quiz_id,
        Question.title,
        Question.added_date,
    ]


class OptionAdmin(ModelView, model=Option):
    column_list = [
        Option.option_id,
        Option.question_id,
        Option.title,
        Option.is_correct_answer,
        Option.added_date,
    ]


admin.add_view(UserAdmin)
admin.add_view(QuizAdmin)
admin.add_view(QuestionAdmin)
admin.add_view(OptionAdmin)

if __name__ == '__main__':
    uvicorn.run(app=app, host="127.0.0.1", port=8000, reload=True, workers=3)
