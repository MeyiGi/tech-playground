class Sentence:
    def __init__(self, text: str):
        self.text = text

    def words(self) -> set:
        """
        Get the set of unique words in the sentence.
        
        :param self: Description
        :return: Description
        :rtype: set
        """
        return set(self.text.split())