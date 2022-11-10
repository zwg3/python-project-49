#!/usr/bin/env python3
from brain_games.scripts.welcome_user import welcome_user
from brain_games.scripts.game_starter_integers import game_starter
import random

NAME = welcome_user()
QUESTION = 'What is the result of the expression?'


def get_conditions():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operation = random.randint(1, 3)
    question = 0
    answer = 0
    if operation == 1:
        question = f'{number_1} + {number_2}'
        answer = number_1 + number_2
    if operation == 2:
        question = f'{number_1} - {number_2}'
        answer = number_1 - number_2
    if operation == 3:
        question = f'{number_1} * {number_2}'
        answer = number_1 * number_2
    return question, answer


def main():
    print(QUESTION)
    count = 0
    while count < 3:
        conditions, correct_answer = get_conditions()
        count += game_starter(conditions, correct_answer, NAME)
        if count == 3:
            print(f'Congratulations, {NAME}!')
