import tkinter as tk
from tkinter import messagebox

quiz_data = [
    {"Question": "Starting position of an array is ",
     "Options": ["1", "0", "-1"],
     "Answer": "0"},
    {"Question": "Git is a",
     "Options": ["Website", "Version Control System"],
     "Answer": "Version Control System"},
    {"Question": "Do you need Github to use Git?",
     "Options": ["Yes", "No"],
     "Answer": "No"}
]

current_question = 0
score = 0

def check_answer(selected_option):
    global current_question, score
    if selected_option == quiz_data[current_question]["Answer"]:
        score += 1

    current_question += 1
    if current_question < len(quiz_data):
        update_question()
    else:
        show_final_score()

def update_question():
    question_label.config(text=quiz_data[current_question]["Question"])
    for i, choice in enumerate(quiz_data[current_question]["Options"]):
        buttons[i].config(text=choice, command=lambda option=choice: check_answer(option))

    # Hide any extra buttons if there are fewer than 3 options
    for j in range(len(quiz_data[current_question]["Options"]), len(buttons)):
        buttons[j].pack_forget()

def show_final_score():
    messagebox.showinfo("Quiz Completed!", f"You scored {score} out of {len(quiz_data)}")
    root.quit()

root = tk.Tk()
root.title("Quiz")

question_label = tk.Label(root, text=quiz_data[current_question]["Question"], font=("Arial", 14))
question_label.pack(pady=20)

buttons = []
for i in range(3):  # Assuming a maximum of 3 buttons
    btn = tk.Button(root, text="", font=("Arial", 14))
    btn.pack(pady=3, fill=tk.X)
    buttons.append(btn)

update_question()

root.mainloop()