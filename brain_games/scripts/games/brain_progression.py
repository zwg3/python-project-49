#!/usr/bin/env python3
import random
import prompt
from brain_games.scripts.cli import welcome_user

NAME = welcome_user()


def get_answer(x, y):
    if y == x:
        print('Correct!')
        return 1
    elif y != x:
        print(f''''{y}' is wrong answer ;(. Correct answer was '{x}'.''')
        print(f'Let`s try again, {NAME}!')
        return 4


def main():
    print('What number is missing in the progression?')
    STEP = 0
    LINE_INTEGERS = []
    LINE_STRINGS = []
    NUMBER_1 = 0
    NUMBER_2 = 0
    COUNT = 0
    REPLACED_INDEX = 0
    USER_ANSWER = 0
    CORRECT_ANSWER = 0
    while COUNT < 3:
        STEP = random.randint(1, 5)
        NUMBER_1 = random.randint(1, 20)
        NUMBER_2 = random.randint(65, 100)
        LINE_INTEGERS = list(range(NUMBER_1, NUMBER_2, STEP))
        LINE_INTEGERS = LINE_INTEGERS[0: 10]
        REPLACED_INDEX = random.randint(0, len(LINE_INTEGERS) - 1)
        for i, x in enumerate(LINE_INTEGERS):
            LINE_STRINGS.append(str(x))
        CORRECT_ANSWER = int(LINE_STRINGS[REPLACED_INDEX])
        LINE_STRINGS[REPLACED_INDEX] = '..'
        LINE_STRINGS = ' '.join(LINE_STRINGS)
        print(f'Question: {LINE_STRINGS}')
        USER_ANSWER = prompt.integer('Your answer: ')
        COUNT += get_answer(CORRECT_ANSWER, USER_ANSWER)
        LINE_STRINGS = []
        if COUNT == 3:
            print(f'Congratulations, {NAME}!')
