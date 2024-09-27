import random


QUESTION = 'What number is missing in the progression?'


def game_condition():
    global hidden_element
    random_start = random.randint(1, 20)
    random_step = random.randint(1, 10)
    list_progression = []

    for i in range(10):
        list_progression.append(random_start + random_step * i)

    index = random.randint(0, 9)
    hidden_element = list_progression[index]
    list_progression[index] = '..'
    new_list = ' '.join(str(el) for el in list_progression)
    print(f'Question: {new_list}')


def answer():
    correct_answer = hidden_element
    return str(correct_answer)
