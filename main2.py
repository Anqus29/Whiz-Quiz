import random
import csv

def retrieve_questions(topic):
    questions_by_category = {}
    # Load questions from CSV file
    with open("questions.csv") as file:
        reader = csv.DictReader(file)
        for row in file:
            category = row["Category"]
            question = row["Question"]
            answer = row["Answer"]
            options = [row["Option1"], row["Option2"], row["Option3"], answer]
            random.shuffle(options)

            if category not in questions_by_category:
                questions_by_category[category] = []

            questions_by_category[category].append({
                "question": question,
                "answer": correct_answer,
                "options": options
            })

def chosen_topic(categories):
    print("Please choose a topic:")
    for i, topic in enumerate(categories, 1):
        print(f"{i}. {topic}")
    choice = int(input("Enter the number of your chosen topic: "))
    if choice in range(1, len(categories) + 1):
        return categories[choice - 1]
    else:
        print("Invalid choice. Please try again.")
        return chosen_topic(categories)


def intro():
    print("Welcome to Angus's Quiz")

def main():
    try:
        intro()
        topic = chosen_topic(categories)
        filtered_questions = retrieve_questions(topic)

    except Exception as error_location:
        print(f"An error occurred: {error_location}")
        main()
main()




