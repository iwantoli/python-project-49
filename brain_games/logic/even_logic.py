from brain_games.cli import welcome_user
from random import randint
from prompt import string


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def logic():
    name = welcome_user()
    count = 0

    print('Answer "yes" if the number is even, otherwise answer "no".')

    while count != 3:
        random_number = randint(1, 101)
        answer = is_even(random_number)
        your_answer = string(f"Question: {random_number} ").lower()
        print(f'Your answer: {your_answer}')

        if your_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's"
                  f"try again, {name}!")
            count = 0

    print(f'Congratulations, {name}!')
