#!/usr/bin/env python3

import random
import math

question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_condition():
    global random_number
    random_number = random.randint(1, 20)
    print(f'Question: {random_number}')


def answer():
    if random_number < 2:
        return 'no'

    divider = 2

    while divider <= math.sqrt(random_number):
        if random_number % divider == 0:
            return 'no'
        divider = divider + 1
    return 'yes'
