# initialize some stuff
import builtins
import random
import sys
import time
import json
from datetime import datetime

now = datetime.now()

# type glitchy
def type_text_glitchy(text, base_delay=0.02, glitch_factor=0.001):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        delay = max(0, base_delay + random.uniform(-glitch_factor, glitch_factor))
        time.sleep(delay)

# Custom print_glitchy function
def print_glitchy(*args, delay=0.01, end='\n', sep=' '):
    for arg in args:
        if isinstance(arg, str):
            type_text_glitchy(arg, delay)
        else:
            type_text_glitchy(str(arg), delay)

    sys.stdout.write(end)
    sys.stdout.flush()
    time.sleep(max(0, delay))


# Temporarily store the original print function
original_print = builtins.print

# Override the built-in print function
builtins.print = print_glitchy

# more initialization
topics = {"animals": "animals.json"}
questionnumber = 0
fingers_lost = 0
fingers_left = 0
score = 0

# 20 alternative responses for invalid input:
alternative_responses = [
    "Terms and Conditions: Are you ready to play 'Finger Jenga' with destiny? Type YES to get started!",
    "Terms and Conditions: By playing this game, you agree to our radical digit-al transformation. Type YES to give us the green light!",
    "Terms and Conditions: Do you promise not to point fingers, especially after we've chopped some off? Type YES to show you're on board!",
    # ... (other responses)
]

print(str(now))
print("...initializing...")
print(str(now) + "\n Tiger Hardwood Software Quiz **initialized**")


# quit function will display the message "Press Enter to exit."
# and then exit the game when the user presses enter.
def quit_game():
    input("Press Enter to exit.")
    sys.exit()

# introduction to the game
# this is really select topics function but we will deal with that later
def start_game():
    global username
    print("\n\n\nWelcome to Tiger Hardwood Software, " + username + "!\n------------------------------\nAvailable Topics:\n")

    while True:
        for topic in topics:
            print(topic)

        selected_topics = input("\nPlease select from the topics above that you would like to be quizzed on: ")

        if selected_topics.lower() in topics:
            # You can process the selected_topics variable as needed for your game logic
            print("Great! You selected:", selected_topics)
            break  # Break out of the loop if a valid topic is selected
        else:
            print("Unfortunately, we don't have that topic. Please select from the list.")
            for topic in topics:
                print(topic)
            print("-----------------------------\n")

def ask_question():
    global question_number  # Declare question_number as a global variable
    question_number += 1
    print("\n\n\nOkay " + username + ", here is question number " + str(question_number) + ".\n")

# bad_input function will display the message "Please enter True or False.
# Press enter to try the same question again."
def bad_input():
    print("Please enter True or False.  Press enter to try the same question again.")
    input()

# wrong_answer function will add 1 to the finger variable and print the wrong answer message,
# then display the current score and how many fingers they lost.
def wrong_answer():
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

def right_answer():
    global score  # Declare score as a global variable
    score += 1
    print("\n\n\n...\n\n\nCongratulations, you are correct! ")
    print("Score: " + str(score) + "  |  fingers_lost: " + str(fingers_lost) + "\n")
    print("fingers left: " + str(fingers_left) + "\n")

def shuffle_questions_and_answers(questions):
    for question_data in questions:
        random.shuffle(question_data["answers"])

# Function to load questions from a JSON file
def load_questions_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        quit_game()  # You may want to implement the quit_game function
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
        quit_game()  # You may want to implement the quit_game function

# Function to ask multiple-choice questions
def ask_question_mc(question_data):
    question = question_data.get("question")
    options = question_data.get("answers")
    correct_answer = question_data.get("correct_answer")

    #print(f"DEBUG: question = {question}")  # Add this line for debugging

    # Shuffle options before presenting them
    random.shuffle(options)

    while True:
        print(question)
        for i, option in enumerate(options, start=0):
            print(f"{chr(ord('a') + i)}) {option}")

        user_input = input("Select the correct option (a, b, c, d) or type 'quit' to exit: ").lower()

        if user_input == "quit":
            quit_game()

        if user_input in ["a", "b", "c", "d"]:
            correct_option_index = options.index(correct_answer)
            selected_option = chr(ord('a') + correct_option_index)

            if user_input == selected_option:
                right_answer()
            else:
                wrong_answer()
            break
        else:
            print("Invalid input. Please enter a valid option (a, b, c, d) or type 'quit' to exit.")

# Assuming selected_topic is already set to the correct file path
selected_topic = "animals.json"

# Load questions from the selected topic file
questions_for_selected_topic = load_questions_from_file(selected_topic)

#end new code to check


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
            print("\nOkay " + username + " with " + str(start_fingers) + " fingers!!                \nLet's see if we can remedy that!")
        else:
            print("\nHuh, strange.\n OK " + username + " with " + str(start_fingers) + " fingers! Let's continue.")
        break  # Break out of the loop if input is valid
    except ValueError:
        print("\nInvalid input. Please enter a number.")

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

# Call the start_game() function after the loop
start_game()
question_number = 0


# The game begins here with question 1.
ask_question()
# Shuffle questions and answers
shuffle_questions_and_answers(questions_for_selected_topic)

# Example usage:
for question_data in questions_for_selected_topic:
    ask_question_mc(question_data)

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