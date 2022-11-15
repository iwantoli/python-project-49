from random import randint

TASK = 'What number is missing in the progression?'


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
    prog = []

    while len(prog) < 5 or len(prog) > 11:
        start_prog = randint(0, 50)
        end_prog = randint(start_prog, 75)
        rand_step = randint(1, 6)
        prog = list(range(start_prog, end_prog, rand_step))

    rand_index = randint(0, len(prog) - 1)

    correct_answer = str(change(prog, rand_index))
    question = f'Question: {print_prog(prog)}'

    return correct_answer, question
