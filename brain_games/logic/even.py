from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def logic():
    random_number = randint(1, 101)

    correct_answer = even(random_number)
    question = f'{random_number}'
    return correct_answer, question
