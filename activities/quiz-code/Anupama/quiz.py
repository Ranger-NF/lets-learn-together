#python quiz
questions =("starting position of an array is :",
           "Git is a :",
           "Do you need github to use git:")
options = (( "A• 1","B• 0","C• -1"),
          ("A• website","B• version control system (VCS)"),
          ("A• yes","B• No"))
answers =("B","B","B")

score=0
question_num = 0

for question in questions:
  print("•••••••••••••••••••")
  print(question)
  for option in options [question_num]:
    print(option)
  user_input = input("select an option:")
  print("")
  
  if user_input == answers[question_num]:
   score += 1 
   print("CORRECT!")
  else:
   print ("INCORRECT!")
   print(f"{answers[question_num]}is the correct answer")
   question_num += 1
