from enum import Enum
from words.Words import *


class Difficulty(Enum):
    JUNIOR = 1
    MIDDLE = 2
    SENIOR = 3
    VERBAL = 4


class GameMode:
    def __init__(self, difficulty: Difficulty, time: int, max_score: int):
        self._difficulty = difficulty
        self._time = time
        self._max_score = max_score

        if difficulty == Difficulty.JUNIOR:
            self._words = JUNIOR_WORDS
        elif difficulty == Difficulty.MIDDLE:
            self._words = MIDDLE_WORDS
        elif difficulty == Difficulty.SENIOR:
            self._words = SENIOR_WORDS
        elif difficulty == Difficulty.VERBAL:
            self._words = VERBAL_WORDS
        else:
            raise ValueError(f"Wrong difficulty given ({difficulty})")

    @property
    def difficulty(self):
        return self._difficulty

    @property
    def time(self):
        return self._time

    @property
    def words(self):
        return self._words.copy()

    @property
    def max_score(self):
        return self._max_score
