import prompt


COUNT_ROUND = 3


def start_game(game):
    name = prompt.string('''Welcome to the Brain Games!
May I have your name? ''')
    print(f'Hello, {name}!\n{game.QUESTION}')

    for _ in range(COUNT_ROUND):
        game_question, right_answer = game.get_question_and_answer()
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
