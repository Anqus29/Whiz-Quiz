import random
from colorama import Fore, init
import time
from typewriter import typing

init()

def ask_question(question_number, question, time_limit, hints_used):
    """
    Handles a single question, including displaying it, managing the timer, and processing user input.
    """
    # Displays the questions and shuffles the options
    typing(Fore.MAGENTA + f"Question {question_number}: {question['question']}")
    options = question["options"]
    correct_answer = options[0]
    random.shuffle(options)

    # Displays the shuffled options
    for i, option in enumerate(options, 1):
        typing(Fore.CYAN + f"{i}. {option}")

     # Records the start time to track the time limit
    start_time = time.time()

    while True:        

        try:
            user_answer = input(Fore.RESET + "Enter the number of your answer or 'H' for a hint: ").strip()

            # Checks if the time limit has run out
            if (time.time() - start_time) >= time_limit:
                typing(Fore.RED + "\nYou ran out of Time!")
                typing(Fore.RED + f"The correct answer was: {correct_answer}")
                return False, hints_used # Returns false if the time is up
            
            if not user_answer.isdigit() and user_answer.lower() == 'h':
                if hints_used < 3: # Checks if there are hints available
                    hints_used += 1
                    typing(Fore.YELLOW + f"Hints remaining: {3 - hints_used}")
                    typing(Fore.GREEN + f"Hint: {question['hint']}")
                else:
                    typing(Fore.RED + "No more hints available.")
                continue # Skip the rest of the loop and prompt again

            elif user_answer.isdigit() and 1 <= int(user_answer) <= len(options):
                user_answer = int(user_answer)
                if options[user_answer - 1] == correct_answer:
                    typing(Fore.GREEN + "Correct!") # Correct answer
                    return True, hints_used # Returns true if the answer is correct
                else:
                    typing(Fore.RED + f"Sorry, the correct answer is {correct_answer}")
                    return False, hints_used # Returns false if the answer is incorrect
            else:
                typing(Fore.RED + "Invalid choice. Please select a valid number.")
        except ValueError:
            # Handle non-numeric inputs that are not 'H'
            typing(Fore.RED + "Invalid input. Please enter a number.")
