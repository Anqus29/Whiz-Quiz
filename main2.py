import random
import csv
file_path = "questions.csv"

def intro():
    print("Welcome to Angus's Quiz")

def retrieve_questions(file_path):
    questions_by_category = {}
    # Load questions from CSV file
    with open("questions.csv", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            question = row["Question"]
            answer = row["Answer"]
            options = row["Options"].split(", ")

            if category not in questions_by_category:
                questions_by_category[category] = []

            questions_by_category[category].append({
                "question": question,
                "answer": answer,
                "options": options
            #combines the question, answer and options into a dictionary
            })
    return questions_by_category


def main():
    intro()
    questions_by_category = retrieve_questions("questions.csv")
    print(questions_by_category)
main()