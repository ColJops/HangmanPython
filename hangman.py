from email import message
import random

import os

# 1
HANGMAN = (
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
---------- """, """
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
---------- """, """
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
---------- """, """
 ------
 |    |
 |    O
 |   -+-
 |  /
 |   
 |   
 |   
 |   
---------- """, """
 ------
 |    |
 |    O
 |   -+-
 |  / |
 |    |
 |   
 |   
 |   
---------- """, """
 ------
 |    |
 |    O
 |   -+-
 |  / | /
 |    |
 |   
 |   
 |   
---------- """, """
 ------
 |    |
 |    O
 |   -+-
 |  / | /
 |    |
 |   / 
 |   | 
 |   
---------- """, """
 ------
 |    |
 |    O
 |   -+-
 |  / | /
 |    |
 |   / /
 |   | |
 |  
---------- """)
HANGMAN2 = (
    '''
------
|    |
|
|
|
|
-------- ''', '''
------
|    |
|    O
|
|
|
-------- ''', '''
--------
|      |
|      O
|     /
|
|
--------- ''', '''
------
|    |
|    O
|   /|
|
|
-------- ''', '''
------
|    |
|    O
|   /|/
|
|
--------- ''', '''
------
|    |
|    O
|   /|/
|   /
|
--------- ''', '''
------
|    |
|    O
|   /|/
|   / /
---------- '''
)
HANGMAN3 = (
    '''
-----
|
|
|
------- ''', '''
-----
|   O
|
|
------- ''', '''
-----
|   O
|  /|
|
-------- ''', '''
-----
|   O
|  /|/
|
------- ''', '''
-----
|   O
|  /|/
|  /
------- ''', '''
-----
|   O
|  /|/
|  / /
-------- '''
)

# 2

MAX_WRONG = len(HANGMAN) - 1

# logo
# print('''
# ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
# ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
# ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
# ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
# ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
# ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
# ''')

#  3

wordsSecondDictionary = 'Afghanistan Kabul Albania Tirana Algeria Algiers Andorra Andorra la Vella Angola Luanda Argentina Buenos Aires Armenia Yerevan Australia Canberra Austria Vienna Azerbaijan Baku Bahamas Nassau Bahrain Manama Bangladesh Dhaka Barbados Bridgetown Belarus Minsk Belgium Brussels Belize Belmopan Bhutan Thimphu Bolivia La Paz Bosnia and Herzegovina Sarajevo Botswana Gaborone Brazil Brasilia Brunei Bandar Seri Begawan Bulgaria Sofia'

try:
    with open("countries-and-capitals1.txt") as file_object:  # wgrywanie pliku ze słowami
        for line in file_object:
            words = file_object.read()
except FileNotFoundError:
    print('File not found. Load new dictionary')
    words = wordsSecondDictionary.split()


word = random.choice(words)
if word == "|":
    word = random.choice(words)

wordToGuess = word.lower()
so_far = "_" * len(wordToGuess)  # one dash for each letter in word to be guessed

wrong = 0  # counter to keep track of number of wrong guesses

used = []  # list to keep track of letters already guessed
os.system('cls')
# logo
print('''
 ██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
 ██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
 ███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
 ██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
 ██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║ 
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
 ''')

print("Welcome to Hangman. Good luck!")

hangmanGFX = HANGMAN
print('Please choose a level:\n\t1 - easy (default)\n\t2 - normal\n\t3 - hard\n\tor press ENTER to default')
choice = input()
level = False
while level == True:
    if choice == '1' or choice == '\r':
        hangmanGFX = HANGMAN
        level = True
    elif choice == '2':
        hangmanGFX = HANGMAN2
        level = True
    elif choice == '3':
        hangmanGFX = HANGMAN3
        level = True
    else:
        print('Please choose a level!')
        level = False

while wrong < MAX_WRONG and so_far != wordToGuess:
    os.system("cls")
    print(HANGMAN[wrong])
    print(f"\nYou've used the following letters:\n", used)
    print("\nSo far, you have guessed:\t", so_far)

    guess = input("Enter your guess by typing one letter or write 'quit' to end the game:\t")

    while guess in used:
        print("You already guessed the letter:\t", guess)
        guess = input("Guess again:\t")

    used.append(guess)

    if guess in wordToGuess:
        print("The letter, ", guess, "is in the word")

        # create a new so_far to include guess
        new = ""

        for i in range(len(wordToGuess)):
            if guess == wordToGuess[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    elif guess == "quit":
        print('Good bya. See you soon ;)')
        guess = exit(0)

    else:
        print("\nSorry,", guess, "isn't in word")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("I would tell you, that you've been hanged. \n\
But you're dead, so.......RIP?")
    message = "The secret word is: " + wordToGuess
    print(message)

else:
    print("\nYou guessed it!")


