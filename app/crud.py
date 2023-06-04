from sqlalchemy.orm import Session
from model import QuizQuestion
from schemas import QuizSchema


def get_questions(db:Session, question_num:int):
    return db.query(QuizQuestion).all()


def create_questions(db:Session, question: QuizQuestion):
    _question = QuizQuestion(
        question_id=question.question_id,
        question_description=question.question_description,
        answer_description=question.answer_description,
        created_at=question.created_at
    )
    db.add(_question)
    db.commit()
    db.refresh(_question)
    return _question