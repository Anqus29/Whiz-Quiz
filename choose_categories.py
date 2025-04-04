from colorama import Fore, init
from typewriter import typing

def display_categories(categories):
    """
    Displays the available categories and prompts the user to choose one.
    """

    typing(Fore.YELLOW + "What topic would you like to choose?")
    typing(Fore.GREEN + "Topics available:")

    # Iterates through the categories and displays them
    for topic, category in enumerate(categories.keys(), 1):
        typing(Fore.CYAN + f"{topic}. {category}")
    
    # Prompts the user to choose a category and Loops until a valid choice is made
    while True:
        try:
            chosen_topic = int(input(Fore.RESET + "\nEnter the number of the topic you wish to play: "))
            if 1 <= chosen_topic <= len(categories):
                return list(categories.keys())[chosen_topic - 1]
            else:
                typing(Fore.RED + "Invalid choice. Please select a valid number.")
        except ValueError:
            typing(Fore.RED + "Invalid input. Please enter a number.")