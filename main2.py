import random
from quiz_data import quiz_questions

def retrieve_questions(topic):
    filtered_questions = [question for question in quiz_questions if question["Category"] == topic]
    random.shuffle(filtered_questions)
    return filtered_questions

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
    score = 0
    categories = ["Science", "History", "Star Wars"]
    intro()
    topic = chosen_topic(categories)
    filtered_questions = retrieve_questions(topic)
    # ...existing code...

main()




