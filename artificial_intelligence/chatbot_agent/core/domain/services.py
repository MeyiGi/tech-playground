from core.domain.entities import Sentence


class BestMatchService:
    def find_best_match(self, question: str, sentences: list[Sentence]) -> Sentence:
        question_words = set(question.lower().split())

        best_match = None
        max_matches = 0

        for sentence in sentences:
            matches = len(sentence.words() & question_words)

            if matches > max_matches:
                best_match = sentence
                max_matches = matches

        return best_match