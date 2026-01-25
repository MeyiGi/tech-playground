from abc import ABC, abstractclassmethod

class AnswerRepositoryPort(ABC):
    @abstractclassmethod
    def get_all(self):
        ...