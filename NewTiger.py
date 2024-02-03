#initialize some stuff
import builtins
import random
import sys
import time
from datetime import datetime
import json
now = datetime.now()

#type slowly
def type_text_slowly(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

# Custom print_slowly function
def print_slowly(*args, **kwargs):
    for arg in args:
        if isinstance(arg, str):
            type_text_slowly(arg)
        else:
            type_text_slowly(str(arg))
    print(**kwargs)

# Temporarily store the original print function
original_print = builtins.print

# Override the built-in print function
builtins.print = print_slowly


#more initialization
topics = {"animals": "animals.json"}
question_number = 0
fingers_lost = 0
fingers_left = 0
score = 0

# 20 alternative responses for invalid input:
alternative_responses = [
    "Terms and Conditions: Are you ready to play 'Finger Jenga' with destiny? Type YES to get started!",
    "Terms and Conditions: By playing this game, you agree to our radical digit-al transformation. Type YES to give us the green light!",
    "Terms and Conditions: Do you promise not to point fingers, especially after we've chopped some off? Type YES to show you're on board!",
    "Terms and Conditions: Brace yourself for the high-five of fate! Type YES to embark on this wild hand-chopping adventure!",
    "Terms and Conditions: Welcome to 'Chop or Not' - where fingers are at stake and laughter is our only currency. Type YES if you're ready for the show!",
    "Terms and Conditions: Are you prepared to give a hand (or a finger) to the cause of humor? Type YES to join our fingerless fellowship!",
    "Terms and Conditions: This game is like 'Simon says,' but Simon is a bit scissor-happy. Type YES if you're up for the challenge!",
    "Terms and Conditions: To play this game, you must be all in—literally! Type YES to bet your fingers on the line!",
    "Terms and Conditions: Warning: This game may cause uncontrollable laughter and temporary finger detachment. Type YES to roll the dice!",
    "Terms and Conditions: Ready for a finger-lickin' good time? Type YES to dip your digits into the wacky world of our game!",
    "Terms and Conditions: By typing YES, you agree to the 'Lose a Finger, Gain a Laugh' policy. Welcome aboard!",
    "Terms and Conditions: Hold on to your digits! Type YES to enter the finger-flipping dimension of our hilarious game.",
    "Terms and Conditions: This game is so cutting-edge; you might lose a few edges! Type YES to embrace the slice of life!",
    "Terms and Conditions: Think of this as a finger-painting class—minus the paint and, well, some fingers. Type YES if you're an art enthusiast!",
    "Terms and Conditions: Do you solemnly swear to have a finger-lickin' good time? Type YES and let the finger roulette begin!",
    "Terms and Conditions: To proceed, please give us the finger... metaphorically speaking! Type YES if you're feeling rebellious!",
    "Terms and Conditions: Welcome to the 'Chopportunity' of a lifetime! Type YES to unlock the finger-chopping fun!",
    "Terms and Conditions: Caution: This game may cause excessive laughter and temporary finger aerodynamics. Type YES if you're up for the challenge!",
    "Terms and Conditions: Prepare to play 'Twister,' but instead of limbs, we're twirling fingers. Type YES if you're ready to spin!",
    "Terms and Conditions: Are you brave enough to enter the finger-lopping carnival of chuckles? Type YES to join the circus!",
]

print(str(now))
print("...initializing...")
print(str(now) + "\n Tiger Hardwood Software Quiz initialized")


# quit function will display the message "Press Enter to exit."
# and then exit the game when the user presses enter.
def quit_game():
    input("Press Enter to exit.")
    sys.exit()

# introduction to the game
# this is really select topics function but we will deal with that later
def startgame():
    print("\n\n\nWelcome to Tiger Hardwood Software, " + username)
    
    while True:
        for topic in topics:
            print(topic)
        
        selected_topics = input("Please select from the topics above that you would like to be quizzed on: ")
        
        if selected_topics.lower() in topics:
            # You can process the selected_topics variable as needed for your game logic
            print("Great! You selected:", selected_topics)
            break  # Break out of the loop if a valid topic is selected
        else:
            print("Invalid topic. Please select from the provided list.")

def askquestion():
    global question_number  # Declare question_number as a global variable
    question_number += 1
    print("\n\n\nOkay " + username + ", here is question number " + str(question_number) + ".\n")


# badinput function will display the message "Please enter True or False.
# Press enter to try the same question again."
def badinput():
    print("Please enter True or False.  Press enter to try the same question again.")
    input()


# wronganswer function will add 1 to the finger variable and print the wrong answer message,
# then display the current score and how many fingers they lost.
def wronganswer():
    global fingers_lost, fingers_left, score  # Declare all variables as global
    fingers_lost += 1
    if fingers_left > 0:
        fingers_left -= 1
        print("Unfortunately, you are incorrect.  Please chop off finger " + str(fingers_lost) + ".\n")
        print("Score: " + str(score) + "\n")
        print("fingers lost: " + str(fingers_lost) + "\n")
        print("fingers left: " + str(fingers_left) + "\n")
    else:
        game_over()  # Trigger game over if fingers_left is less than zero

def rightanswer():
    global score  # Declare score as a global variable
    score += 1
    print("\n\n\n...\n\n\nCongratulations, you are correct! ")
    print("Score: " + str(score) + "  |  fingers_lost: " + str(fingers_lost) + "\n")
    print("fingers left: " + str(fingers_left) + "\n")


# Game starts by selecting a username;
# the user gets a guest username if they don't enter one.
# If the user enters a username, the game will welcome them with their username.
print("\n\n\n\n")
username = input("Select a username: ")
username = username.strip() if username else "Tiger"

# The game inquires about the user's fingers.
while True:
    try:
        start_fingers = int(input("OK " + username + ", how many fingers do you have? "))
        fingers_left = start_fingers
        if start_fingers == 10:
            print("Okay, let's see if we can remedy that!")
        else:
            print("Huh, strange. Let's continue.")
        break  # Break out of the loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a number.")


# The user must accept terms and conditions.
while True:
    print("\nTerms and Conditions: You must be honest, or we will find you and cut off your fingers. Do you accept?")
    try:
        accept_terms = input("Type YES if you accept our terms and conditions: ").strip().lower()
        if accept_terms == "yes":
            break  # Exit the loop if the user enters "YES"
        else:
            print("To continue, you MUST ENTER YES.")
            # Select a random alternative response for invalid input
            random_response = random.choice(alternative_responses)
            print(random_response)
    except ValueError:
        print("Invalid input. To continue, you MUST ENTER YES.")

# Call the startgame() function after the loop
startgame()

# The game begins here with question 1.
askquestion()
print("Tiger Hardwood Software is a company that sells software to hardwood companies.")
answer1 = input("True or False: ")
if answer1.lower() == "true":
    wronganswer()
elif answer1.lower() == "false":
    rightanswer()
else:
    badinput()

# The game continues to question 2.
askquestion()
print("Tiger Hardwood Software is a company that sells hardwood to software companies.\n")
answer2 = input("True or False: ")
if answer2.lower() == "true":
    wronganswer()
elif answer2.lower() == "false":
    rightanswer()
else:
    print("Please enter True or False.")

# The game is over, and the user's score is displayed.
def game_over():
    if fingers_lost == 0:
        percentage = 0
    else:
        percentage = fingers_lost / (fingers_lost + fingers_left)
    print("\n\n\nCongratulations, " + username + ", you have completed the Tiger Hardwood Software quiz!")
    print("You scored " + str(score) + " out of " + str(question_number) + " questions.")
    print("You started with " + str(start_fingers) + " fingers.")
    print("You lost " + str(fingers_lost) + " fingers in the process.  That's {:.2%} of your fingers! Ouch".format(percentage))
    print("You have " + str(fingers_left) + " fingers left:\n")
    print("Thank you for playing! " + username + "!\n\n\n\n\n\n")
    print("Game Over")
    # Avoid calling quit_game() here

# Call the game_over function when the game ends
game_over()