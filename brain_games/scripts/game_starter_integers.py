import prompt
from brain_games.scripts.get_answer import get_answer


def game_starter(conditions, correct_answer, NAME):
    user_answer = 0
    result = 0
    print(f'Question: {conditions}')
    user_answer = prompt.integer('Your answer: ')
    result = + get_answer(correct_answer, user_answer, NAME)
    return result
