import random
import os

words2 = 'Afghanistan, Kabul, Albania, Tirana, Algeria, Algiers, Andorra, Andorra la Vella, Angola, Luanda, Argentina, Buenos Aires, Armenia, Yerevan, Australia, Canberra, Austria, Vienna, Azerbaijan, Baku, Bahamas, Nassau, Bahrain, Manama, Bangladesh, Dhaka, Barbados, Bridgetown, Belarus, Minsk, Belgium, Brussels, Belize, Belmopan, Bhutan, Thimphu, Bolivia, La Paz,Bosnia and Herzegovina, Sarajevo, Botswana, Gaborone, Brazil, Brasilia, Brunei, Bandar Seri, Begawan, Bulgaria, Sofia'
wordsTest = 'Cocaine, Zuluzulu, Pokaz'
try:
     with open("countries-and-capitals.txt") as file_object: #wgrywanie pliku ze słowami
            words = file_object.read().split()
except FileNotFoundError:
     print('File not found. Load new dictionary')
     words = words2.split().lower()
#words = wordsTest.split().lower()
#grafika
HangMan_Pics1 = ['''
 +----+
      |
      |
      |
      |
      ===''','''
 +----+
 O    |
 |    |
      |
      |
      ===''', '''
 +----+
 O    |
/|    |
      |
      |
      ===''','''
 +----+
 O    |
/|\   |
      |
      |
      ===''','''
 +----+
 O    |
/|\   |
 |    |
      |
      === ''','''
 +----+
 O    |
/|\   |
 |    |
/     |
      ===''','''
 +----+
 O    |
/|\   |
 |    |
/ \   |
      ===
''']

HangMan_Pics2 = ['''
 +----+
 O    |
      |
      |
      |
      ===''','''
 +----+
 O    |
/     |
      |
      |
      ===''','''
 +----+
 O    |
/|    |
      |
      |
      ===''', '''
 +----+
 O    |
/|\   |
      |
      |
      ===''', '''
 +----+
 O    |
/|\   |
/ \   |
      |
      ===''']

HangMan_Pics3 = ['''
 +-----+
       |
       |
       |
       |
       ===''', '''
 +-----+
 O     |
       |
       |
       |
       ===''', '''
 +-----+
 O     |
/      |
       |
       |
       ===''','''
 +-----+
 O     |
/ \    |
       |
       |
       ===''', '''
 +-----+
 O     |
/ \    |
/      |
       |
       ===''', '''
 +-----+
 O     |
/ \    |
/ \    |
       |
       ==='''
]
 #losowanie wyrazu  
def getSecretWord(words):
      wordIndex=random.randint(0,len(words) - 1)
      secretWord=words[wordIndex]

      if secretWord == '|': #wyświetlanie tylko słów
            wordIndex = wordIndex +1
            secretWord = words[wordIndex]
      return(secretWord)

def dislayOnScreen(misses, correct, secretWord,hangmanGfx):
      os.system("cls")
      print(hangmanGfx[len(misses)])
      print()

      print('Missed letters:', end= ' ') #wyświetlanie obok siebie zamiast jedna pod drugą
      for letter in misses:
            print(letter, end= ' ')
      print()

      empty ='_'*len(secretWord)

      for i in range(len(secretWord)): #podmiana pustych pól, gdy zgadnięta litera
            if secretWord[i] in correct:
                  empty = empty[:i] + secretWord[i] + empty[i+1:]

      for letter in empty:
            print(letter, end=' ')
      print()

def getGuess(alreadyGuess):
      while True:
            print('Please, write your letter.')
            guess = input()
            guess = guess.lower()
            if len(guess) != 1:
                  print('Please enter a single letter')
            elif guess in alreadyGuess:
                  print('You have already guessed that letter. Choose again.')
            elif guess not in 'abcdefghijklmnopqrstuvwxyz':
                  print('Please enter a LETTER')
            else:
                  return guess

def gameEnd(): #funkcja zwraca True, jeżeli gracz chce grać dalej
      print('Do you want to play again? (yes or no)')
      return input().lower().startswith('y')
      
title = "H A N G M A N"
print(title.center(70))
misses =''
correct = ''
secretWord = getSecretWord(words)
gameOver = False
hangmanGFX = HangMan_Pics1
print('Please choose a level:\n\t1 - easy (default)\n\t2 - normal\n\t3 - hard\n\tor press ENTER to default')
choose = input()
level = False
while level == True:
      if choose == '1' or choose == '\r':
            hangmanGFX = HangMan_Pics1
            level = True
      elif choose =='2':
            hangmanGFX = HangMan_Pics2
            level = True
      elif choose == '3':
            hangmanGFX = HangMan_Pics3
            level = True
      else:
            print('Please choose a level!')
            level = False

gameDone = False

while True:
      dislayOnScreen(misses, correct, secretWord, hangmanGFX) #gracz wprowadza literę

      guess = getGuess(misses + correct)
      if guess in secretWord:

            correct = correct + guess
            foundWord = True
            for i in range(len(secretWord)):
                  if secretWord[i] not in correct:
                        foundWord = False
                        break
            if foundWord:
                  print(f'Yes! The secret word is: {secretWord}! You have won!')
                  gameDone = True
      else:
            misses = misses + guess

      if len(misses) == len(hangmanGFX) - 1:
            dislayOnScreen(misses, correct, secretWord, hangmanGFX)
            print(f'You have run out of guesses!\nAfter {str(len(misses))} misses guessed and {str(len(correct))} correct guesses. The secret word is: {secretWord}')
            gameDone = True

      if gameDone:
            if gameEnd():
                  misses = ''
                  correct = ''
                  gameDone = False
                  secretWord = getSecretWord(words)
            else:
                  break      