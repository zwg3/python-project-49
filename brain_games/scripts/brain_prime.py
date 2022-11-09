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


def is_prime(x):
    if x < 2:
        return 'no'
    for i in range(2, x):
        if x % i == 0:
            return 'no'
    return 'yes'


def main():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    num_1 = 0
    user_answer = 0
    correct_answer = 0
    count = 0
    while count < 3:
        num_1 = random.randint(1, 100)
        correct_answer = is_prime(num_1)
        print(f'Question: {num_1}')
        user_answer = prompt.string('Your answer: ')
        count += get_answer(correct_answer, user_answer)
        if count == 3:
            print(f'Congratulations, {name}!')
