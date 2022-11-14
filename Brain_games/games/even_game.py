import random

QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_INTEGER = 1
MAX_INTEGER = 100


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def get_conditions():
    random_number = random.randint(MIN_INTEGER, MAX_INTEGER)
    if is_even(random_number):
        answer = 'yes'
    else:
        answer = 'no'
    return random_number, answer
