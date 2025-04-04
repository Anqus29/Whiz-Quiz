from colorama import Fore
from typewriter import typing

def play_again(total_score):
    """
    Prompts the user to play again or exit the game.
    """
    while True:
        #Ask the user if they want to play again
        typing(Fore.RESET + "Would you like to play again? (Y/N): ")
        user_input = input().strip().lower()

        #If the user inputs Y continues the game, if N exits the game
        if user_input == "y":
            return True
        elif user_input == "n":
            typing(Fore.BLUE + "Thank you for playing!")
            typing(f"Your total score was {total_score}")
            return False
        else:
            typing(Fore.RED + "Invalid choice. Please enter 'Y' or 'N'.")