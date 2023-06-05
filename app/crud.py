from repository import QuestionsRepository
from model import QuizQuestion
import requests


class QuizService():
    def __init__(self, repository:QuestionsRepository):
        self.repository = repository
    
    def get_questions(self, question_num):
        response = requests.get(f'https://jservice.io/api/random?count={question_num}')
        list_of_questions = response.json()
        print(list_of_questions)
        for question in list_of_questions:
            _question = QuizQuestion(
                id = question['id'],
                # question_id=question['id'],
                question_description=question['question'],
                answer_description=question['answer'],
                created_at=question['created_at']
            )    
            self.repository.create_question(_question)
        return response.json()