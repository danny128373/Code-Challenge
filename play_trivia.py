import json
import random


def play_trivia():
    # Open json file to load
    with open('Apprentice_TandemFor400_Data.json') as f:
        # Assigning json file to questions_and_answers as a list of dictionaries
        questions_and_answers = json.load(f)
        # Looping through each question and display question and choices
        correct_counter = 0
        for question in questions_and_answers:
            # prints question
            print(question['question'])
            # Combining correct and incorrect choices and assigning them to choices variable
            choices = question['incorrect'] + [question['correct']]
            # Shuffling in order to mask the correct answer, otherwise the correct answer would always be the last choice
            random.shuffle(choices)
            # Looping through choices to print
            for counter, answer in enumerate(choices):
                print(f'{counter + 1}. {answer}')

            while True:
                # User input gets assigned to choice
                choice = int(input(">> "))
                if choice in range(1, len(choices) + 1):
                    if choices[choice - 1] == question['correct']:
                        print(f'Correct! The answer is {question["correct"]}')
                        correct_counter += 1
                        break
                    else:
                        print(f'Wrong! The answer is {question["correct"]}')
                        break
                print(
                    'Incorrect input, please enter an integer representing your answer.')
