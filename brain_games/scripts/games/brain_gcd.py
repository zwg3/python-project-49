#!/usr/bin/env python3
from math import gcd
from brain_games.scripts.cli import welcome_user
import random
import prompt

NAME = welcome_user()


def get_answer(x, y):
    if y == x:
        print('Correct!')
        return 1
    elif y != x:
        print(f''''{y}' is wrong answer ;(. Correct answer was '{x}'.''')
        print(f'''Let's try again, {NAME}!''')
        return 4


def main():
    print('Find the greatest common divisor of given numbers.')
    NUMBER_1 = 0
    NUMBER_2 = 0
    USER_ANSWER = 0
    CORRECT_ANSWER = 0
    COUNT = 0
    while COUNT < 3:
        NUMBER_1 = random.randint(1, 100)
        NUMBER_2 = random.randint(1, 100)
        CORRECT_ANSWER = gcd(NUMBER_1, NUMBER_2)
        print(f'Question: {NUMBER_1} {NUMBER_2}')
        USER_ANSWER = prompt.integer('Your answer: ')
        COUNT += get_answer(CORRECT_ANSWER, USER_ANSWER)
        if COUNT == 3:
            print(f'Congratulations, {NAME}!')
