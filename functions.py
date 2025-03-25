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
    # loads questions from CSV file
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row["Category"]
            question = row["Question"]
            options = [option.strip() for option in row["Options"].split(",")]
            answer_index = int(row["Answer"]) - 1 
            hint = row["Hint"]
            #adds the data into individual variables
            if category not in questions_by_category:
                questions_by_category[category] = []
                #creates a list of each question type for each category
            questions_by_category[category].append({
                "question": question,
                "answer_index": answer_index,  # Store the correct answer index
                "options": options,
                "hints": hint
            #combines the question, answer and options into a dictionary
            })
    return questions_by_category

def display_categories(categories):
    print("What topic would you like to choose?\nTopics available:")
    for i, category in enumerate(categories.keys(), 1):
        print(f"{i}. {category}")
        #print avaliable topics
    while True:
        try:
            chosen_topic = int(input("\nEnter the number of the topic: "))
            #accepts an input from the user 
            if 1 <= chosen_topic <= len(categories):
                return list(categories.keys())[chosen_topic-1]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            #asks for a valid input if the input is wrong

def run_quiz(questions_by_category, chosen_topic):
    correct_answers = 0
    print(f"\nStarting quiz in category: {chosen_topic}\n")

    #shuffles questions
    questions = questions_by_category[chosen_topic]
    random.shuffle(questions) 

    #loops for each question
    for question_number, question in enumerate(questions, 1):
        print(f"Question {question_number}: {question['question']}")
        options = question["options"]
        correct_answer = options[question["answer_index"]] # Get the correct answer
        random.shuffle(options)  # Shuffle options
        
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        # Get user input for the answer
        while True:
            try:
                user_answer = int(input("Enter the number of your answer or '0' for a hint: "))
                #accepts the user input

                if user_answer == 0:
                    print(f"Hint: {question['hints']}\n")
                    #if the user asks for a hint
                
                elif 1 <= user_answer <= len(options):
                    break
                else:
                    print("Invalid choice. Please select a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        #accepts the user input
        if options[user_answer - 1] == correct_answer:
            correct_answers += 1
            print("Correct!\n")
            #if the user is correct
        else:
            print(f"Sorry, the correct answer is {correct_answer}\n")
            #if the user is wrong
        print(f"Correct answers: {correct_answers}/{question_number}\n")
        #prints the current total score
    print(f"\nYou got {correct_answers} out of {question_number} questions correct.")
    #prints the final score