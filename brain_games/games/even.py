import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    game_question = random.randint(1, 10)

    if game_question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return game_question, right_answer
