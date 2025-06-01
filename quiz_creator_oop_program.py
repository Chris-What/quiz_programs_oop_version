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
#4. initialize a storage for quiz data and the output filename
#5. display welcome message to user when starting program
#6. collect the question, choices, and the correct answer
#7. validate the correct answer input
#8. ask the user if they want to enter another question
#9. save all collected questions to a json file
#10. display message when finishing program
#11. run the full program
#12. start the program by creating an intance of the quiz creator class and running it