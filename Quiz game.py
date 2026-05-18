
import time

quiz_questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A) Mumbai", "B) Delhi", "C) Chennai", "D) Kolkata"],
        "answer": "B"
    },

    {
        "question": "2. Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Venus"],
        "answer": "C"
    },

    {
        "question": "3. Who is known as the Father of Computers?",
        "options": ["A) Charles Babbage", "B) Newton", "C) Einstein", "D) Alan Turing"],
        "answer": "A"
    },

    {
        "question": "4. Which language is used for Python programming?",
        "options": ["A) HTML", "B) Python", "C) Java", "D) C++"],
        "answer": "B"
    },

    {
        "question": "5. What is the result of 15 + 10?",
        "options": ["A) 20", "B) 10", "C) 25", "D) 30"],
        "answer": "C"
    }
]

print("\n")
print("=" * 50)
print("        WELCOME TO QUIZ GAME")
print("=" * 50)

player_name = input("Enter Your Name: ")

print("\nHello", player_name, "!")
print("Quiz is Starting...")
time.sleep(2)

score = 0
question_number = 1

for quiz in quiz_questions:

    print("\n" + "-" * 50)
    print(quiz["question"])
    print("-" * 50)

    for option in quiz["options"]:
        print(option)

    answer = input("\nEnter Your Answer (A/B/C/D): ").u
    if answer == quiz["answer"]:
        print("Correct Answer!")
        score += 1

    else:
        print("Wrong Answer!")
        print("Correct Answer is:", quiz["answer"])

    time.sleep(1)
    question_number += 1


print("\n")
print("=" * 50)
print("              QUIZ RESULT")
print("=" * 50)

print("Player Name :", player_name)
print("Total Questions :", len(quiz_questions))
print("Correct Answers :", score)
print("Wrong Answers :", len(quiz_questions) - score)

percentage = (score / len(quiz_questions)) * 100

print("Percentage :", percentage, "%")

if percentage >= 90:
    print("Grade : A+")
    print("Outstanding Performance!")

elif percentage >= 75:
    print("Grade : A")
    print("Excellent Work!")

elif percentage >= 60:
    print("Grade : B")
    print("Good Job!")

elif percentage >= 40:
    print("Grade : C")
    print("Average Performance!")

else:
    print("Grade : F")
    print("Better Luck Next Time!")

print("=" * 50)
print("     THANK YOU FOR PLAYING QUIZ GAME")
print("=" * 50)
