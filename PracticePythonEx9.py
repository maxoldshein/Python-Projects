import random

def guessingGame():
    randomNumber = random.randrange(1, 10)
    playAgain = True

    while (playAgain == True):
        guessRange = False
        numberUserGuess = 0

        while (guessRange == False):
            guessNumber = 0
            userGuess = raw_input("Please enter a number between 1 and 9: ")

            if (userGuess == "exit"):
                playAgain = False
                guessRange = True
                print("Thanks for playing!")
                print("You used " + str(guessNumber) + " guess(es) before you threw in the towel!")
                response = raw_input("Would you like to play again? ")

                if (response.upper() == "YES"):
                    playAgain = True
                else:
                    playAgain = False
                
                break
                
            numberUserGuess = int(userGuess)
            
            if (numberUserGuess >= 1 and numberUserGuess <= 9):
                guessRange = True
            else:
                guessRange == False
                print("Please enter a number between 1 and 9!")
        if (playAgain == False):
            break
        elif (numberUserGuess == randomNumber):
            guessNumber += 1
            playAgain = False
            print("You got it! Way to go! It took you " + str(guessNumber) + " guesses to get the right answer!")

            response = raw_input("Would you like to play again? ")

            if (response.upper() == "YES"):
                playAgain = True
            else:
                playAgain = False
        elif (numberUserGuess > randomNumber):
            guessNumber += 1
            playAgain = True
            print("Your guess was a bit high... Why don't you guess a little lower?")
        elif (numberUserGuess < randomNumber):
            guessNumber += 1
            playAgain = True
            print("Your guess was a bit low... Why don't you guess a little higher?")
            
guessingGame()
    
