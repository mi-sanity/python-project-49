import random


QUESTION = 'Find the greatest common divisor of given numbers.'


def game_question_right_answer():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    game_question = f'{number1} {number2}'

    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
            right_answer = number1 + number2
        else:
            number2 = number2 % number1
            right_answer = number1 + number2
    return game_question, right_answer
