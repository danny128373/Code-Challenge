import os
from play_trivia import play_trivia


def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        "\u001b[47m\u001b[30;1m+-++-++-++-++-++-++-++-++-++-")
    print("+ T A M D E M   T R I V I A +")
    print("+-++-++-++-++-++-++-++-++-++-\u001b[0m\n")
    print("1. Are you ready to start?")
    print("2. Exit")


def main_menu():
    build_menu()
    choice = input(">> ")

    if choice == "1":
        play_trivia()


main_menu()
