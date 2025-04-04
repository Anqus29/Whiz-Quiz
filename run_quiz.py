from colorama import Fore
import random
from typewriter import typing
from ask_question import ask_question



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

    # Retrieves the questions and shuffles them
    questions = questions_by_category[chosen_topic]
    random.shuffle(questions)

    # Loops through the questions and asks them one by one
    for question_number, question in enumerate(questions, 1):
        # Asks the questions and gets whether the answer was correct or not and the number of hints used
        correct, hints_used = ask_question(question_number, question, time_limit, hints_used)
        # If the user answered correctly, increments the correct answers count
        if correct:
            correct_answers += 1

        typing(Fore.GREEN + f"Correct answers so far: {correct_answers}/{question_number}\n")

    typing(Fore.GREEN + f"\nYou got {correct_answers} out of {len(questions)} questions correct.")
    typing(Fore.YELLOW + f"You used {hints_used} hint/s.\n")
    # Updates the total score based on the number of correct answers
    total_score += correct_answers
    return total_score
