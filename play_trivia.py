import json
import random
import os
import subprocess


class PlayTrivia():
    def __init__(self):
        # Keeps tracks of the number of correct answers
        self.correct_counter = 0

    def clear(self):
        '''Clears console'''
        if os.name in ('nt', 'dos'):
            subprocess.call("cls")
        elif os.name in ('linux', 'osx', 'posix'):
            subprocess.call("clear")
        else:
            print("\n") * 120

    def play_trivia(self):
        ''' Trivia gameplay'''
        # Opens json file to load
        with open('Apprentice_TandemFor400_Data.json') as f:
            # Assigning json file to questions_and_answers as a list of dictionaries
            questions_and_answers = json.load(f)
            # shuffles questions in order to not keep getting the same 10 questions
            random.shuffle(questions_and_answers)
            # Iterates over first 10 questions
            for question in questions_and_answers[:10]:
                # prints question
                print(question['question'])
                # Combining correct and incorrect choices and assigning them to choices
                choices = question['incorrect'] + [question['correct']]
                self.display_answer_choices(choices)
                self.check_if_correct(question, choices)
            # Calls score rating in order to display appropriate message
            print(self.score_rating(self.correct_counter))
            input('Please press enter to continue...')
            # closes json file
            f.close()

    def score_rating(self, correct):
        '''Depending on the user score, it displays the appropriate message'''
        if not isinstance(correct, int):
            raise TypeError('The score has to be an integer between 0 and 10.')
        if correct < 0 or correct > 10:
            raise ValueError('The score has to be between 0 and 10.')
        if correct == 10:
            return f'Perfect, best trivia player to ever roam this world! Score: {correct}/10'
        elif 7 < correct < 10:
            return f'You did great! Score: {correct}/10'
        elif 5 < correct < 7:
            return f'Not bad, not great. Score: {correct}/10'
        elif 0 <= correct < 7:
            return f'Were you even trying? Score: {correct}/10'

    def display_answer_choices(self, choices):
        '''Displays answer choices in a random order'''
        # Shuffling in order to mask the correct answer, otherwise the correct answer would always be the last choice
        random.shuffle(choices)
        # Looping through choices to print
        for counter, answer in enumerate(choices):
            print(f'{counter + 1}. {answer}')

    def check_if_correct(self, question, choices):
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
                        self.correct_counter += 1
                        input('Press enter to continue...')
                        self.clear()
                        break
                    else:
                        print(
                            f'Wrong! The answer is {question["correct"]}')
                        input('Press enter to continue...')
                        self.clear()
                        break
                print(f'{choice} isn\'t an answer choice.')
            except:
                print(
                    'Incorrect input, enter the integer corresponding with your answer.')
