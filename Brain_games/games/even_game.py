#!/usr/bin/env python3
import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def get_conditions():
    number_1 = random.randint(1, 100)
    answer = is_even(number_1)
    if answer:
        answer = 'yes'
    else:
        answer = 'no'
    return number_1, answer


def even_game():
    return (QUESTION, get_conditions())