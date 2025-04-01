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

def ask_question(question_number, question, time_limit, hints_used):
    """
    Handles a single question, including displaying it, managing the timer, and processing user input.
    """
    typing(Fore.MAGENTA + f"Question {question_number}: {question['question']}")
    options = question["options"]
    correct_answer = options[0]  # The correct answer is always the first option
    random.shuffle(options)  # Shuffle the options

    # Display the options
    for i, option in enumerate(options, 1):
        typing(Fore.CYAN + f"{i}. {option}")

    # Set the timer for the question
    start_time = time.time()

    # Get user input with a timer
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time > time_limit:
            typing(Fore.RED + "You ran out of Time!")
            typing(Fore.RED + f"The correct answer was: {correct_answer}")
            return False, hints_used  # User ran out of time

        try:
            user_answer = input(Fore.RESET + "Enter the number of your answer or 'H' for a hint: ").strip()
            if not user_answer.isdigit():
                if user_answer.lower() == 'h':
                    # If the user wants a hint
                    if hints_used < 3:
                        hints_used += 1
                        typing(Fore.YELLOW + f"Hints remaining: {3 - hints_used}\n")
                        typing(Fore.GREEN + f"Hint: {question['hint']}\n")
                    else:
                        typing(Fore.RED + "No more hints available.\n")
                    continue  # Skip the rest of the loop and prompt again
                else:
                    typing(Fore.RED + "Invalid input. Please enter a number or 'H' for a hint.")
                    continue  # Skip the rest of the loop and prompt again

            user_answer = int(user_answer)

            if 1 <= user_answer <= len(options):
                # Check if the user's answer is correct
                if options[user_answer - 1] == correct_answer:
                    typing(Fore.GREEN + "Correct!\n")
                    return True, hints_used  # User answered correctly
                else:
                    typing(Fore.RED + f"Sorry, the correct answer is {correct_answer}\n")
                    return False, hints_used  # User answered incorrectly
            else:
                typing(Fore.RED + "Invalid choice. Please select a valid number.")
        except ValueError:
            typing(Fore.RED + "Invalid input. Please enter a number.")

def run_quiz(questions_by_category, chosen_topic, total_score):
    """
    Runs the quiz for the chosen topic and updates the total score.
    """
    correct_answers = 0
    time_limit = 15  # Time limit for each question in seconds
    hints_used = 0  # Track the number of hints used

    typing(Fore.YELLOW + f"\nStarting quiz in category: {chosen_topic}\n")
    typing(Fore.YELLOW + f"You will have {time_limit} seconds to answer each question.")
    typing(Fore.YELLOW + "You will get 3 hints.\n")

    # Shuffle questions
    questions = questions_by_category[chosen_topic]
    random.shuffle(questions)

    # Loop through each question
    for question_number, question in enumerate(questions, 1):
        correct, hints_used = ask_question(question_number, question, time_limit, hints_used)
        if correct:
            correct_answers += 1

        typing(Fore.GREEN + f"Correct answers so far: {correct_answers}/{question_number}\n")

    # Display the final score for this quiz
    typing(Fore.GREEN + f"\nYou got {correct_answers} out of {question_number} questions correct.")
    typing(Fore.YELLOW + f"You used {hints_used} hints.\n")
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