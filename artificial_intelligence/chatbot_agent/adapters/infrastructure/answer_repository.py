from core.application.ports import AnswerRepositoryPort
from core.domain.entities import Sentence


class InMemoryAnswersRepository(AnswerRepositoryPort):
    def get_all(self):
        return [
            Sentence("я люблю программирование"),
            Sentence("программирование на python очень удобно"),
            Sentence("я изучаю архитектуру программ")
        ]