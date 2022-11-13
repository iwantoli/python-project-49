from brain_games.cli import welcome_user
from random import randint
from prompt import string


def print_prog(prog):
    seq = ''
    for elem in prog:
        if seq:
            seq += ' '
        seq += str(elem)
    return seq


def change(prog, rand_index):
    number = 0
    for index in range(len(prog)):
        if index == rand_index:
            number = prog[index]
            prog[index] = '..'
    return number


def logic():
    name = welcome_user()
    count = 0

    print('What number is missing in the progression?')

    while count != 3:
        prog = []

        while len(prog) < 5 or len(prog) > 11:
            start_prog = randint(0, 50)
            end_prog = randint(start_prog, 75)
            rand_step = randint(1, 6)
            prog = list(range(start_prog, end_prog, rand_step))

        rand_index = randint(0, len(prog) - 1)
        answer = str(change(prog, rand_index))

        your_answer = string(f'Question: {print_prog(prog)}, Answer: ')
        print(f'Your answer: {your_answer}')

        if your_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{your_answer}' is wrong answer ;(. Correct answer was '{answer}'. Let's "
                  f"try again, {name}")
            count = 0

    print(f'Congratulations, {name}!')
