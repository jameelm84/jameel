import random

from typing import Tuple

from quiz_questions import *


def get_random_question() -> Tuple[str, str]:  # Selects a random question from the question dictionary.
    question, answer = random.choice(list(game_questions.items()))  # ('What is the capital of France?', 'Paris')
    # game_questions.pop(question)
    return question, answer

user_score = 0l
def check_answer(question, user_answer) -> bool :
    correct_answer = game_questions.get(question)
    return user_answer.lower() == correct_answer.lower()


# print(get_random_question())
