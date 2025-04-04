import csv
from typewriter import typing
from colorama import Fore

score_path = "high_score.csv"  # Ensure the file has a .csv extension for clarity

def high_score_check(correct_answers, chosen_topic):
    """
    Checks if the current score is a high score for the chosen topic and updates the high score file accordingly.
    """
    # Reads the high scores from the file
    high_scores = {}

    try:
        with open(score_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                category = row["Category"]  # Extract the category
                name = row["Name"]          # Extract the name of the high scorer
                score = int(row["Score"])   # Extract and convert the score to an integer
                high_scores[category] = {"name": name, "score": score}  # Store the high score for the category
    except FileNotFoundError:
        # If the file does not exist, initialize an empty high_scores dictionary
        typing(Fore.YELLOW + "High score file not found. A new file will be created.")
    except KeyError as e:
        # Handle missing columns in the CSV file
        typing(Fore.RED + f"Error: Missing column in the CSV file: {e}. Please ensure the file has 'Category', 'Name', and 'Score' columns.")
        return

    # Check if the current score is higher than the stored high score for the chosen topic
    if chosen_topic not in high_scores or correct_answers > high_scores[chosen_topic]["score"]:
        typing(Fore.GREEN + f"Congratulations! You have set a new high score of {correct_answers} for {chosen_topic}.")
        
        # Prompt the user to enter their name
        while True:
            user_name = input(Fore.RESET + "Enter your name: ").strip()
            if user_name and len(user_name) <= 20 and user_name.isalnum():
                break
            typing(Fore.RED + "Name must be alphanumeric and up to 20 characters. Please enter a valid name.")
        
        # Update the high score for the chosen topic
        high_scores[chosen_topic] = {"name": user_name, "score": correct_answers}

    try:
        # Write the updated high scores back to the file
        with open(score_path, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ["Category", "Name", "Score"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for category, data in high_scores.items():
                writer.writerow({"Category": category, "Name": data["name"], "Score": data["score"]})
    except Exception as e:
        print(Fore.RED + f"Error writing to high score file: {e}")
