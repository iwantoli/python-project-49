from random import randint

TASK = 'Find the greatest common divisor of given numbers.'


def gcd(first_number, second_number):
    min_number = min(first_number, second_number)
    max_divider = 0

    for divider in range(1, min_number):
        if first_number % divider == 0 and second_number % divider == 0:
            max_divider = max(max_divider, divider)

    return str(max_divider)


def logic():
    first_number = randint(1, 100)
    second_number = randint(1, 100)

    correct_answer = gcd(first_number, second_number)
    question = f'{first_number} {second_number}'
    return correct_answer, question


