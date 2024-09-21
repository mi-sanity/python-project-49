#!/usr/bin/env python3

import random


welcome_question = 'What is the result of the expression?'

def game_condition():
    global random_number1 
    global random_number2
    global random_symbol
    random_number1 = random.randint(1, 10)
    random_number2 = random.randint(1, 10)
    symbol = ['+', '-', '*']
    random_symbol = random.choice(symbol)
    print(f'Question: {random_number1} {random_symbol} {random_number2}')


def answer():
    if random_symbol == '+':
        calc_sum = random_number1 + random_number2
        return str(calc_sum)
    elif random_symbol == '-':
        calc_diff = random_number1 - random_number2
        return str(calc_diff)
    else:
        calc_multi = random_number1 * random_number2
        return str(calc_multi)
