from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel


T = TypeVar('T')


class QuizSchema(BaseModel):

    id: Optional[int]=None
    question_id: Optional[int]=None
    question_description: Optional[str]=None
    answer_description: Optional[str]=None
    created_at: Optional[str]=None

    class Config:
        orm_mode = True


class RequestQuiz(BaseModel):
    parameter: QuizSchema - Field(...)



class Response(GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]