#!/usr/bin/env python3
from brain_games.scripts.welcome_user import welcome_user
from brain_games.scripts.game_starter_strings import game_starter
import random

NAME = welcome_user()
QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def get_conditions():
    number_1 = random.randint(1, 100)
    answer = 0
    if is_prime(number_1):
        answer = 'yes'
    else:
        answer = 'no'
    return number_1, answer


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
