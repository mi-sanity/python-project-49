#!/usr/bin/env python3

import prompt
import random


def calc_number():
    name = prompt.string('''Welcome to the Brain Games!
May I have your name? ''')
    print(f'''Hello, {name}!
What is the result of the expression?''')

    count_ans = 0
    while count_ans < 3:
        random_number1 = random.randint(1, 10)
        random_number2 = random.randint(1, 10)
        symbol = ['+', '-', '*']
        random_symbol = random.choice(symbol)
        
        if random_symbol == '+':
            result = random_number1 + random_number2
        elif random_symbol == '-':
            result = random_number1 - random_number2
        else:
            result = random_number1 * random_number2

        ans = prompt.string(f'''Question: {random_number1} {random_symbol} {random_number2}
Your answer: ''')
        if int(ans) == result:
            count_ans = count_ans + 1
            print('Correct!')
        else:
            return print(f'''"{ans}" is wrong answer ;(. Correct answer was "{result}".
Let's try again, {name}!''')
    return print(f'Congratulations, {name}!')
