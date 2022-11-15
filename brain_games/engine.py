from brain_games.cli import welcome_user
from prompt import string


def rounds(correct_answer, question):
    your_answer = string(f"Question: {question} ")
    print(f"Your answer: {your_answer}")

    if your_answer == correct_answer:
        return False
    else:
        return your_answer


def course_game(game):
    name = welcome_user()
    print(game.TASK)
    count = 0

    while count != 3:
        correct_answer, question = game.logic()
        ans = rounds(correct_answer, question)
        if ans is False:
            print('Correct!')
            count += 1
        else:
            print(f"'{ans}' is wrong answer ;(. Correct answer was '{correct_answer}'")
            print("Let's "f"try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')

