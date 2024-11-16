questions = [
    "1. Starting position of an array is: ",
    "2. Git is a: ",
    "3. Do you need GitHub to use Git?: ",
]

options = [
    ["1) 1", "2) 0", "3) -1"],
    ["1) Website", "2) Version Control system (VCS)"],
    ["1) Yes", "2) No"]
]

answers = [
    2,
    2,
    2
]

question_index = 0

for each_question in questions:
    print(each_question)
    print("\n".join(options[question_index])) # Printing option in a new line

    print("") # Adding an empty line
    user_input = int(input("Select an option number: "))
    print("")

    if user_input == answers[question_index]:
        print("Right Answer!!")
    else:
        print("Wrong answer :(")

    print("\n======")
    question_index +=1
