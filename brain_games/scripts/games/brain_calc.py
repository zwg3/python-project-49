#!/usr/bin/env python3
import random
import prompt
from brain_games.scripts.cli import welcome_user

NAME = welcome_user()


def ask(z, a, b):
    if z == 1:
        CORRECT_ANSWER = a + b
        print(f'Question: {a} + {b}')
        return CORRECT_ANSWER
    elif z == 2:
        CORRECT_ANSWER = a - b
        print(f'Question: {a} - {b}')
        return CORRECT_ANSWER
    elif z == 3:
        CORRECT_ANSWER = a * b
        print(f'Question: {a} * {b}')
        return CORRECT_ANSWER


def get_answer(x, y):
    if y == x:
        print('Correct!')
        return 1
    elif y != x:
        print(f''''{y}' is wrong answer ;(. Correct answer was '{x}'.''')
        print(f'Let`s try again, {NAME}!')
        return 4


def main():
    print('What is the result of the expression?')
    NUMBER_1 = 0
    NUMBER_2 = 0
    OPERATION = 0
    USER_ANSWER = 0
    CORRECT_ANSWER = 0
    COUNT = 0

    while COUNT < 3:
        NUMBER_1 = random.randint(1, 100)
        NUMBER_2 = random.randint(1, 100)
        OPERATION = random.randint(1, 3)
        CORRECT_ANSWER = ask(OPERATION, NUMBER_1, NUMBER_2)
        USER_ANSWER = prompt.integer('Your answer: ')
        COUNT += get_answer(CORRECT_ANSWER, USER_ANSWER)
        if COUNT == 3:
            print(f'Congratulations, {NAME}!')
