import tkinter as tk
from tkinter import messagebox


questions = [
    {
        "question": "Starting Position of an array is?",
        "choices": ["0", "-1", "1"],
        "answer": "0"
    },
    {
        "question": "Git is a?",
        "choices": ["website", "Version Control System","None"],
        "answer": "Version Control System"
    },
    {
        "question": "Do you need GitHub to use git?",
        "choices": ["Yes", "No","None"],
        "answer": "No"
    }
]


current_question_index = 0
score = 0


def display_question():
    global current_question_index
    question_data = questions[current_question_index]
    question_label.config(text=question_data["question"])
    for idx, choice in enumerate(question_data["choices"]):
        options[idx].config(text=choice)


def check_answer(selected_choice):
    global current_question_index, score
    question_data = questions[current_question_index]
    if selected_choice == question_data["answer"]:
        score += 1
    current_question_index += 1
    if current_question_index < len(questions):
        display_question()
    else:
        display_score()


def display_score():
    if score == len(questions):
        messagebox.showinfo("Quiz Completed", f"Congratulations! You got a full score: {score}/{len(questions)}")
    else:
        messagebox.showinfo("Quiz Completed", f"Your score is: {score}/{len(questions)}")
    root.destroy()


root = tk.Tk()
root.title("Quiz App")


question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400, justify="center")
question_label.pack(pady=20)


options = []
for i in range(3):  
    btn = tk.Button(root, text="", font=("Arial", 14), width=25, command=lambda choice=i: check_answer(options[choice].cget("text")))
    btn.pack(pady=5)
    options.append(btn)


display_question()
root.mainloop()
