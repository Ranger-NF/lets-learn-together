print(' '*10,"┼ Quiz┼")
print("1. starting position of an array is:")
print("A.1\nB.2\nC.0\n")
op=input(">>>>").upper()
score=0
match op:
    case "C":
        print("Option C is correct")
        score+=1

    case _:

        print("Incorrect answer,correct answer is Option C:0")

print("2. Git is a:")
print("A.Website\nB.Version Control System (VCS)")
op=input(">>>>").upper()

match op:
    case "B":
        print("Option B is correct")
        score+=1

    case _:

        print("Incorrect answer,correct answer is Option B:Version Control System (VCS)")

print("3. Do you need github to use git?:")
print("A.Yes\nB.No")
op = input(">>>>").upper()
match op:
            case "B":
                print("Option B is correct")
                score+=1

            case _:

                print("Incorrect answer,correct answer is Option B:No,we don't need Github to use git")

print("YOUR SCORE IS",score,"/3")