import random
import csv
import os
from terminaltexteffects.effects.effect_burn import Burn
from terminaltexteffects.effects.effect_expand import Expand
from colorama import Fore, init

file_path = "questions.csv"
init()


def intro():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    effect = Burn(" █████╗      ██████╗ ██╗   ██╗██╗███████╗     ██████╗  █████╗ ███╗   ███╗███████╗\n██╔══██╗    ██╔═══██╗██║   ██║██║╚══███╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝\n███████║    ██║   ██║██║   ██║██║  ███╔╝     ██║  ███╗███████║██╔████╔██║█████╗  \n██╔══██║    ██║▄▄ ██║██║   ██║██║ ███╔╝      ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  \n██║  ██║    ╚██████╔╝╚██████╔╝██║███████╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗\n╚═╝  ╚═╝     ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝")
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

    effect = Expand("██████╗ ██╗   ██╗     █████╗ ███╗   ██╗ ██████╗ ██╗   ██╗███████╗\n██╔══██╗╚██╗ ██╔╝    ██╔══██╗████╗  ██║██╔════╝ ██║   ██║██╔════╝\n██████╔╝ ╚████╔╝     ███████║██╔██╗ ██║██║  ███╗██║   ██║███████╗\n██╔══██╗  ╚██╔╝      ██╔══██║██║╚██╗██║██║   ██║██║   ██║╚════██║\n██████╔╝   ██║       ██║  ██║██║ ╚████║╚██████╔╝╚██████╔╝███████║\n╚═════╝    ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝ ╚══════╝\n")                                                                 
    with effect.terminal_output() as terminal:
        for frame in effect:
            terminal.print(frame)

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
                "hint": hint
            #combines the question, answer and options into a dictionary
            })
    return questions_by_category

def display_categories(categories):
    print(Fore.YELLOW + "What topic would you like to choose?")
    print(Fore.GREEN + "Topics available:")
    for i, category in enumerate(categories.keys(), 1):
        print(Fore.CYAN + f"{i}. {category}")
    while True:
        try:
            chosen_topic = int(input(Fore.RESET + "\nEnter the number of the topic: "))
            if 1 <= chosen_topic <= len(categories):
                return list(categories.keys())[chosen_topic - 1]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def run_quiz(questions_by_category, chosen_topic, total_score):
    correct_answers = 0
    print(Fore.YELLOW + f"\nStarting quiz in category: {chosen_topic}\n")

    #shuffles questions
    questions = questions_by_category[chosen_topic]
    random.shuffle(questions) 

    #loops for each question
    for question_number, question in enumerate(questions, 1):
        print(Fore.MAGENTA + f"Question {question_number}: {question['question']}")
        options = question["options"]
        correct_answer = options[question["answer_index"]] # Get the correct answer
        random.shuffle(options)  # Shuffle options
        
        for i, option in enumerate(options, 1):
            print(Fore.CYAN + f"{i}. {option}")
        # Get user input for the answer
        while True:
            try:
                user_answer = int(input(Fore.RESET + "Enter the number of your answer or '0' for a hint: "))
                #accepts the user input

                if user_answer == 0:
                    print(Fore.GREEN + f"Hint: {question['hint']}\n")
                    #if the user asks for a hint
                elif 1 <= user_answer <= len(options):
                    break
                else:
                    print(Fore.RED + "Invalid choice. Please select a valid number.")
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")
    
        if options[user_answer - 1] == correct_answer:
            correct_answers += 1
            print(Fore.GREEN + "Correct!\n")
            #if the user is correct
        else:
            print(Fore.RED + f"Sorry, the correct answer is {correct_answer}\n")
            #if the user is wrong
        print(Fore.GREEN +f"Correct answers: {correct_answers}/{question_number}\n")
        #prints the current total score
    print(Fore.GREEN +f"\nYou got {correct_answers} out of {question_number} questions correct.")
        #prints the final score
    total_score += correct_answers  # Update the total score
    return total_score
