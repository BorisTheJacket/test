from sqlalchemy.orm import Session
from model import QuizQuestion
# from schemas import QuizSchema


class QuestionsRepository():
    # Repository responsibility
    def __init__(self, db:Session):
        self.db = db


    def get_questions(self, question_num:int):
        return self.db.query(QuizQuestion).all()


    def create_question(self, question: QuizQuestion):
        self.db.add(question)
        self.db.commit()
        self.db.refresh(question)
        return question