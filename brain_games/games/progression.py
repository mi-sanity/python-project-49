import random


QUESTION = 'What number is missing in the progression?'
LENGTH = 10

def get_question_and_answer():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    stop = start + step * LENGTH

    list_progression = list(range(start, stop, step))

    index = random.randint(0, 9)
    hidden_element = list_progression[index]
    list_progression[index] = '..'
    right_answer = hidden_element
    game_question = ' '.join(str(el) for el in list_progression)
    return game_question, right_answer
