print ("Multiple Choice Quiz")
score = 0
percentage = 0
total_questions = 2
a = ("Python command to display a text on the screen?", "A. display\nB. print\nC. out", "B")
b = ("What is 2+3?", "A.1\nB.2\nC.5","C")
questions = (a,b)
for question,choices,answer in questions:
    print(question)
    print(choices)
    user = input("Answer (A, B or C?):").upper()
    if user == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    percentage = (score/total_questions)*100
print(f"Score: {score}, Percentage: {percentage}%")



#print("""
#1. What is the Python command to display a text on the screen?
#display, print, out""")
#ans = "print"
#user = input().lower()
#if ans == user:
   #print("Correct!")
   #score += 1
#else:
   #print("Incorrect!")
#print(f"Your Score is {score}")

#print("""
#1. What is 2+3?
#1, 2, 5""")
#ans = "5"
#user = input().lower()
#if ans == user:
   #print("Correct!")
   #score += 1
#else:
   #print("Incorrect!")
#percentage = (score/total_questions)*100
#print(f"Score: {score}, Percentage: {percentage}%")
