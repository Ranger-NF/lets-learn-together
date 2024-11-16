questions = ("Starting position of an array is:",
             "Git is a:",
             "Do you need a github to use git?")
options = (("A. 1 ","B. 0 ","C. -1 "),
           ("A. Website ","B. Version Control System (VCS)"),
           ("A.Yes  ","B.No "))
answers = ("B","B","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(question)
    
    for option in options[question_num]:
        print(option)

    guess=input("Enter (A,B,C): ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1
    
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("***********************************")
print("Total Score obtained: ", score,"out of 3")
    