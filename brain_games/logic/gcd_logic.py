from brain_games.cli import welcome_user
from random import randint
from prompt import string


def gcd(first_number, second_number):
    min_number = min(first_number, second_number)
    max_divider = 0

    for divider in range(1, min_number):
        if first_number % divider == 0 and second_number % divider == 0:
            max_divider = max(max_divider, divider)

    return str(max_divider)


def logic():
    name = welcome_user()
    count = 0

    print('Find the greatest common divisor of given numbers.')

    while count != 3:
        first_number = randint(0, 100)
        second_number = randint(0, 100)
        answer = gcd(first_number, second_number)

        your_answer = string(f"Question: {first_number} {second_number}, Answer: ")
        print(f'Your answer: {answer}')

        if your_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{your_answer}'. \nLet's"
                  f"try again, {name}")
            count = 0

    print(f'Congratulations, {name}!')
