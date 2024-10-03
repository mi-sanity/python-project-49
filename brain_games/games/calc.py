import random


QUESTION = 'What is the result of the expression?'


def get_question_and_answer():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    symbol = random.choice(['+', '-', '*'])
    game_question = f'{number1} {symbol} {number2}'

    if symbol == '+':
        right_answer = number1 + number2
    elif symbol == '-':
        right_answer = number1 - number2
    elif symbol == '*':
        right_answer = number1 * number2

    return game_question, right_answer
