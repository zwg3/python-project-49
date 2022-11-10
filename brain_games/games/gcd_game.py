#!/usr/bin/env python3
from brain_games.scripts.welcome_user import welcome_user
from brain_games.scripts.game_starter_integers import game_starter
from math import gcd
import random

NAME = welcome_user()
QUESTION = 'Find the greatest common divisor of given numbers.'


def get_conditions():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {number_2}'
    asnswer = gcd(number_1, number_2)
    return question, asnswer


def main():
    print(QUESTION)
    count = 0
    while count < 3:
        conditions, correct_answer = get_conditions()
        count += game_starter(conditions, correct_answer, NAME)
        if count == 3:
            print(f'Congratulations, {NAME}!')


if __name__ == "__main__":
    main()
