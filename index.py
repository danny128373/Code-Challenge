import os
from play_trivia import play_trivia


def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Prints title and options for user
    print(
        "\u001b[47m\u001b[30;1m+-++-++-++-++-++-++-++-++-++-")
    print("+ T A N D E M   T R I V I A +")
    print("+-++-++-++-++-++-++-++-++-++-\u001b[0m\n")
    print("1. Are you ready to start?")
    print("2. Exit")


def main_menu():
    build_menu()
    # Assigns user input to choice
    choice = input(">> ")
    # Starts trivia game
    if choice == "1":
        play_trivia()
    # If user didn't input 1 or 2, it calls this function again
    if choice != "2":
        main_menu()


main_menu()
