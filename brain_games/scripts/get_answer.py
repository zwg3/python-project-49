#!/usr/bin/env python3
def get_answer(x, y, z):
    print(y)
    if y == x:
        print('Correct!')
        return 1
    elif y != x:
        print(f"'{y}' is wrong answer ;(. Correct answer was '{x}'.")
        print(f"Let's try again, {z}!")
        return 4
