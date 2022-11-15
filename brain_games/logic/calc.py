from random import randint

TASK = 'What is the result of the expression?'


def calculation(first_number, second_number, operation):
    if operation == '+':
        return str(first_number + second_number)
    elif operation == '-':
        return str(first_number - second_number)
    elif operation == '*':
        return str(first_number * second_number)


def logic():

    first_number = randint(1, 40)
    second_number = randint(1, 40)
    operation = ['+', '-', '*'][randint(0, 2)]

    correct_answer = calculation(first_number, second_number, operation)
    question = f'{first_number} {operation} {second_number}'
    return correct_answer, question



