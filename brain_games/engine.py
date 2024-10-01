import prompt


def engine_game(game_module):
    name = prompt.string('''Welcome to the Brain Games!
May I have your name? ''')
    print(f'Hello, {name}!\n{game_module.QUESTION}')

    count_answer = 3

    for _ in range(count_answer):
        game_question, right_answer = game_module.game_question_right_answer()
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != str(right_answer):
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'."
                  f"\nLet's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
