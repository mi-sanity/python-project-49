import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_condition():
    global random_number
    random_number = random.randint(1, 10)
    print(f'Question: {random_number}')


def answer():
    if random_number % 2 == 0:
        return 'yes'
    elif random_number % 2 != 0:
        return 'no'
