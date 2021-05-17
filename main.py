from question_model import Question
from data import Request_question
from quiz_brain import QuizBrain
from ui import QuizInterface
import html

question_bank = []

questions = Request_question()

def make_question_bank():
    global question_bank
    for question in questions.question_data:
        question_text = html.unescape(question["question"])
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

make_question_bank()

quiz = QuizBrain(question_bank, questions)
gui = QuizInterface(quiz, quiz.high_score)
