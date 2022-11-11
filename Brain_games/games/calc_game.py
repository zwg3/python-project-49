#!/usr/bin/env python3
import random

QUESTION = 'What is the result of the expression?'


def get_numbers():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operation = random.randint(1, 3)
    return number_1, number_2, operation


def get_conditions(x):
    x, y, z = x()
    if z == 1:
        question = f'{x} + {y}'
        answer = x + y
    if z == 2:
        question = f'{x} - {y}'
        answer = x - y
    if z == 3:
        question = f'{x} * {y}'
        answer = x * y
    return str(question), str(answer)


def main():
    return get_conditions(get_numbers)
