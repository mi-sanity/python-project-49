import random
import math

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def answer(x):
    if x < 2:
        return False

    divider = 2

    while divider <= math.sqrt(x):
        if x % divider == 0:
            return False
        divider = divider + 1
    return True


def game_question_right_answer():
    game_question = random.randint(1, 20)
    right_answer = 'yes' if answer(game_question) else 'no'
    return game_question, right_answer
