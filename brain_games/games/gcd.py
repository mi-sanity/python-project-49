#!/usr/bin/env python3

import random


question = 'Find the greatest common divisor of given numbers.'


def game_condition():
    global random_number1
    global random_number2
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)
    print(f'Question: {random_number1} {random_number2}')


def answer():
    random_number3 = random_number1
    random_number4 = random_number2

    while random_number3 != 0 and random_number4 != 0:
        if random_number3 > random_number4:
            random_number3 = random_number3 % random_number4
            result = random_number3 + random_number4
        else:
            random_number4 = random_number4 % random_number3
            result = random_number3 + random_number4
    return str(result)
