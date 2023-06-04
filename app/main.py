from fastapi import FastAPI
import requests



app = FastAPI(
    title="Quiz quetsions request"
)



@app.get("/")
def get_hello():
    return "Hello, world!"


@app.post("/questions-{question_num}")
def post_number(question_num):
    response = requests.get(f'https://jservice.io/api/random?count={question_num}')
    
    list_of_questions = response.json()

    for question in list_of_questions:
        if question["answer"] in database['answer']:
            post_number(1)
        else:
            question["id"], question["answer"], question["question"], question["created_at"], question["value"]

    return response.json()