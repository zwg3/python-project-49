#!/usr/bin/env python3
import prompt


def game_starter(conditions):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    count = 0
    print(conditions.QUESTION)
    while count < 3:
        recieved_conditions = conditions.get_conditions()
        question_for_user, correct_answer = recieved_conditions
        print(f'Question: {question_for_user}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')
