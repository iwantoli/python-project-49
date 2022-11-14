from brain_games.cli import welcome_user
from random import randint
from prompt import string


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
    name = welcome_user()
    count = 0

    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    while count != 3:
        number = randint(1, 200)
        answer = prime(number)

        your_answer = string(f'Question: {number}, Answer: ').lower()
        print(f'Your answer: {your_answer}')

        if your_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{answer}'. Let's "
                  f"try again, {name}")
            count = 0

    print(f'Congratulations, {name}!')
