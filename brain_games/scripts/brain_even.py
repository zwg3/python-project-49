#!/usr/bin/env python3
import random


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num = 0
    correct_answer = 0
    user_answer = 0
    count = 0
    while count < 3:
        num = random.randint(1, 100)
        if num % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(f'Question: {num}')
        user_answer = input()
        if user_answer == correct_answer:
            print('Correct!')
            count += 1
