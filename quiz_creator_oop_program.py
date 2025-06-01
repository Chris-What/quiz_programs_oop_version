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
#7. validate the correct answer input
#8. ask the user if they want to enter another question
#9. save all collected questions to a json file
#10. display message when finishing program
#11. run the full program
#12. start the program by creating an intance of the quiz creator class and running it