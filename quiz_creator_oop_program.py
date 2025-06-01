import json

#1. define class that represents a single quiz question
class Question:
    def __init__(self, prompt, choices, correct_answer):
        self.prompt = prompt
        self.choices = choices
        self.correct_answer = correct_answer

#2. convert the question to a dictionary for json
    def dict(self):
        return {
            "question": self.prompt,
            "choices": self.choices,
            "correct_answer": self.correct_answer
        }

#3. define class that manages the quiz creation process
class QuizCreator:
    def __init__(self, filename="quiz_questions.json"):
#4. initialize a storage for quiz data and the output filename
        self.filename = filename
        self.quiz_data = []

#5. display welcome message to user when starting program
    def display_welcome_message(self):
        print("Welcome to Quiz Creator! This program allows you to create questions to be used in a quiz. To start, enter a question below.")

#6. collect the question, choices, and the correct answer
    def get_question_input(self):
        prompt = input("Enter a question for the quiz: ")
        choices = {
            "A": input("Enter choice A: "),
            "B": input("Enter choice B: "),
            "C": input("Enter choice C: "),
            "D": input("Enter choice D: "),
        }

#7. validate the correct answer input
        correct_answer = ""
        while correct_answer not in choices:
            correct_answer = input("Which choice is the correct answer? (A/B/C/D): ").upper()
            if correct_answer not in choices:
                print("Invalid choice; please choose between A, B, C, or D.")

        return Question(prompt, choices, correct_answer)

#8. ask the user if they want to enter another question
    def ask_to_continue(self):
        while True:
            choice = input("Do you want to enter another quiz question? (yes/no): ").lower()
            if choice in ["yes", "no"]:
                return choice == "yes"
            else:
                print('invalid choice; please choose between "yes" or "no".')

#9. save all collected questions to a json file
    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump([question.to_dict() for question in self.quiz_data], file, indent=4)

#10. display message when finishing program
#11. run the full program
#12. start the program by creating an intance of the quiz creator class and running it