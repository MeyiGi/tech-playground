from core.application.ports import AnswerRepositoryPort
from core.domain.services import BestMatchService


class GetAnswerUseCase:
    def __init__(self, repository: AnswerRepositoryPort):
        self.repository = repository
        self.service = BestMatchService()

    def execute(self, question: str) -> str:
        sentences = self.repository.get_all()
        result = self.service.find_best_match(question=question, sentences=sentences)
        return result.text if result else "Ответ не найден"