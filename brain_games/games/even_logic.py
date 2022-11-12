from random import randint
from prompt import string
from brain_games.cli import welcome_user


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def even():
    name = welcome_user()
    count = 0

    print('Answer \'yes\' if the number is even, otherwise answer \'no\'')

    while count != 3:
        random_number = randint(1, 101)
        answer = string(f'Question: {random_number} ').lower()
        print(f'Your answer: {answer}')

        if is_even(random_number) == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even(random_number)}'. Let's "
                  f"try again, {name}")
            count = 0

    print(f'Congratulations, {name}!')

