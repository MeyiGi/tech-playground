class CliController:
    def __init__(self, use_case):
        self.use_case = use_case

    def ask(self):
        question = input("Ввдите вопрос: ")
        answer = self.use_case.execute(question)
        print("Ответ:", answer)