import random
import csv
import os

file_path = "questions.csv"

def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Angus's Quiz\n")
    #tis an intro but also clears ugly text

def retrieve_questions(file_path):
    questions_by_category = {}
    # load questions from CSV file
    with open("questions.csv", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            question = row["Question"]
            answer_index = int(row["Answer"]) - 1  # Convert answer to zero-based index
            options = row["Options"].split(",")
            #adds the data into indivial variables
            if category not in questions_by_category:
                questions_by_category[category] = []
                #creates a list of each question type for each category
            questions_by_category[category].append({
                "question": question,
                "answer_index": answer_index,  # Store the correct answer index
                "options": options
            #combines the question, answer and options into a dictionary
            })
    return questions_by_category

def display_categories(catagories):
    print("What topic would you like to choose?\nTopics available:")
    for i, category in enumerate(catagories.keys(), 1):
        print(f"{i}. {category}")
        #print avalable topics
    
    chosen_topic = int(input("\nEnter the number of the topic: "))
    #accepts an input from the user 
    while chosen_topic < 1 or chosen_topic > len(catagories):
        print("Invalid choice. Please select a valid number.")
        chosen_topic = int(input("What topic would you like to choose?\nEnter the number of the topic: "))
        #asks for a valid input if the input is wrong
    return list(catagories.keys())[chosen_topic-1]

def run_quiz(questions_by_category, chosen_topic):
    correct_answers = 0
    print(f"\nStarting quiz in category: {chosen_topic}\n")
    questions = questions_by_category[chosen_topic]
    random.shuffle(questions)
    #shuffles the questions
    for individual_questions, question in enumerate(questions, 1):
        print(f"{question['question']}\n")
        #prints the question
        options = question["options"]
        random.shuffle(options)  # Shuffle options
        correct_option = options.index(question["options"][question["answer_index"]]) + 1  # Adjust correct answer index
        for individual_options, option in enumerate(options, 1):
            print(f"{individual_options}. {option}\n")
            #prints the options
        user_answer = int(input("Enter the number of your answer: "))
        #accepts the user input
        while user_answer < 1 or user_answer > len(options):
            print("Invalid choice. Please select a valid number.")
            user_answer = int(input("Enter the number of your answer: "))
            #loops and asks for a valid input if the input is wrong
        if user_answer == correct_option:
            correct_answers += 1
            print("Correct!\n")
            #if the user is correct
        else:
            print(f"Sorry, the correct answer is {options[correct_option - 1]}\n")
            #if the user is wrong
        print(f"Correct answers: {correct_answers}/{individual_questions}\n")
        #prints the total score

def main():
    intro()
    questions_by_category = retrieve_questions("questions.csv")
    chosen_topic = display_categories(questions_by_category)
    run_quiz(questions_by_category, chosen_topic)

main()