# games/progression.py

import random


def get_question():
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    progression = [start * ratio ** i for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = " ".join(map(str, progression))
    return question, correct_answer


def start_progression_game():
    name = input("May I have your name? ")
    return {
        'name': name,
        'get_question': get_question,
    }
