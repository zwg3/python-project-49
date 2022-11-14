from math import gcd
import random

QUESTION = 'Find the greatest common divisor of given numbers.'
MIN_INTEGER = 1
MAX_INTEGER = 100


def get_conditions():
    number_1 = random.randint(MIN_INTEGER, MAX_INTEGER)
    number_2 = random.randint(MIN_INTEGER, MAX_INTEGER)
    question = f'{number_1} {number_2}'
    asnswer = gcd(number_1, number_2)
    return str(question), str(asnswer)
