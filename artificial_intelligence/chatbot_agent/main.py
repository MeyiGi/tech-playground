from adapters.infrastructure.answer_repository import InMemoryAnswersRepository
from adapters.interface.cli_controller import CliController
from core.application.use_cases import GetAnswerUseCase


repo = InMemoryAnswersRepository()
use_case = GetAnswerUseCase(repository=repo)
cli_controller = CliController(use_case)

while True:
    cli_controller.ask()