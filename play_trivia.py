import json
import random
import os
import subprocess


def play_trivia():
    ''' Trivia gameplay'''
    # clears console
    clear()
    # Opens json file to load
    with open('Apprentice_TandemFor400_Data.json') as f:
        # Assigning json file to questions_and_answers as a list of dictionaries
        questions_and_answers = json.load(f)
        # Keeps tracks of the number of correct answers
        correct_counter = 0
        # shuffles questions in order to not keep getting the same 10 questions
        random.shuffle(questions_and_answers)
        # Iterates over first 10 questions
        for question in questions_and_answers[:10]:
            # prints question
            print(question['question'])
            # Combining correct and incorrect choices and assigning them to choices
            choices = question['incorrect'] + [question['correct']]
            display_answer_choices(choices)
            check_if_correct(question, choices)
        # Calls score rating in order to display appropriate message
        print(score_rating(correct_counter))
        input('Please press enter to continue...')
        # closes json file
        f.close()


def score_rating(correct):
    '''Depending on the user score, it displays the appropriate message'''

    if correct == 10:
        return f'Perfect, best trivia player to ever roam this world! Score: {correct}/10'
    elif correct > 7:
        return f'You did great! Score: {correct}/10'
    elif correct > 5:
        return f'Not bad, not great. Score: {correct}/10'
    else:
        return f'Were you even trying? Score: {correct}/10'


def clear():
    '''Clears console'''
    if os.name in ('nt', 'dos'):
        subprocess.call("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        subprocess.call("clear")
    else:
        print("\n") * 120


def display_answer_choices(choices):
    '''Displays answer choices in a random order'''
    # Shuffling in order to mask the correct answer, otherwise the correct answer would always be the last choice
    random.shuffle(choices)
    # Looping through choices to print
    for counter, answer in enumerate(choices):
        print(f'{counter + 1}. {answer}')


def check_if_correct(question, choices):
    '''Checks if user input is correct'''
    # while loop continues until user enters an answer choice
    while True:
        try:
            # User input gets assigned to choice
            choice = int(input(">> "))
            # checks if user input is one of the answer choices
            if choice in range(1, len(choices) + 1):
                # checks if user choice is the correct answer
                if choices[choice - 1] == question['correct']:
                    print(
                        f'Correct! The answer is {question["correct"]}')
                    correct_counter += 1
                    input('Press enter to continue...')
                    clear()
                    break
                else:
                    print(
                        f'Wrong! The answer is {question["correct"]}')
                    input('Press enter to continue...')
                    clear()
                    break
            print(f'{choice} isn\'t an answer choice.')
        except:
            print(
                'Incorrect input, enter the integer corresponding with your answer.')
# TODO:
# unit tests
# readme Python 3.8
