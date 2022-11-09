#!/usr/bin/env python3
from math import gcd
from brain_games.scripts.cli import welcome_user
import random
import prompt

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
    print('Find the greatest common divisor of given numbers.')
    num_1 = 0
    num_2 = 0
    user_answer = 0
    correct_answer = 0
    count = 0
    while count < 3:
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)
        correct_answer = gcd(num_1, num_2)
        print(f'Question: {num_1} {num_2}')
        user_answer = prompt.integer('Your answer: ')
        count += get_answer(correct_answer, user_answer)
        if count == 3:
            print(f'Congratulations, {name}!')