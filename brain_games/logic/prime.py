from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(number):
    div = 2
    while div * div < number:
        if number % div == 0:
            return 'no'
        div += 1
    if div * div == number:
        return 'no'

    return 'yes'


def logic():
    number = randint(1, 200)

    correct_answer = prime(number)
    question = f'{number}'

    return correct_answer, question
