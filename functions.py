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

    effect = Expand("██████╗ ██╗   ██╗     █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗███████╗\n██╔══██╗╚██╗ ██╔╝    ██╔══██╗████╗  ██║██╔════╝ ██║   ██║██╔════╝\n██████╔╝ ╚████╔╝     ███████║██╔██╗ ██║██║  ███╗██║   ██║███████╗\n██╔══██╗  ╚██╔╝      ██╔══██║██║╚██╗██║██║   ██║██║   ██║╚════██║\n██████╔╝   ██║       ██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝███████║\n╚═════╝    ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝  ╚══════╝\n")                                                                 
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

def retrieve_questions(file_path):
    """
    Loads questions from a CSV file and organizes them by category.
    """
    questions_by_category = {}
    try:
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row["Category"]
                question = row["Question"]
                options = [option.strip() for option in row["Options"].split(",")]
                hint = row["Hint"]
                if category not in questions_by_category:
                    questions_by_category[category] = []
                questions_by_category[category].append({
                    "question": question,
                    "options": options,
                    "hint": hint
                })
    except FileNotFoundError:
        typing(Fore.RED + "Error: The questions file was not found. Please ensure 'questions.csv' exists.")
        raise
    except KeyError as e:
        typing(Fore.RED + f"Error: Missing column in the CSV file: {e}")
        raise
    return questions_by_category

def display_categories(categories):
    """
    Displays the available categories and prompts the user to choose one.
    """
    typing(Fore.YELLOW + "What topic would you like to choose?")
    typing(Fore.GREEN + "Topics available:")
    for topic, category in enumerate(categories.keys(), 1):
        typing(Fore.CYAN + f"{topic}. {category}")
    while True:
        try:
            chosen_topic = int(input(Fore.RESET + "\nEnter the number of the topic: "))
            if 1 <= chosen_topic <= len(categories):
                return list(categories.keys())[chosen_topic - 1]
            else:
                typing(Fore.RED + "Invalid choice. Please select a valid number.")
        except ValueError:
            typing(Fore.RED + "Invalid input. Please enter a number.")

def run_quiz(questions_by_category, chosen_topic, total_score):
    """
    Runs the quiz for the chosen topic and updates the total score.
    """
    correct_answers = 0
    time_limit = 20
    hints_used = 0

    typing(Fore.YELLOW + f"\nStarting quiz in category: {chosen_topic}\n")
    typing(Fore.YELLOW + f"You will have {time_limit} seconds to answer each question.")
    typing(Fore.YELLOW + "You will get 3 hints.\n")

    questions = questions_by_category[chosen_topic]
    random.shuffle(questions)

    for question_number, question in enumerate(questions, 1):
        correct, hints_used = ask_question(question_number, question, time_limit, hints_used)
        if correct:
            correct_answers += 1

        typing(Fore.GREEN + f"Correct answers so far: {correct_answers}/{question_number}\n")

    typing(Fore.GREEN + f"\nYou got {correct_answers} out of {len(questions)} questions correct.")
    typing(Fore.YELLOW + f"You used {hints_used} hint/s.\n")
    total_score += correct_answers
    return total_score

def ask_question(question_number, question, time_limit, hints_used):
    """
    Handles a single question, including displaying it, managing the timer, and processing user input.
    """
    typing(Fore.MAGENTA + f"Question {question_number}: {question['question']}")
    options = question["options"]
    correct_answer = options[0]
    random.shuffle(options)

    for i, option in enumerate(options, 1):
        typing(Fore.CYAN + f"{i}. {option}")

    start_time = time.time()  # Record the start time

    while True:
        # Check if time has run out
        

        try:
            user_answer = input(Fore.RESET + "Enter the number of your answer or 'H' for a hint: ").strip()
            if (time.time() - start_time) >= time_limit:
                typing(Fore.RED + "\nYou ran out of Time!")
                typing(Fore.RED + f"The correct answer was: {correct_answer}")
                return False, hints_used
            if not user_answer.isdigit() and user_answer.lower() == 'h':
                if hints_used < 3:
                    hints_used += 1
                    typing(Fore.YELLOW + f"Hints remaining: {3 - hints_used}")
                    typing(Fore.GREEN + f"Hint: {question['hint']}")
                else:
                    typing(Fore.RED + "No more hints available.")
                continue
            elif user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
                user_answer = int(user_answer)
                if options[user_answer - 1] == correct_answer:
                    typing(Fore.GREEN + "Correct!")
                    return True, hints_used
                else:
                    typing(Fore.RED + f"Sorry, the correct answer is {correct_answer}")
                    return False, hints_used
            else:
                typing(Fore.RED + "Invalid choice. Please select a valid number.")
        except ValueError:
            typing(Fore.RED + "Invalid input. Please enter a number.")

def play_again(total_score):
    """
    Prompts the user to play again or exit the game.
    """
    while True:
        typing(Fore.RESET + "Would you like to play again? (Y/N): ")
        user_input = input().strip().lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            typing(Fore.BLUE + "Thank you for playing!")
            typing(f"Your total score was {total_score}")
            return False
        else:
            typing(Fore.RED + "Invalid choice. Please enter 'Y' or 'N'.")