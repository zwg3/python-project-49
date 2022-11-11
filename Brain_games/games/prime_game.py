#!/usr/bin/env python3
import random

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def get_conditions():
    number_1 = random.randint(1, 100)
    if is_prime(number_1):
        answer = 'yes'
    else:
        answer = 'no'
    return str(number_1), str(answer)


def main():
    return (get_conditions())
