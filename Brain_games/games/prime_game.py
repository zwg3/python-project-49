import random

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_INTEGER = 1
MAX_INTEGER = 100


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_conditions():
    random_number = random.randint(MIN_INTEGER, MAX_INTEGER)
    if is_prime(random_number):
        answer = 'yes'
    else:
        answer = 'no'
    return str(random_number), str(answer)
