#!/usr/bin/env python3
from Brain_games.cli import welcome_user
import prompt

NAME = welcome_user()


def game_starter(conditions):
    question_for_user = 0
    count = 0
    while count < 1:
        game_question, recieved_conditions = conditions()
        question_for_user, c = recieved_conditions
        print(game_question)
        print(f'Question: {question_for_user}')
        u = prompt.string('Your answer: ')
        if u == c:
            print('Correct!')
            count += 1
        else:
            print(f"'{u}' is wrong answer ;(. Correct answer was '{c}'.")
            print(f"Let's try again, {NAME}!")
            count += 4
        while count < 3:
            game_question, recieved_conditions = conditions()
            question_for_user, c = recieved_conditions
            print(f'Question: {question_for_user}')
            u = prompt.string('Your answer: ')
            if u == c:
                print('Correct!')
                count += 1
            else:
                print(f"'{u}' is wrong answer ;(. Correct answer was '{c}'.")
                print(f"Let's try again, {NAME}!")
                count += 4
        if count == 3:
            print(f'Congratulations, {NAME}!')
