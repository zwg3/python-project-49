#!/usr/bin/env python3
from brain_games.scripts.brain_games_1 import conditions_resolver
from math import gcd
import random

QUESTION = 'Find the greatest common divisor of given numbers.'


def get_conditions():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {number_2}'
    asnswer = gcd(number_1, number_2)
    return str(question), str(asnswer)


def main():
    conditions_resolver(QUESTION, get_conditions)
