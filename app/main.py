# -- Active: 1685786933474@@127.0.0.1@5432@admin
from fastapi import FastAPI
from repository import QuestionsRepository
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Date, inspect
from sqlalchemy.orm import sessionmaker, scoped_session
from crud import QuizService
from model import table_name


DATABASE_URL = "postgresql://admin:root@localhost:5432/postgres"


engine = create_engine(DATABASE_URL)
SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
repository = QuestionsRepository(SessionLocal)

# if not inspect(engine).has_table(table_name):
#     metadata = MetaData(engine)
#     Table(table_name, metadata,
#           Column('Id', Integer, primary_key=True), Column('Question_description', String), Column('Answer_description', String), Column('Created_at', Date))
    
#     metadata.create_all(bind=engine)


app = FastAPI(
    title="Quiz quetsions request"
)


@app.post("/questions-{question_num}")
def post_number(question_num):
    return QuizService(repository).get_questions(question_num)
