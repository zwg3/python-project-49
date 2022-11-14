import random

QUESTION = 'What is the result of the expression?'
MIN_INTEGER = 1
MAX_INTEGER = 100
MATH_OPERATIONS = ['+', '-', '*']


def get_question():
    number_1 = random.randint(MIN_INTEGER, MAX_INTEGER)
    number_2 = random.randint(MIN_INTEGER, MAX_INTEGER)
    chosen_operation = random.choice(MATH_OPERATIONS)
    question = f'{number_1} {chosen_operation} {number_2}'
    return question


def get_conditions():
    question = get_question()
    equation = question.split()
    if equation[1] == '+':
        answer = int(equation[0]) + int(equation[2])
    if equation[1] == '-':
        answer = int(equation[0]) - int(equation[2])
    if equation[1] == '*':
        answer = int(equation[0]) * int(equation[2])
    return str(question), str(answer)
