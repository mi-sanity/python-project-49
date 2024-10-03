import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_prime(num):
    if num < 2:
        return False

    for divider in range(2, int(num ** 0.5) + 1):
        if num % divider == 0:
            return False
    return True


def get_question_and_answer():
    game_question = random.randint(1, 20)
    right_answer = 'yes' if check_prime(game_question) else 'no'
    return game_question, right_answer
