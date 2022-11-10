#!/usr/bin/env python3
from brain_games.scripts.brain_games_main import conditions_resolver
import random

QUESTION = 'What number is missing in the progression?'


def get_progression():
    step = 0
    line_integers = []
    number_1 = 0
    number_2 = 0
    step = random.randint(1, 5)
    number_1 = random.randint(1, 20)
    number_2 = random.randint(65, 100)
    line_integers = list(range(number_1, number_2, step))
    line_integers = line_integers[0: 10]
    return line_integers


def get_conditions():
    line_integers = get_progression()
    line_strings = []
    replaced_index = 0
    replaced_value = 0
    replaced_index = random.randint(0, len(line_integers) - 1)
    for i, x in enumerate(line_integers):
        line_strings.append(str(x))
    replaced_value = int(line_strings[replaced_index])
    line_strings[replaced_index] = '..'
    line_strings = ' '.join(line_strings)
    return str(line_strings), str(replaced_value)


def main():
    conditions_resolver(QUESTION, get_conditions)
