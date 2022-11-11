#!/usr/bin/env python3
import prompt


def game_starter(conditions):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count = 0
    print(conditions.QUESTION)
    while count < 3:
        recieved_conditions = conditions.main()
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
