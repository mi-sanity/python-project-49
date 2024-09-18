#!/usr/bin/env python3

import prompt
import random


def even_number():
    name = prompt.string('''Welcome to the Brain Games!
May I have your name? ''')
    print(f'''Hello, {name}!
Answer "yes" if the number is even, otherwise answer "no".''')

    count_ans = 0
    while count_ans < 3:
        random_number = random.randint(1, 10)
        ans = prompt.string(f'''Question: {random_number}
Your answer: ''')
        if random_number % 2 == 0 and ans.lower() == 'yes':
            count_ans = count_ans + 1
            print('Correct!')
        elif random_number % 2 == 0 and ans.lower() != 'yes':
            return print(f'''"{ans}" is wrong answer ;(. Correct answer was "yes".
Let's try again, {name}!''')
        elif random_number % 2 != 0 and ans.lower() == 'no':
            count_ans = count_ans + 1
            print('Correct!')
        else:
            return print(f'''"{ans}" is wrong answer ;(. Correct answer was "no".
Let's try again, {name}!''')
    return print(f'Congratulations, {name}!')
