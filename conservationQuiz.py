import csv
import random

# Variables - should find out the way to do this correctly
gameMode = 0
correctAnswerCount = 0
incorrectAnswerCount = 0
totalAnswerCount = 0
roundsToPlay = 3

# Set path to CSV file
csv_file = 'speciesData.csv'

# Read the CSV file
with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    fullSpeciesData = list(reader)

def main(roundsToPlay, gameMode, correctAnswerCount, incorrectAnswerCount, totalAnswerCount):
    # Prompt for game mode if it hasn't been selected by the user
    if gameMode == 0:
        setGameMode(roundsToPlay, gameMode, correctAnswerCount, incorrectAnswerCount, totalAnswerCount)

    # Select 4 random rows from fullSpeciesData
    possibleAnswers = random.sample(fullSpeciesData, 4)

    # Assign each row to an answer for scientificMode
    correctAnswer = possibleAnswers[0]
    incorrectAnswer1 = possibleAnswers[1]
    incorrectAnswer2 = possibleAnswers[2]
    incorrectAnswer3 = possibleAnswers[3]

    # Set, shuffle, and output answer list for scientific mode
    if gameMode == "scientificMode":
        print(f"What is the scientific name for the species " + correctAnswer[1] + ":")
        correct = correctAnswer[2]
        answerList = [incorrectAnswer1[2], incorrectAnswer2[2], incorrectAnswer3[2], correctAnswer[2]]
        random.shuffle(answerList)

    # Set, shuffle, and output answer list for common mode
    elif gameMode == "commonMode":
        print(f"What is the common name for the species " + correctAnswer[2] + " species:")
        correct = correctAnswer[1]
        answerList = [incorrectAnswer1[1], incorrectAnswer2[1], incorrectAnswer3[1], correctAnswer[1]]
        random.shuffle(answerList)

    # Set, shuffle, and output answer list for banding code mode
    elif gameMode == "bandingCodeMode":
        print(f"What is the banding code for the " + correctAnswer[1] + " species:")
        correct = correctAnswer[0]
        answerList = [incorrectAnswer1[0], incorrectAnswer2[0], incorrectAnswer3[0], correctAnswer[0]]
        random.shuffle(answerList)

    # Set, shuffle, and output answer list for banding species mode
    elif gameMode == "bandingSpeciesMode":
        print(f"What is the species name for the " + correctAnswer[0] + " banding code:")
        correct = correctAnswer[1]
        answerList = [incorrectAnswer1[1], incorrectAnswer2[1], incorrectAnswer3[1], correctAnswer[1]]
        random.shuffle(answerList)

    # Display answers and call checkAnswer
    print(f"1: " + answerList[0] +
          "\n2: " + answerList[1] +
          "\n3: " + answerList[2] +
          "\n4: " + answerList[3])

    checkAnswer(correct, gameMode, answerList, correctAnswerCount, incorrectAnswerCount, totalAnswerCount)

def checkAnswer(correct, gameMode, answerList, correctAnswerCount, incorrectAnswerCount, totalAnswerCount):
    # Ask for answer
    answer = input("> ")
    if correct == answerList[int(answer) - 1]:
        # Output for correct answer and add one to correctAnswerCount
        print("\n***** CORRECT! ******")
        correctAnswerCount += 1
    else:
        # Output for incorrect answer and add one to incorrectAnswerCount
        print(f"\n***** Sorry, that's incorrect. The correct answer was: " + str(correct) + " ******")
        incorrectAnswerCount += 1

    # Increase total answer count
    totalAnswerCount += 1

    if totalAnswerCount == roundsToPlay:
        # Report score and ask to play again if round to play has been reached
        print("Your final score is:")
        print(f"Correct answers: " + str(correctAnswerCount))
        print(f"Incorrect answers: " + str(incorrectAnswerCount))
        playAgain(roundsToPlay, gameMode, correctAnswerCount, incorrectAnswerCount, totalAnswerCount)
    else:
        # Report score and start next round
        print("Your current score is:")
        print(f"Correct answers: " + str(correctAnswerCount))
        print(f"Incorrect answers: " + str(incorrectAnswerCount) + "\n\n")
        main(roundsToPlay, gameMode, correctAnswerCount, incorrectAnswerCount, totalAnswerCount)

def setGameMode(roundsToPlay, gameMode, correctAnswerCount, incorrectAnswerCount, totalAnswerCount):
    # Prompt the player for the game mode they would like to play
    print("\nWhat mode would you like to play:")
    print("1) Guess the scientific name of a species")
    print("2) Guess the common name of a species")
    print("3) Guess the banding code of a species")
    print("4) Guess the species of a banding code")
    gameModeSelect = int(input("> "))
    # Set game mode variable based on player selection or prompt for a valid selection
    if gameModeSelect == 1:
        gameMode = "scientificMode"
    elif gameModeSelect == 2:
        gameMode = "commonMode"
    elif gameModeSelect == 3:
        gameMode = "bandingCodeMode"
    elif gameModeSelect == 4:
        gameMode = "bandingSpeciesMode"
    else:
        print("Please enter a valid selection (1, 2, 3, or 4)")
        setGameMode(roundsToPlay, gameMode, correctAnswerCount, incorrectAnswerCount, totalAnswerCount)

    # Call main game loop
    main(roundsToPlay, gameMode, correctAnswerCount, incorrectAnswerCount, totalAnswerCount)

def playAgain(roundsToPlay, gameMode, correctAnswerCount, incorrectAnswerCount, totalAnswerCount):
    # Prompt the player to play again
    print("\nWould you like to play again?\n1: Yes\n2: Change game mode\n3: Exit\n")
    playAgainSelection = int(input("> "))
    if playAgainSelection == 1:
        # Reset the total answer count so next round will play the correct number of rounds and call main loop
        totalAnswerCount = 0
        # Call main game loop
        main(roundsToPlay, gameMode, correctAnswerCount, incorrectAnswerCount, totalAnswerCount)

    elif playAgainSelection == 2:
        # Reset the total answer count so next round will play the correct number of rounds and call main loop
        totalAnswerCount = 0
        # Prompt for new game mode
        setGameMode(roundsToPlay, gameMode, correctAnswerCount, incorrectAnswerCount, totalAnswerCount)

    elif playAgainSelection == 3:
        # Exit game
        print("Thanks for playing the Conservation Quiz!")
        quit()

if __name__ == '__main__':
    main(roundsToPlay, gameMode, correctAnswerCount, incorrectAnswerCount, totalAnswerCount)
