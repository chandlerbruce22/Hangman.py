import random
from wordList import wordList

def generate_word() :
    # If you don't want another file to deal with, just uncomment the following line and it'll work.
    # wordList = ['apple', 'banana', 'orange', 'pear', 'peach', 'watermelon']
    words = wordList
    return random.choice(words)

def play_again() :
    repeat = input("Do you want to play again? (yes/no): ")
    repeat = repeat.lower()

    if repeat == 'yes' :
        play_hangman()
    else :
        print('You are done playing.\n') 


def play_hangman() :
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    guessed_letters = []
    word = generate_word()
    attempts = 0
    guessed_word = False

    print('\nThis word has', len(word), 'letters.')
    print(len(word) * '_ ')

    while guessed_word == False :
        print('You have guessed ' + str(attempts) + ' times')
        guess = input('Please enter one letter or guess the word: ')

        if len(guess) == 1 :
            if guess not in alphabet :
                print('Please enter a letter from the alphabet.\n')
            elif guess in guessed_letters :
                print('You have already guess this letter.\n')
            elif guess not in word :
                print('That letter is not part of the word.\n')
                guessed_letters.append(guess)
                attempts += 1
            elif guess in word :
                print('Good job! That was correct!\n')
                guessed_letters.append(guess)
                attempts +=1
            else :
                print('Error. Please contact the programmer.\n')
        
        elif len(guess) == len(word) :
            if guess == word :
                print('Congrats, you have guessed the word.\n')
                attempts +=1
                guessed_word = True
                status = word
            else :
                print('Sorry, that is not the word.\n')
                attempts += 1
                guessed_word = False
       
        else :
            print('Your current character count does not equal the word you are trying to guess.')

        
        if guessed_word == False :
            status = ''
            for letter in word :
                if letter in guessed_letters:
                    status += letter
                else :
                    status += '_ '
            print(status)

        if status == word :
            print('The word was: ' + word + '. It took you ' + str(attempts) + ' guesses.\n')
            guessed_word = True
        else :
            guessed_word = False
    
    play_again()

play_hangman()


print('You finished! You are out of the game now.')
