#!/usr/bin/env python3
import random

QUESTION = 'What number is missing in the progression?'


def get_progression():
    line_integers = []
    step = random.randint(1, 5)
    number_1 = random.randint(1, 20)
    number_2 = random.randint(65, 100)
    line_integers = list(range(number_1, number_2, step))
    line_integers = line_integers[0: 10]
    return line_integers


def get_conditions():
    line_integers = get_progression()
    line_strings = []
    replaced_index = random.randint(0, len(line_integers) - 1)
    for i, x in enumerate(line_integers):
        line_strings.append(str(x))
    replaced_value = int(line_strings[replaced_index])
    line_strings[replaced_index] = '..'
    line_strings = ' '.join(line_strings)
    return str(line_strings), str(replaced_value)
