#!/usr/bin/env python3

import random
import prompt

question = 'Answer "yes" if the number is even, otherwise answer "no".'

def function():
    random_number = random.randint(1, 10)
    user_answer = prompt.string(f'''Question: {random_number}
Your answer: ''')

    if random_number % 2 == 0:
        right_answer = 'yes'
    elif random_number % 2 != 0:
        right_answer = 'no'



