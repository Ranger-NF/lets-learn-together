questions = ["starting position of an array is :", "git is a :", "do you need github to use git?"]

options = [["1. 0", "2. 1", "3. -1"], ["1. website", "2. version control system"], ["1. yes", "2. no"]]

answers = [1, 2, 2]

qp = 0
score = 0

for question in questions:
    print(question, "\n")
    print("\n".join(options[qp]))

    response = int(input("Choose an option: "))

    if response == answers[qp]:
        score += 1
        print("The answer is correct.")
        print("\n--------------\n")
    else:
        print("The answer is incorrect.")
        print("\n--------------\n")

    qp += 1  

print("Your final score is:" ,score)
    
 

