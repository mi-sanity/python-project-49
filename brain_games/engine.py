#!/usr/bin/env python3

import prompt


def engine_game(game_module):
    name = prompt.string('''Welcome to the Brain Games!
May I have your name? ''')
    print(f'Hello, {name}!\n{game_module.welcome_question}')

    count_answer = 0
    while count_answer < 3:
        game_module.game_condition()
        user_answer = prompt.string('Your answer: ')
        right_answer = game_module.answer()

        if user_answer == right_answer:
            count_answer = count_answer + 1
            print('Correct!')
        else:
            return print(f'''"{user_answer}" is wrong answer ;(. Correct answer was "{right_answer}".
Let's try again, {name}!''')
    return print(f'Congratulations, {name}!')
