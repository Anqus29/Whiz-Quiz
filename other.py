import csv
import random

def load_questions_from_csv(questions):
    # Load questions from a CSV file and return them in a dictionary format.
    questions_by_category = {}
    categories = {}
    with open(questions) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row['Category']
            question = row['Question']
            options = row['Options'].split(", ")
            answer = row['Answer']
            random.shuffle(options)
            # Add the question to the dictionary with answers and options
            if category not in questions_by_category:
                questions_by_category[category] = []
                categories[category] = []
            # add the question to the list of questions for the category
            questions_by_category[category].append({
                "question": question,
                "answer": answer,
                "options": options
                #combines the question, answer and options into a dictionary
            })
    
    return questions_by_category

def display_categories(questions_by_category):
    """Displays available categories to the user."""
    print("Available categories:")
    for i, category in enumerate(questions_by_category.keys(), 1):
        print(f"{i}. {category}")

def get_category_choice(questions_by_category):
    """Gets user's category choice."""
    while True:
        try:
            choice = int(input("Select a category by number: "))
            if 1 <= choice <= len(questions_by_category):
                return list(questions_by_category.keys())[choice - 1]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Please enter a number.")

def quiz_user(questions_by_category):
    """Conducts a quiz based on the selected category."""
    display_categories(questions_by_category)
    selected_category = get_category_choice(questions_by_category)
    
    print(f"\nStarting quiz in category: {selected_category}\n")
    
    questions = questions_by_category[selected_category]
    random.shuffle(questions)
    score = 0
    
    for q in questions:
        print(f"{q['question']}")
        for i, option in enumerate(q['options'], 1):
            print(f"  {i}. {option}")
        
        while True:
            try:
                user_choice = int(input("Enter the number of your answer: "))
                if 1 <= user_choice <= len(q['options']):
                    break
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Please enter a number.")
        
        user_answer = q['options'][user_choice - 1]
        if user_answer == q['correct_answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {q['correct_answer']}\n")
    
    print(f"Quiz finished! Your score: {score}/{len(questions)}")

def main():
    questions_catagories = load_questions_from_csv("questions.csv")
    intro()



main()