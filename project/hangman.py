##Project by GONZALEZ Victor - Epsi FR Toulouse | B3 Devops - 18/12


## Import Librairies

import random
from pathlib import Path
import string

## Declaration of the variables

listOfLetters = string.ascii_letters
p = Path("project/words.txt")
f = open(p, "r")
wordList = f.read().splitlines()
wordToGuess, wordLength = '', ''
errors, correct, maxError = 0, 0, 6
wordToGuessArray, wordToGuessHiddenArray, letterPicked = [], [], []


## Functions declarations

## Decide if the player lost by reaching 6 errors of if he won by guessing all the letters. Continue the game otherwise.
def isVictoryOrLose():
    end = False
    if correct == wordLength:
        print("\nVictory, you guessed all the letters !")
        end = True
    elif errors == maxError:
        print("\nDefeat, you reached 6 errors before finding all the letters !")
        end = True
    if end :
        print("The word to guess was : ", wordToGuess, "\nEnd of the game, thank you for playing !")
    else :
        startTurn()

## Verify if the letter is in the word. Add an error if not.
def guessLetter(letter):
    global errors, correct, letterPicked
    right = False
    for j in range(wordLength):
        if letter == wordToGuessArray[j]:
            wordToGuessHiddenArray[j] = letter
            correct += 1
            right = True
    if right == False:
        errors += 1
        print('Only ', maxError - errors, ' errors left')
    letterPicked.append(letter)
    isVictoryOrLose()
    
## Ask the player to write a letter, and then verify if it's a single valid letter that have not been tried yet.
def checkLetter():
    letter = input(">>> Choose your letter : ")
    if letter not in listOfLetters :
        print("Please, type a single valid letter\n")
        checkLetter()
    elif letter.upper() in letterPicked :
        print("Pick a letter you haven't already tried\n")
        checkLetter()
    elif letter == "":
        print("Write a letter before pressing Enter\n")
        checkLetter()
    else :
        guessLetter(letter.upper())
        

## Start the turn by displaying the letters found and an underscore for any letter not found yet.
def startTurn():
    wordCompletion = ''
    for comp in wordToGuessHiddenArray:
        wordCompletion += comp + ' '
    print("\n", wordCompletion, "\n")
    checkLetter()


## Initialize values.
## wordToGuess : word picked randomly to guess.
## wordToGuessArray : same word but with each letter splitted in a list.
## wordToGuessHiddenArray : once again but this time with a _ instead of the letter if the player haven't guessed it yet.
## wordLength : This is pretty explicit

def init():
    global wordToGuess, wordToGuessArray, wordToGuessHiddenArray, wordLength
    print("\n>>> Welcome to Hangman ! \nGuess the word by typing all letter it contains. \nTry 6 wrong letters and you'll loose ! \nGood luck ! \n")
    wordToGuess = random.choice(wordList)
    wordToGuessArray = list(wordToGuess)
    for _ in range(len(wordToGuessArray)):
         wordToGuessHiddenArray.append("_")     
    wordLength = len(wordToGuess)
    startTurn()

## Call the Init function to start the game.
init()