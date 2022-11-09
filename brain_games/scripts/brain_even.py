#!/usr/bin/env python3

import random
import prompt
from brain_games.scripts.cli import welcome_user

name = welcome_user()


def get_answer(x, y):
    if y == x:
        print('Correct!')
        return 1
    elif y != x:
        print(f''''{y}' is wrong answer ;(. Correct answer was '{x}'.''')
        print(f'Let`s try again, {name}!')
        return 4


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num = 0
    user_answer = 0
    correct_answer = 0
    count = 0
    while count < 3:
        num = random.randint(1, 100)
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {num}')
        user_answer = prompt.string('Your answer: ')
        count += get_answer(correct_answer, user_answer)
        if count == 3:
            print(f'Congratulations, {name}!')