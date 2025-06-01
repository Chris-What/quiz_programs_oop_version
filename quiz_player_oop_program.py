import json
import random
from colorama import init, Fore, Style

#1. initialize colorama, quiz questions, and score
init(autoreset=True)

class QuizQuestion:
    def __init__(self, prompt, choices, correct_answer):
        self.prompt = prompt
        self.choices = choices
        self.correct_answer = correct_answer

    def from_dict(cls, data):
        return cls(data["question"], data["choices"], data["correct_answer"])

class QuizPlayer:
    def __init__(self, filename="quiz_questions.json"):
        self.filename = filename
        self.questions = []
        self.score = 0

#2. load questions from quiz_questions.json
    def load_questions(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.questions = [QuizQuestion.from_dict(item) for item in data]
        except FileNotFoundError:
            print(Fore.RED + "Hmm... There's no quiz file, yet. Try using the Quiz Creator program first in order to use this one!")
            exit()

#3. display welcome message
#4. shuffle the questions and start the quiz
#5. display the final score
#6. display exit message
#7. create a main entry point to run the program
#8. launch the program