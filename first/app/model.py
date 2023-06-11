from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

table_name = 'quiz_questions'

class QuizQuestion(Base):
    __tablename__ = table_name
    
    id=Column(Integer, primary_key=True)
    question_description=Column(String)
    answer_description=Column(String)
    created_at=Column(Date)


    def __repr__(self):
        return str(self.id)


    
