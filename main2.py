from functions import typing,intro, retrieve_questions, display_categories, run_quiz,play_again
from colorama import Fore


def main():
    total_score = 0  # Initialize total score

    intro()
    questions_by_category = retrieve_questions("questions.csv")

    while True:
        questions_by_category = retrieve_questions("questions.csv")
        chosen_topic = display_categories(questions_by_category)
        total_score = run_quiz(questions_by_category, chosen_topic, total_score)
        # Ask the user if they want to play again
        if not play_again(total_score):
            break  # Exit the game if the user chooses not to play again

main()