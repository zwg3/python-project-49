#!/usr/bin/env python3
import random
import prompt
from brain_games.scripts.cli import welcome_user

name = welcome_user()


def ask(z, a, b):
    if z == 1:
        correct_answer = a + b
        print(f'Question: {a} + {b}')
        return correct_answer
    elif z == 2:
        correct_answer = a - b
        print(f'Question: {a} - {b}')
        return correct_answer
    elif z == 3:
        correct_answer = a * b
        print(f'Question: {a} * {b}')
        return correct_answer


def get_answer(x, y):
    if y == x:
        print('Correct!')
        return 1
    elif y != x:
        print(f''''{y}' is wrong answer ;(. Correct answer was '{x}'.''')
        print(f'Let`s try again, {name}!')
        return 4


def main():
    print('What is the result of the expression?')
    num_1 = 0
    num_2 = 0
    operation = 0
    user_answer = 0
    correct_answer = 0
    count = 0

    while count < 3:
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)
        operation = random.randint(1, 3)
        correct_answer = ask(operation, num_1, num_2)
        user_answer = prompt.integer('Your answer: ')
        count += get_answer(correct_answer, user_answer)
        if count == 3:
            print(f'Congratulations, {name}!')
