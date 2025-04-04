from typewriter import typing
from introduction import intro
from retrieve_questions import retrieve_questions
from choose_categories import display_categories
from run_quiz import run_quiz
from play_again import play_again
from colorama import Fore


def main():
    total_score = 0  # Initialize total score2

    intro()

    while True:
        questions_by_category = retrieve_questions("questions.csv")  # Load questions from CSV file
        chosen_topic = display_categories(questions_by_category)
        total_score = run_quiz(questions_by_category, chosen_topic, total_score)
        # Ask the user if they want to play again
        if not play_again(total_score):
            break  # Exit the game if the user chooses not to play again

main()