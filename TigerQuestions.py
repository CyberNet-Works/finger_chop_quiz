#initialize some stuff
from datetime import datetime
now = datetime.now()
print(str(now))
print("...initializing...")
print(str(now) + "\n Tiger Hardwood Software Quiz initialized")
    
#The game will then ask the user a series of questions about Tiger Hardwood Software
#Game starts by selecting username, user gets a guest username if they don't enter one.
#If the user enters a username, the game will welcome them with their username
print("\n\n\n\n")
username = input("Select a username: ")
if username == "":
      username = "Tiger"
else:
      username = username

question_number = 0
fingers = 0
score = 0

#wronganswer function will add 1 to the finger variable and print the wrong answer message,
#then display the current score and how many fingers they lost..
      
def wronganswer():
    global fingers  # Declare fingers as a global variable
    fingers +=1
    print("Unfortunately, you are incorrect.  Please chop off finger " + str(fingers) + ".\n")
    print("Score: " + str(score) + "\n")
    print("Fingers: " + str(fingers) + "\n")

#rightanswer function will add 1 to the score variable and print the correct answer message
#then display the current score and how many fingers they lost.
def rightanswer():
    global score  # Declare score as a global variable
    score += 1
    print("\n\n\n...\n\n\nCongratulations, you are correct! ")
    print("Score: " + str(score) + "  |  Fingers: " + str(fingers) + "\n")

#badinput function will display the message "Please enter True or False.  Press enter to try the same question again."
def badinput():
    print("Please enter True or False.  Press enter to try the same question again.")
    input()

#quit function will display the message "Press Enter to exit." and then exit the game when the user presses enter.
def quit():
    input("Press Enter to exit.")


def askquestion():
    global question_number  # Declare question_number as a global variable
    question_number += 1
    print("\n\n\nOkay " + username + ", here is question number " + str(question_number) + ".\n")

#The question engine will shuffle the questions, and ask them in a random order.
def question_engine()
     
#Welcome and select topics for quiz
print("Welcome to Tiger Hardwood Software, " + username ")
print("Please select the topics you would like to quiz on:\n")



#The game begins here with question 1.
askquestion()
print("Tiger Hardwood Software is a company that sells software to hardwood companies.")
answer1 = input("True or False: ")
if answer1.lower() == "true":
    wronganswer()
elif answer1.lower() == "false":
    rightanswer()
else:
    badinput()


#The game continues to question 2.
askquestion()
print("Tiger Hardwood Software is a company that sells hardwood to software companies.\n")
answer2 = input("True or False: ")
if answer2.lower() == "true":
    wronganswer()
elif answer2.lower() == "false":
    rightanswer()
else:
    print("Please enter True or False.")

#The game is over and the user's score is displayed.
print("\n\n\nCongratulations, " + username + ", you have completed the Tiger Hardwood Software quiz!")
print("You scored " + str(score) + " out of " + str(question_number) + " questions.")
print("You lost " + str(fingers) + " fingers in the process.")
print("Thank you for playing! "+ username + "!\n\n\n\n\n\n")
print("Game Over")
quit()