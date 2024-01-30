# Find the next / previous letter game
import random

english_alphabets = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f', 7 : 'g', 8 : 'h', 9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o', 16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't', 21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y', 26 : 'z'}
user_input = input("Let's start the game! press 'S' to Start or 'Q' to quit: ")
score = 0
no_of_question = 0
list_choice = ['Next','Previous']

if user_input == 'Q' or user_input == 'q':
    print('Okay, we play another time!')
else:
    while user_input != '':
        choice = random.choice(list_choice)
        random_int = random.randint(2,25)
        if choice == 'Next':
            print(f'Find the "{choice}" letter of "{english_alphabets[random_int]}"')
            no_of_question += 1
            user_input = input('Enter the "next" letter in lowercase: ')
            if user_input == english_alphabets[random_int + 1]:
                score += 1
            elif user_input == '':
                print('Empty String!, Game Ends!!!')
            else:
                score -= 1
                print(f'Oops! Wrong Answer! The correct answer is "{english_alphabets[random_int + 1]}"')
        else:
            print(f'Find the "{choice}" letter of "{english_alphabets[random_int]}"')
            no_of_question += 1
            user_input = input('Enter the "previous" letter in lowercase: ')
            if user_input == english_alphabets[random_int - 1]:
                score += 1
            elif user_input == '':
                print('Empty String!, Game Ends!!!')
            else:
                score -= 1
                print(f'Oops! Wrong Answer! The correct answer is "{english_alphabets[random_int - 1]}"')
    print(f'Out of {no_of_question - 1} you scored {score}')
