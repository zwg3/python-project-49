import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_INTEGER = 1
MAX_INTEGER = 100


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def get_conditions():
    number_1 = random.randint(MIN_INTEGER, MAX_INTEGER)
    answer = is_even(number_1)
    if answer:
        answer = 'yes'
    else:
        answer = 'no'
    return number_1, answer
