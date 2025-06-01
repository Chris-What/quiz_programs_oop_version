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

    @classmethod
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
    def welcome_message(self):
        print(Fore.CYAN + Style.BRIGHT + "\nThink ya got the smarts? Then try this out! WELCOME to the QUIZ PLAYER!!")
        print(Fore.YELLOW + "Answer questions made from the Quiz Creator program, and test your brain!")

#4. shuffle the questions and start the quiz
    def play_quiz(self):
        random.shuffle(self.questions)
        total = len(self.questions)

        for number, question in enumerate(self.questions, start=1):
            print(Fore.MAGENTA + f'\nQuestion number {number}: {question.prompt}')
            for letter, choice in question.choices.items():
                print(f"    {letter}) {choice}")

            user_answer = input(Fore.CYAN + "What'll it be? A, B, C, or D?: ").strip().upper()

            if user_answer == question.correct_answer:
                print(Fore.GREEN + "DING DING DING!!! We got a smarty-pants here!")
                self.score += 1
            else:
                correct = question.correct_answer
                print(Fore.RED + f'Not quite! The correct answer is {correct}: {question.choices[correct]}')

        self.display_score(total)

#5. display the final score
    def display_score(self, total):
        print(Fore.BLUE + "\nMade it to the end! Hardly broke a sweat? Or were tears running down your face? Let's find out if you aced this quiz!")
        print(Fore.YELLOW + f"Drumroll please! *krrrr....*\nYour score is.... {self.score} out of {total}!")

        percent = (self.score / total) * 100

        if percent == 100:
            print(Fore.GREEN + Style.BRIGHT + "Are you Albert Einstein or something?? You're a GENIUS!!!")
        elif percent >= 75:
            print(Fore.GREEN + "Ya got a bright future ahead of ya, kid. One day, you might be in the history books!")
        elif percent >= 50:
            print(Fore.YELLOW + "Not bad! Keep working and you'll be better in no time!")
        else:
            print(Fore.RED + "Oh... Don't worry, we all have those moments. Just keep trying and you'll get there!")

#6. display exit message
    def exit_message(self):
        print(Fore.CYAN + Style.BRIGHT + "\nNo matter if your score is low or high, what matters is that we learn, and have fun while doing so! Thank you, dear user, for answering this quiz in the QUIZ PLAYER PROGRAM!!!")

#7. create a main entry point to run the program
    def run(self):
        self.welcome_message()
        self.load_questions()
        self.play_quiz()
        self.exit_message()

#8. launch the program
if __name__ == "__main__":
    player = QuizPlayer()
    player.run()