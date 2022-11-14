import random

QUESTION = 'What number is missing in the progression?'
MIN_INTEGER = 1
MAX_INTEGER = 100
MIN_LINE_LIMIT_INTEGER = 20
MAX_LINE_LIMIT_ITEGER = 65
MIN_STEP_INTEGER = 1
MAX_STEP_INTEGER = 5


def get_progression():
    line_integers = []
    step = random.randint(MIN_STEP_INTEGER, MAX_STEP_INTEGER)
    number_1 = random.randint(MIN_INTEGER, MIN_LINE_LIMIT_INTEGER)
    number_2 = random.randint(MAX_LINE_LIMIT_ITEGER, MAX_INTEGER)
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
