import random
import csv
import os
from terminaltexteffects.effects.effect_burn import Burn
from terminaltexteffects.effects.effect_expand import Expand
from colorama import Fore, init
import sys
import time

file_path = "questions.csv"
init()

def typing(prompt_text):
    """
    Prints text with a typing effect.
    """
    for char in prompt_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print("")

def intro():
    """
    Displays the intro animation using terminal text effects.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
    effect = Burn(" █████╗      ██████╗ ██╗   ██╗██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗\n██╔══██╗    ██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝\n███████║    ██║   ██║██║   ██║██║  ███╔╝     ██║  ███╗███████║██╔████╔██║█████╗  \n██╔══██║    ██║▄▄ ██║██║   ██║██║ ███╔╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  \n██║  ██║    ╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗\n╚═╝  ╚═╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝")
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

    effect = Expand("██████╗ ██╗   ██╗     █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗███████╗\n██╔══██╗╚██╗ ██╔╝    ██╔══██╗████╗  ██║██╔════╝ ██║   ██║██╔════╝\n██████╔╝ ╚████╔╝     ███████║██╔██╗ ██║██║  ███╗██║   ██║███████╗\n██╔══██╗  ╚██╔╝      ██╔══██║██║╚██╗██║██║   ██║██║   ██║╚════██║\n██████╔╝   ██║       ██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝███████║\n╚═════╝    ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝\n")                                                                 
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)
    print("------------------------------------------------------------------------------------------------------------")

def retrieve_questions(file_path):
    """
    Loads questions from a CSV file and organizes them by category.
    """
    questions_by_category = {}
    # loads questions from CSV file
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            question = row["Question"]
            options = [option.strip() for option in row["Options"].split(",")]
            hint = row["Hint"]
            #adds the data into individual variables
            if category not in questions_by_category:
                questions_by_category[category] = []
                #creates a list of each question type for each category
            questions_by_category[category].append({
                "question": question,
                "options": options,
                "hint": hint
            #combines the question, answer and options into a dictionary
            })
    return questions_by_category

def display_categories(categories):
    """
    Displays the available categories and prompts the user to choose one.
    """
    typing(Fore.YELLOW + "What topic would you like to choose?")
    typing(Fore.GREEN + "Topics available:")
    for i, category in enumerate(categories.keys(), 1):
        typing(Fore.CYAN + f"{i}. {category}")
    while True:
        try:
            chosen_topic = int(input(Fore.RESET + "\nEnter the number of the topic: "))
            if 1 <= chosen_topic <= len(categories):
                return list(categories.keys())[chosen_topic - 1]
            else:
                typing("Invalid choice. Please select a valid number.")
        except ValueError:
            typing("Invalid input. Please enter a number.")

def run_quiz(questions_by_category, chosen_topic, total_score):
    """
    Runs the quiz for the chosen topic and updates the total score.
    """
    correct_answers = 0
    time_limit = 15
    hints_used = 0
    #sets the time limit and hints used to 0

    typing(Fore.YELLOW + f"\nStarting quiz in category: {chosen_topic}\n")
    typing(Fore.YELLOW + f"You will have {time_limit} seconds to answer each question")
    typing(Fore.YELLOW + f"You will get 3 hints\n")

    #shuffles questions
    questions = questions_by_category[chosen_topic]
    random.shuffle(questions) 

    #loops for each question
    for question_number, question in enumerate(questions, 1):
        typing(Fore.MAGENTA + f"Question {question_number}: {question['question']}")
        options = question["options"]
        correct_answer = options[0] # Get the correct answer
        random.shuffle(options)  # Shuffle options
        
        #displays the options
        for i, option in enumerate(options, 1):
            typing(Fore.CYAN + f"{i}. {option}")

        #set the timer for 15 seconds
        start_time = time.time()

        # Get user input for the answer
        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > time_limit:
                typing(Fore.RED + "You ran out of Time!")
                typing(Fore.RED + f"The correct answer was: {correct_answer}")
                break
            # check if the user runs out of time

            try:
                user_answer = input(Fore.RESET + "Enter the number of your answer or 'H' for a hint: ").strip()
                if not user_answer.isdigit():
                    if user_answer.lower() == 'h':
                        #if the user wants a hint, it will display the hint
                        if hints_used < 3:
                            hints_used += 1
                            typing(Fore.YELLOW + f"Hints remaining: {3 - hints_used}\n")
                            typing(Fore.GREEN + f"Hint: {question['hint']}\n")
                            #if the user has hints left, it will display how many hints are left
                        else:
                            typing(Fore.RED + "No more hints available.\n")
                                #if the user runs out of hints
                        continue
                    else:
                        typing(Fore.RED + "Invalid input. Please enter a number or 'H' for a hint.")
                    continue

                elif 1 <= int(user_answer) <= len(options):
                    user_answer = int(user_answer)
                    if options[user_answer - 1] == correct_answer:
                        correct_answers += 1
                        typing(Fore.GREEN + "Correct!\n")
                        #if the user is correct
                    else:
                        typing(Fore.RED + f"Sorry, the correct answer is {correct_answer}\n")
                    typing(Fore.GREEN +f"Correct answers: {correct_answers}/{question_number}\n")
                    break
                else:
                    typing(Fore.RED + "Invalid choice. Please select a valid number.")
            except ValueError:
                typing(Fore.RED + "Invalid input. Please enter a number.")
    
        
        
    typing(Fore.GREEN +f"\nYou got {correct_answers} out of {question_number} questions correct.")
    print("You used {hints_used} hints") #prints the final score
    total_score += correct_answers  # Update the total score
    return total_score


def play_again(total_score):
    """
    Prompts the user to play again or exit the game.
    """
    while True:
        typing(Fore.RESET + "Would you like to play again? (Y/N): ")
        user_input = input().strip().lower()
        if user_input == "y":
            return True  # User wants to play again
        elif user_input == "n":
            typing(Fore.BLUE + "Thank you for playing!")
            typing(f"Your total score was {total_score}")
            return False  # User wants to exit the game
        else:
            typing(Fore.RED + "Invalid choice. Please enter 'Y' or 'N'.")
