import random

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_INTEGER = 1
MAX_INTEGER = 100


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def get_conditions():
    number_1 = random.randint(MIN_INTEGER, MAX_INTEGER)
    if is_prime(number_1):
        answer = 'yes'
    else:
        answer = 'no'
    return str(number_1), str(answer)
