#!/usr/bin/env python3

import random
import prompt
from brain_games.scripts.cli import welcome_user

NAME = welcome_user()


def get_answer(x, y):
    if y == x:
        print('Correct!')
        return 1
    elif y != x:
        print(f''''{y}' is wrong answer ;(. Correct answer was '{x}'.''')
        print(f'Let`s try again, {NAME}!')
        return 4


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    NUM = 0
    USER_ANSWER = 0
    CORRECT_ASWER = 0
    COUNT = 0
    while COUNT < 3:
        NUM = random.randint(1, 100)
        if NUM % 2 == 0:
            CORRECT_ASWER = 'yes'
        else:
            CORRECT_ASWER = 'no'
        print(f'Question: {NUM}')
        USER_ANSWER = prompt.string('Your answer: ')
        COUNT += get_answer(CORRECT_ASWER, USER_ANSWER)
        if COUNT == 3:
            print(f'Congratulations, {NAME}!')
