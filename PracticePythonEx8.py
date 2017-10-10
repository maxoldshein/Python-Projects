def rockPaperScissors():
    playAgain = True
    player1Wins = 0
    player2Wins = 0
    print("Welcome to the game Rock, Paper, Scissors!")
    print("The rules are simple! Here they are if you forgot:")
    print("1. Rock beats Scissors")
    print("2. Paper beats Rock")
    print("3. Scissors beat Paper")

    print(180 * "-")
    
    while(playAgain == True):
        userOneInput = raw_input("Player 1, please choose either rock, paper, or scissors: ")
        userTwoInput = raw_input("Player 2, please choose either rock, paper, or scissors: ")

        if (userOneInput == "rock" and userTwoInput == "rock"):
            print("Its a tie! Player 1 chose " + userOneInput + " and Player 2 chose " + userTwoInput + ", resulting in a tie!")
            userPlayAgain = raw_input("Would you like to play again? ")

        elif (userOneInput == "rock" and userTwoInput == "scissors"):
            print("Player 1 wins! Player 1 chose " + userOneInput + " and Player 2 chose " + userTwoInput + ", resulting in a win for Player 1!")
            player1Wins += 1
            userPlayAgain = raw_input("Would you like to play again? ")

        elif(userOneInput == "rock" and userTwoInput == "paper"):
            print("Player 2 wins! Player 1 chose " + userOneInput + " and Player 2 chose " + userTwoInput + ", resulting in a win for Player 2!")
            player2Wins += 1
            userPlayAgain = raw_input("Would you like to play again? ")
            
        elif (userOneInput == "scissors" and userTwoInput == "scissors"):
            print("Its a tie! Player 1 chose " + userOneInput + " and Player 2 chose " + userTwoInput + ", resulting in a tie!")
            userPlayAgain = raw_input("Would you like to play again? ")
            
        elif (userOneInput == "scissors" and userTwoInput == "paper"):
            print("Player 1 wins! Player 1 chose " + userOneInput + " and Player 2 chose " + userTwoInput + ", resulting in a win for Player 1!")
            player1Wins += 1
            userPlayAgain = raw_input("Would you like to play again? ")

        elif (userOneInput == "scissors" and userTwoInput == "rock"):
            print("Player 2 wins! Player 1 chose " + userOneInput + " and Player 2 chose " + userTwoInput + ", resulting in a win for Player 2!")
            player2Wins += 1
            userPlayAgain = raw_input("Would you like to play again? ")
            
        elif (userOneInput == "paper" and userTwoInput == "paper"):
            print("Its a tie! Player 1 chose " + userOneInput + " and Player 2 chose " + userTwoInput + ", resulting in a tie!")
            userPlayAgain = raw_input("Would you like to play again? ")

        elif (userOneInput == "paper" and userTwoInput == "rock"):
            print("Player 1 wins! Player 1 chose " + userOneInput + " and Player 2 chose " + userTwoInput + ", resulting in a win for Player 1!")
            player1Wins += 1
            userPlayAgain = raw_input("Would you like to play again? ")
            
        elif (userOneInput == "paper" and userTwoInput == "scissors"):
            print("Player 2 wins! Player 1 chose " + userOneInput + " and Player 2 chose " + userTwoInput + ", resulting in a win for Player 2!")
            player2Wins += 1
            userPlayAgain = raw_input("Would you like to play again? ")
            
        else:
            print("One player entered an illegal move or didn't enter a move at all, so the game couldn't be completed!")
            userPlayAgain = raw_input("Would you like to play again? ")

        if (userPlayAgain == "yes" or userPlayAgain == "Yes"):
            playAgain = True

        else:
            playAgain = False

    print(180 * "-")
    print("The score of the game was...")
    print("Player 1 Wins: " + str(player1Wins))
    print("Player 2 Wins: " + str(player2Wins))
    print(180 * "-")

rockPaperScissors()
