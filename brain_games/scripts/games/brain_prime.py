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
        print(f'''Let's try again, {NAME}!''')
        return 4


def is_prime(x):
    if x < 2:
        return 'no'
    for i in range(2, x):
        if x % i == 0:
            return 'no'
    return 'yes'


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    NUMBER_1 = 0
    USER_ANSWER = 0
    CORRECT_ANSWER = 0
    COUNT = 0
    while COUNT < 3:
        NUMBER_1 = random.randint(1, 100)
        CORRECT_ANSWER = is_prime(NUMBER_1)
        print(f'Question: {NUMBER_1}')
        USER_ANSWER = prompt.string('Your answer: ')
        COUNT += get_answer(CORRECT_ANSWER, USER_ANSWER)
        if COUNT == 3:
            print(f'Congratulations, {NAME}!')
