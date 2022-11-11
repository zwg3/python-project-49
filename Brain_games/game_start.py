#!/usr/bin/env python3
import prompt
from Brain_games.games import calc_game

a = calc_game



def game_starter(conditions):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count = 0
    print(a.QUESTION)
    while count < 1:
        question_for_user, c = conditions()
        print(f'Question: {question_for_user}')
        u = prompt.string('Your answer: ')
        if u == c:
            print('Correct!')
            count += 1
        else:
            print(f"'{u}' is wrong answer ;(. Correct answer was '{c}'.")
            print(f"Let's try again, {name}!")
            break
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
                print(f"Let's try again, {name}!")
                break
        if count == 3:
            print(f'Congratulations, {name}!')




# def game_starter(conditions):
#     print('Welcome to the Brain Games!')
#     name = prompt.string('May I have your name? ')
#     print('Hello, ' + name + '!')
#     count = 0
#     while count < 1:
#         game_question, recieved_conditions = conditions()
#         question_for_user, c = recieved_conditions
#         print(game_question)
#         print(f'Question: {question_for_user}')
#         u = prompt.string('Your answer: ')
#         if u == c:
#             print('Correct!')
#             count += 1
#         else:
#             print(f"'{u}' is wrong answer ;(. Correct answer was '{c}'.")
#             print(f"Let's try again, {name}!")
#             break
#         while count < 3:
#             game_question, recieved_conditions = conditions()
#             question_for_user, c = recieved_conditions
#             print(f'Question: {question_for_user}')
#             u = prompt.string('Your answer: ')
#             if u == c:
#                 print('Correct!')
#                 count += 1
#             else:
#                 print(f"'{u}' is wrong answer ;(. Correct answer was '{c}'.")
#                 print(f"Let's try again, {name}!")
#                 break
#         if count == 3:
#             print(f'Congratulations, {name}!')
