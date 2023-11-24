import os 
import random
from termcolor import colored
LINE = '-' * 70


def clear_screen():
    os.system('cls')


def welcome_message():
    print()
    print(LINE , end= ' ')
    print(colored("<<< WELCOME TO THE GUESS GAME >>>" , 'yellow' , attrs=['bold']) , end= ' ')
    print(LINE)
    print()
    print(f'List of the words: {list_of_the_words}')
    print()
    print(LINE)
    print()


def get_input():
    while True:
        user_input = input('Enter your guess from list of the words: ')
        if user_input.isalpha():
            return user_input.title()
        else:
            print()
            print('Invalid input. Your guess should be a word.')
            print('Please try again.')
            print(LINE)


def get_input_from_list(words):
    user_input = get_input()
    while user_input not in words:
        print()
        print(f'You have to guess a word from the given word list: {list_of_the_words}')
        print('Please enter a correct word.')
        print(LINE)
        user_input = get_input()
    return user_input.title()


def number_of_rounds_from_user():
    while True:
        user_input = input('Enter number of the rounds: ')
        if not user_input.isdigit() or int(user_input) <= 0:
            print()
            print('Number of the rounds should be "POSITIVE NUMBER".')
            print('Please try again.')
            print(LINE)
        else:
            return int(user_input)
            
                
def do_you_want_game_again():
    while True:
        user_input = input('Do you want to game again?(y/n): ')
        if user_input.lower() in ['y' , 'n']:
            if user_input.lower() == 'y':
                run_game(list_of_the_words)
            else:
                print(LINE)
                print()
                print(colored('<<< END OF THE GAME >>>' , 'green'))
                print(colored('<<< THANK YOU FOR CHOOSING US >>>' , 'white'))
                print(colored('<<< GOOD LUCK >>>' , 'red'))
                print()
                return
        else:
            print()
            print('Invalid input. Please enter y = (yes) or n = (no)')
            print(LINE)


def run_game(words):
    clear_screen()
    welcome_message()
    number_of_rounds = number_of_rounds_from_user()
    print()
    correct_word = random.choice(list_of_the_words)

    for rounds in range(number_of_rounds):
        user_input = get_input_from_list(words)
        if user_input == correct_word:
            print()
            print(LINE)
            print('Your guess is right.')
            print()
            print(colored('YOU WON!' , 'green' , attrs=['bold']))
            print()
            return
        else:
            if (number_of_rounds - 1 - rounds == 0):
                print()
                print('Your guess is wrong.')
                print(LINE)
                break
            print()
            print('Your guess is wrong!')
            print()
            print(f'Please enter again. Number of the rounds left: {number_of_rounds - 1 - rounds}')
            print(LINE)
    
    print()
    print(colored('YOU LOST!' , 'red'))
    print()
    print(colored(f'The correct answer is {correct_word}.' , 'green'))
    print(LINE)


list_of_the_words = ['Neda','Zhina','Nika','Navid','Sarina','Hadis','Khodanoor','Kian']
run_game(list_of_the_words)
do_you_want_game_again()
