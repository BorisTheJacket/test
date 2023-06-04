from sqlalchemy import Column, Integer, String, Date
from config import Base


class QuizQuestion(Base):
    __tablename__ = 'Quiz questions'

    id=Column(Integer, primary_key=True)
    question_id=Column(Integer)
    question_description=Column(String)
    answer_description=Column(String)
    created_at=Column(Date)