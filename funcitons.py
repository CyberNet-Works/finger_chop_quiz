def quit(): #quit function will display the message "Press Enter to exit." and then exit the game when the user presses enter.
    input("Press Enter to exit.")

def game_over(): #The game is over and the user's score is displayed.
    if fingers_start == 0:
        percentage = 0
    else:
        percentage = fingers_lost / fingers_start
    print("\n\n\nCongratulations, " + username + ", you have completed the Tiger Hardwood Software quiz!")
    print"You scored " + str(score) + " out of " + str(question_number) + " questions.")
    print("Y(ou started with " + str(fingers_start) + " fingers.")
    print("You lost " + str(fingers_lost) + " fingers in the process.  That's " + str(percentage) + " of your fingers! Ouch")
    print("You have " + str(fingers_left) + " fingers left:\n")
    print("Thank you for playing! "+ username + "!\n\n\n\n\n\n")
    print("Game Over")
    quit()

    