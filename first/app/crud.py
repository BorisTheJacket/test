from repository import QuestionsRepository
from model import QuizQuestion
import requests


class QuizService():

    _max_retry = 10

    def __init__(self, repository:QuestionsRepository):
        self.repository = repository
    

    def api_request(self, question_num):
        response = requests.get(f'https://jservice.io/api/random?count={question_num}')
        return response.json()


    def get_questions(self, question_num):
        last_saved = None
        
        for _ in range(self._max_retry):

            for question in self.api_request(question_num):
                _question = QuizQuestion(
                    id = question['id'],
                    question_description=question['question'],
                    answer_description=question['answer'],
                    created_at=question['created_at']
                )    
                if not self.repository.question_exists(_question):    
                    self.repository.create_question(_question)
                    last_saved = question
            if last_saved != None:
                return last_saved
        return None
    

