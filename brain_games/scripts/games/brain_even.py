#!/usr/bin/env python3
from brain_games.scripts.welcome_user import welcome_user
from brain_games.scripts.game_starter_strings import game_starter
import random

NAME = welcome_user()
QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def get_conditions():
    number_1 = random.randint(1, 100)
    answer = is_even(number_1)
    if answer:
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
