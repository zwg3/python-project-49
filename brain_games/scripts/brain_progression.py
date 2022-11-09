#!/usr/bin/env python3
import random
from brain_games.scripts.cli import welcome_user

name = welcome_user()


def get_answer(x):
    user_answer = int(input())
    if user_answer == x:
        print('Correct!')
        return 1
    elif user_answer != x:
        print(f'{user_answer} is wrong answer ;(. Correct answer was {x}')
        print(f'Let`s try again, {name}!')
        return 4


def main():
    print('What number is missing in the progression?')
    step = 0
    line = []
    line_str = []
    num_1 = 0
    num_2 = 0
    step = 0
    count = 0
    replaced = 0
    correct_answer = 0
    while count < 3:
        step = random.randint(2, 5)
        num_1 = random.randint(1, 20)
        num_2 = random.randint(65, 100)
        line = list(range(num_1, num_2, step))
        line = line[0: 10]
        replaced = random.randint(0, len(line) - 1)
        for i, x in enumerate(line):
            line_str.append(str(x))
        correct_answer = int(line_str[replaced])
        line_str[replaced] = '..'
        line_str = ' '.join(line_str)
        print(f'Question: {line_str}')
        count += get_answer(correct_answer)
        line_str = []
        if count == 3:
            print(f'Congratulations, {name} !')
