print ("Multiple Choice Quiz")
score = 0
print("""
1. What is the Python command to display a text on the screen?
display, print, out""")
ans = "print"
user = input().lower()
if ans == user:
   print("Correct!")
   score += 1
else:
   print("Incorrect!")
print(f"Your Score is {score}")

print("""
1. What is 2+3?
1, 2, 5""")
ans = "5"
user = input().lower()
if ans == user:
   print("Correct!")
   score += 1
else:
   print("Incorrect!")
print(f"Your Score is {score}")
