import random


QUESTION = 'What number is missing in the progression?'


def game_question_right_answer():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    list_progression = []

    for i in range(10):
        list_progression.append(start + step * i)

    index = random.randint(0, 9)
    hidden_element = list_progression[index]
    list_progression[index] = '..'
    right_answer = hidden_element
    game_question = ' '.join(str(el) for el in list_progression)
    return game_question, right_answer
