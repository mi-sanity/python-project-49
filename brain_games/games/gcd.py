import random


QUESTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
            gcd = num1 + num2
        else:
            num2 = num2 % num1
            gcd = num1 + num2
    return gcd


def get_question_and_answer():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    game_question = f'{number1} {number2}'
    right_answer = get_gcd(number1, number2)
    return game_question, right_answer
