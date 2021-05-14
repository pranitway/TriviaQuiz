from question_model import Question
from data import question_data
import html


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None
        self.high_score = 0
        self.check_high_score()

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            self.fetch_more_ques()
            return True

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        quest = self.question_list[self.question_number].text
        temp_ques_num = self.question_number + 1
        self.question_number += 1
        self.check_high_score()
        return f"Q.{temp_ques_num}: {quest}"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            self.check_high_score()
            with open("high_score.txt", mode="r") as file_rr:
                self.high_score = file_rr.read()
            return self.score, "correct", self.high_score

        else:
            print("That's wrong.")
            return self.score, "wrong", self.high_score

    def check_high_score(self):
        try:
            file_r = open("high_score.txt", mode="r")
        except FileNotFoundError:
            print("high_score.txt File Not Exist")
            with open("high_score.txt", mode="w") as file_w:
                file_w.write(str(self.score))
        else:
            try:
                self.high_score = int(file_r.read())
            except Exception as e:
                print(e)
                self.high_score = 0
                with open("high_score.txt", mode="w") as file_w1:
                    file_w1.write(str(self.score))
            else:
                if self.score > self.high_score:
                    with open("high_score.txt", mode="w") as file_w2:
                        file_w2.write(str(self.score))
            file_r.close()

    def fetch_more_ques(self):
        print(question_data)
        for question in question_data:
            question_text = html.unescape(question["question"])
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            self.question_list.append(new_question)
