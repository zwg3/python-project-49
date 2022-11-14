import random

QUESTION = 'What number is missing in the progression?'
MIN_INTEGER = 1
MAX_INTEGER = 100
MIN_LINE_LIMIT_INTEGER = 20
MAX_LINE_LIMIT_ITEGER = 65
MIN_STEP_INTEGER = 1
MAX_STEP_INTEGER = 5


def get_progression():
    line = []
    step = random.randint(MIN_STEP_INTEGER, MAX_STEP_INTEGER)
    number_1 = random.randint(MIN_INTEGER, MIN_LINE_LIMIT_INTEGER)
    number_2 = random.randint(MAX_LINE_LIMIT_ITEGER, MAX_INTEGER)
    for i in range(number_1, number_2, step):
        line.append(str(i))
    line = line[0: 10]
    return line


def get_conditions():
    line = get_progression()
    replaced_index = random.randint(0, len(line) - 1)
    replaced_value = int(line[replaced_index])
    line[replaced_index] = '..'
    line = ' '.join(line)
    return str(line), str(replaced_value)
