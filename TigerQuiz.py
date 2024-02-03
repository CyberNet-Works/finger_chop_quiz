#initialize some stuff
import sys
from datetime import datetime
now = datetime.now()
topics = {"animals":"animals.json"}
question_number = 0
fingers_lost = 0
fingers_start = 0
score = 0
print(str(now))
print("...initializing...")
print(str(now) + "\n Tiger Hardwood Software Quiz initialized")

#quit function will display the message "Press Enter to exit." and then exit the game when the user presses enter.
def quit():
    input("Press Enter to exit.")
    sys.exit()


#introduction to the game
def startgame():
    print("Welcome to Tiger Hardwood Software, " + username)
    print("Please select topics to quiz on:\n")
    input(list(topics.keys()))

#
def askquestion():
    global question_number  # Declare question_number as a global variable
    question_number += 1
    print("\n\n\nOkay " + username + ", here is question number " + str(question_number) + ".\n")

#wronganswer function will add 1 to the finger variable and print the wrong answer message,
#then display the current score and how many fingers they lost..

def wronganswer():
    global fingers_lost  # Declare fingers as a global variable
    fingers_lost +=1
    fingers_left -=1
    print("Unfortunately, you are incorrect.  Please chop off finger " + str(fingers_lost) + ".\n")
    print("Score: " + str(score) + "\n")
    print("fingers lost: " + str(fingers_lost) + "\n")
    print("fingers left: " + str(fingers_left) + "\n")

#rightanswer function will add 1 to the score variable and print the correct answer message
#then display the current score and how many fingers they lost.
def rightanswer():
    global score  # Declare score as a global variable
    score += 1
    print("\n\n\n...\n\n\nCongratulations, you are correct! ")
    print("Score: " + str(score) + "  |  fingers_lost: " + str(fingers_lost) + "\n")
    print("fingers left: " + str(fingers_left) + "\n")

#Game starts by selecting username, user gets a guest username if they don't enter one.
#If the user enters a username, the game will welcome them with their username
print("\n\n\n\n")
username = input("Select a username: ")
username = username if username else "Tiger"

fingers_left = int(input(("OK " + username + ", how many fingers do you have? "))) #The game inquires about users fingers.

print("Terms and Conditions: You must be honest, or we will find you and cut off your fingers.  Do you accept? ")
accept_terms = input("Type YES if you accept our terms and conditions: \n") #The user must accept terms and conditions or quit.
if accept_terms.lower == "yes":
    startgame()
else:
    quit()

#The game begins here with question 1.
askquestion()

#GAME SECTION 
#This section of the game needs to pull questions from the chosen json file and display them to the user.  If they get them wrong, wronganswer() if they get them right, rightanswer()  bad input, try again

print("Tiger Hardwood Software is a company that sells software to hardwood companies.")
answer1 = input("True or False: ")
if answer1.lower() == "true":
    wronganswer()
elif answer1.lower() == "false":
    rightanswer()
else:
    badinput()


#The game is over and the user's score is displayed.
def game_over():
    if fingers_start == 0:
        percentage = 0
    else:
        percentage = fingers_lost / fingers_start
    print("\n\n\nCongratulations, " + username + ", you have completed the Tiger Hardwood Software quiz!")
    print("You scored " + str(score) + " out of " + str(question_number) + " questions.")
    print("You started with " + str(fingers_start) + " fingers.")
    print("You lost " + str(fingers_lost) + " fingers in the process.  That's " + str(percentage) + " of your fingers! Ouch")
    print("You have " + str(fingers_left) + " fingers left:\n")
    print("Thank you for playing! "+ username + "!\n\n\n\n\n\n")
    print("Game Over")
    quit()
