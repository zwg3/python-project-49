#!/usr/bin/env python3
import random
from brain_games.scripts.welcome_user import welcome_user
from brain_games.scripts.game_starter_integers import game_starter

NAME = welcome_user()
QUESTION = 'What number is missing in the progression?'


def get_conditions():
    step = 0
    line_integers = []
    line_strings = []
    number_1 = 0
    number_2 = 0
    replaced_index = 0
    replaced_value = 0
    step = random.randint(1, 5)
    number_1 = random.randint(1, 20)
    number_2 = random.randint(65, 100)
    line_integers = list(range(number_1, number_2, step))
    line_integers = line_integers[0: 10]
    replaced_index = random.randint(0, len(line_integers) - 1)
    for i, x in enumerate(line_integers):
        line_strings.append(str(x))
    replaced_value = int(line_strings[replaced_index])
    line_strings[replaced_index] = '..'
    line_strings = ' '.join(line_strings)
    return line_strings, replaced_value


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
