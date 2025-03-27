from functions import intro, retrieve_questions, display_categories, run_quiz
from colorama import Fore, init
import os

init()

def main():
    total_score = 0  # Initialize total score
    intro()
    while True:
        questions_by_category = retrieve_questions("questions.csv")
        chosen_topic = display_categories(questions_by_category)
        total_score = run_quiz(questions_by_category, chosen_topic, total_score)

        # Ask the user if they want to play again
        while True:
            play_again = input("Would you like to play again? (Y/N): ").lower()
            if play_again == "y":
                break  # Restarts the game 
            elif play_again == "n":
                print(Fore.BLUE + "Thank you for playing!")
                print(f"Your total score was {total_score}")
                return  # Exits the game
            else:
                print(Fore.RED +"Invalid choice. Please enter 'Y' or 'N'.")

main()