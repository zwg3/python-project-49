#!/usr/bin/env python3
import random

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
    return str(question), str(answer)


def calc_game():
    return (QUESTION, get_conditions())
