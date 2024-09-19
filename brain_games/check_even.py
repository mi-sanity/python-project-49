#!/usr/bin/env python3

import prompt


def engine_game(game_module):
    name = prompt.string('''Welcome to the Brain Games!
May I have your name? ''')
    print(f'Hello, {name}!\n{question}')

    count_answer = 0
    while count_answer < 3:
        if_for_games = game_module.function()
        print(if_for_games)
        
        if user_answer == right_answer:
            count_answer = count_answer + 1
            print('Correct!')
        else:
            return print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{right_answer}".
Let's try again, {name}!''')
    return print(f'Congratulations, {name}!')

