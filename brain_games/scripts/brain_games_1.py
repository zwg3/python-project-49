#!/usr/bin/env python3
from brain_games.cli import welcome_user
import prompt

NAME = welcome_user()


def get_answer(x, y, z):
    if y == x:
        print('Correct!')
        return 1
    elif y != x:
        print(f"'{y}' is wrong answer ;(. Correct answer was '{x}'.")
        print(f"Let's try again, {z}!")
        return 4


def game_starter(conditions, correct_answer, NAME):
    user_answer = 0
    result = 0
    print(f'Question: {conditions}')
    user_answer = prompt.string('Your answer: ')
    result = + get_answer(correct_answer, user_answer, NAME)
    return result


def conditions_resolver(question, conditions):
    print(question)
    count = 0
    while count < 3:
        conditions_1, correct_answer = conditions()
        count += game_starter(conditions_1, correct_answer, NAME)
        if count == 3:
            print(f'Congratulations, {NAME}!')
