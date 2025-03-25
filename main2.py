from functions import intro, retrieve_questions, display_categories, run_quiz
import os

def main():
    while True:
        intro()
        questions_by_category = retrieve_questions("questions.csv")
        chosen_topic = display_categories(questions_by_category)
        run_quiz(questions_by_category, chosen_topic)

        # Ask the user if they want to play again
        while True:
            play_again = input("Would you like to play again? (Y/N): ").lower()
            if play_again == "y":
                break  # Restarts the game
            elif play_again == "n":
                print("Thank you for playing!")
                os.system('cls' if os.name == 'nt' else 'clear')
                return  # Exits the game
            else:
                print("Invalid choice. Please enter 'Y' or 'N'.")

main()