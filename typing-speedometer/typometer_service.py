import random
from words_data import fetch_words


class TypoSpeedometerService:
    def __init__(self):
        self.wordlist = fetch_words()
        self.correct_words = 0

    def compare_words(self, requested_word: str, given_word: str):

        if requested_word.strip() == given_word.strip():
            self.correct_words += 1
            return True
        else:
            return False

    def calculate_wpm(self):
        return round(self.correct_words)

    def reset(self):
        self.wordlist = fetch_words()
        self.correct_words = 0

    def fetch_random_word(self):
        return self.wordlist[random.randrange(len(self.wordlist))]
