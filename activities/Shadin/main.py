 
import tkinter as tk
from tkinter import messagebox

def score():
    score = 0
    answ1 = ans1.get()
    answ2 = ans2.get()
    answ3 = ans3.get()

    if answ1 == 0:
        score += 1
    if answ2 == "Version Control System":
        score += 1
    if answ3 == "No":
        score += 1

    messagebox.showinfo("Score", f"You got {score} out of 3 correct")

    ask = messagebox.askyesno("Answer", "Do you want to know the answer?")
    if ask:
        messagebox.showinfo("Answer", "1> 0\n2> Version Control System\n3> No")
    root.destroy()
    

root = tk.Tk()
root.title("Quiz")

qn1 = tk.Label(root, text="1. Starting position of an array is:")
ans1 = tk.IntVar()
ansof1 =["-1", "0", "1"]
qn1ans1 = tk.OptionMenu(root, ans1, *ansof1)
ans1.set(ansof1[0])

qn1.pack()
qn1ans1.pack()

qn2 = tk.Label(root, text="2. Git is a: ")
ans2 = tk.StringVar()
ansof2 = ["Website","Version Control System"]
qn2ans2 = tk.OptionMenu(root, ans2, *ansof2)
ans2.set(ansof2[0])

qn2.pack()
qn2ans2.pack()

qn3 = tk.Label(root, text="3. Do you need github to use git?")
ans3 = tk.StringVar()
ansof3 = ["Yes", "No"]
qn3ans3 = tk.OptionMenu(root, ans3, *ansof3)
ans3.set(ansof3[0])

qn3.pack()
qn3ans3.pack()

btn = tk.Button(root, text="Submit", command=score)
btn.pack()

root.mainloop()