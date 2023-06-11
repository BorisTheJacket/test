from sqlalchemy.orm import Session
from model import QuizQuestion


class QuestionsRepository():
    
    def __init__(self, db:Session):
        self.db = db


    def create_question(self, question: QuizQuestion):
        self.db.add(question)
        self.db.commit()
        self.db.refresh(question)
        return question
    

    def question_exists(self, question: QuizQuestion):
        return self.db.query(QuizQuestion).get(question.id) != None 
    

    