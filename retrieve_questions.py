import csv
from colorama import Fore

file_path = "questions.csv"

def retrieve_questions(file_path):
    """
    Loads questions from a CSV file and organizes them by category.
    """
    questions_by_category = {}
    try:
        # Opens the CSV file and reads its content
        with open(file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Processes each row in the CSV file
            for row in reader:
                category = row["Category"] # Category of the question
                question = row["Question"] # The question itself
                options = [option.strip() for option in row["Options"].split(",")] # Options for the question
                hint = row["Hint"] # Hint for the question

                if category not in questions_by_category:
                    questions_by_category[category] = [] # Initializes the category if not already present
                questions_by_category[category].append({ # Appends the question, option and hint to the category
                    "question": question,
                    "options": options,
                    "hint": hint
                })
    # FileNotFoundError is raised if the file is not found
    except FileNotFoundError:
        print(Fore.RED + "Error: The questions file was not found. Please ensure 'questions.csv' exists.")
        raise
    # KeyError is raised if the expected columns are not found in the CSV file
    except KeyError as e:
        print(Fore.RED + f"Error: Missing column in the CSV file: {e}")
        raise
    return questions_by_category