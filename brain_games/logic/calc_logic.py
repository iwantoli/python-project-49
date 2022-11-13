from brain_games.cli import welcome_user
from random import randint
from prompt import string


def calculation(first_number, second_number, operation):
    if operation == '+':
        return str(first_number + second_number)
    elif operation == '-':
        return str(first_number - second_number)
    elif operation == '*':
        return str(first_number * second_number)


def calc():
    name = welcome_user()
    count = 0

    print('What is the result of the expression?')

    while count != 3:
        first_number = randint(1, 40)
        second_number = randint(1, 40)
        operation = ['+', '-', '*'][randint(0, 2)]
        evalu = calculation(first_number, second_number, operation)

        answer = string(f"Question: {first_number} {operation} {second_number}, Answer: ")
        print(f'Your answer: {answer}')

        if evalu == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{evalu}'. Let's"
                  f"try again, {name}")
            count = 0

    print(f'Congratulations, {name}!')
