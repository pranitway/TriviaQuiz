from tkinter import *
from quiz_brain import QuizBrain
import pathlib

THEME_COLOR = "#375362"
RED_COLOR = "#e84545"
FONT = ("Courier", 20, "bold")
class QuizInterface:
    def __init__(self, quiz_obj: QuizBrain, high_score):
        self.quiz = quiz_obj
        self.window = Tk()
        self.window.title("TriviaQuiz")
        self.window.geometry("400x570")
        self.window.resizable(False, False)
        icon_path = f"{pathlib.Path.cwd()}/images/quiz.ico"
        self.window.iconbitmap(icon_path)
        self.window.config(background="#b4aee8")

        self.label_score1 = Label(master=self.window, text=f"Prev.\nHigh Score: {high_score}", font=("Courier", 15, "bold"), bg="#b4aee8", fg="white",justify="left")
        self.label_score1.grid(column=0, row=0, columnspan=2, sticky=W, pady=(30, 10), padx=(35, 0))

        self.label_score2 = Label(master=self.window, text="\nScore: 0", font=("Courier", 15, "bold"), bg="#b4aee8", fg="WHITE" , justify="right")
        self.label_score2.grid(column=0, row=0, columnspan=2, sticky=E, pady=(30, 10))

        self.canvas = Canvas(master=self.window, width=330, height=300, bg=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=(36, 0))

        self.label_q = self.canvas.create_text(165, 96, text=f"question", width=320,
                                               font=('Courier', 15, 'bold'), fill="white", justify="center")

        img_button_1 = PhotoImage(file="images/true.png")
        button_true = Button(master=self.window, image=img_button_1, command=self.send_true)
        button_true.grid(column=0, row=2, padx=(36, 0), pady=(20, 0))

        img_button_2 = PhotoImage(file="images/false.png")
        button_false = Button(master=self.window, image=img_button_2, command=self.send_false)
        button_false.grid(column=1, row=2, pady=(20, 0))

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.label_q, text=q_text)

    def send_true(self):
        return_score, answ, high_score = self.quiz.check_answer("True")
        self.label_score2["text"] = f"\nScore: {return_score}"
        self.label_score1["text"] = f"Prev.\nHigh Score: {high_score}"
        if answ == "wrong":
            self.change_back_color(RED_COLOR)
            self.window.after(200, self.change_back_color, "#b4aee8")
        self.get_next_question()

    def send_false(self):
        return_score, answ, high_score = self.quiz.check_answer("False")
        self.label_score2["text"] = f"\nScore: {return_score}"
        self.label_score1["text"] = f"Prev.\nHigh Score: {high_score}"
        if answ == "wrong":
            self.change_back_color(RED_COLOR)
            self.window.after(200, self.change_back_color, "#b4aee8")

        self.get_next_question()

    def change_back_color(self, color):
        self.window.config(background=color)
