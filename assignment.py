school = "Ladoke Akintola University of Technology"
department = "Computer science"
date = "20/ 10/ 26"
course = "lou 212"
instructions = "Answer all five questions"
print(school)
print(department)
print(date)
print(course)
print(instructions)

score = 0

question1  = (
            """1. What is the capital of Nigeria?"
        A. Lagos
        B. Abuja
        C. Kano
        D. Ibadan
""")
print(question1)
answer1 = input("Enter your answer: ")

if answer1 == "B":
    score = score + 1

question2  = (
            """2. How many days are in a week?"
        A. Eight days
        B. Nine days
        C. Seven days
        D. Twelve days
""")
print(question2)
answer2 = input("Enter your answer: ")

if answer2 == "C":
    score = score + 1

    question3  = (
            """3. What planet is known as the red planet?"
        A. Earth
        B. Venus
        C. Saturn
        D. Mars
""")
print(question3)
answer3 = input("Enter your answer: ")

if answer3 == "D":
    score = score + 1

    question4  = (
            """4. How many continets are there in the world?"
        A. Seven
        B. Five
        C. Six
        D. Nine
""")
print(question4)
answer4 = input("Enter your answer: ")

if answer4 == "A":
    score = score + 1

    question5  = (
            """5. What is the largest ocean in the world?"
        A. Atlantic ocean
        B. Pacific ocean
        C. Indian ocean
        D. Arctic ocean
""")
print(question5)
answer5 = input("Enter your answer: ")

if answer5 == "D":
    score = score + 1

print("Examination Completed")
print("Your score is:", score,"/5")
print("percentage:",(score / 5) * 100, "%")

