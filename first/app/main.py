from fastapi import FastAPI, status, exceptions
from repository import QuestionsRepository
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from crud import QuizService


DATABASE_URL = "postgresql://admin:root@db:5432/admin"


engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
repository = QuestionsRepository(SessionLocal)
quiz_service = QuizService(repository)


app = FastAPI(
    title="Quiz quetsions request"
)


@app.post("/questions-{question_num}", status_code=status.HTTP_201_CREATED)
def post_number(question_num: int):
    if question_num > 100:
        raise exceptions.HTTPException(status_code=400)
    return quiz_service.get_questions(question_num)
      
