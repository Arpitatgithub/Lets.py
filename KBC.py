
# q1="What is the first 2 digit number"
# q2="What is the first 3 digit number"
# q3="What is the first 4 digit number"
# qus=[q1,q2,q3]
# q4=10
# q2=100
# q3=1000
# A1=int(input())
# for i in qus:
#           if (A1==q4):
#            print("Write Answer")
#           else:
#                 print("Wrong Answer") 

# a1=10
# q1=int(input("write first two digit number"))
# if q1==a1:
#           print("Right answer")
# else:
#  print("Wrong answer")


# q1=10
# q2=2
# q3=3
# a1=int(input("Write first two digit number : "))
# qus=[q1,q2,q3]
# while q1==a1:
#           print("Right answer")
#           break
# else:
#         print("Wrong answer")

# def kbc_game():
#     # List of questions, options, and answers
#     questions = [
#         {
#             "question": "Which planet is known as the Red Planet?",
#             "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Venus"],
#             "answer": 2
#         },
#         {
#             "question": "What is the capital of India?",
#             "options": ["1. Mumbai", "2. New Delhi", "3. Kolkata", "4. Chennai"],
#             "answer": 2
#         },
#         {
#             "question": "Which is the largest mammal?",
#             "options": ["1. Elephant", "2. Blue Whale", "3. Giraffe", "4. Rhinoceros"],
#             "answer": 2
#         },
#         {
#             "question": "Who is known as the Father of the Nation in India?",
#             "options": ["1. Jawaharlal Nehru", "2. Subhash Chandra Bose", "3. Mahatma Gandhi", "4. Bhagat Singh"],
#             "answer": 3
#         },
#         {
#             "question": "Which is the smallest continent in the world?",
#             "options": ["1. Asia", "2. Antarctica", "3. Australia", "4. Europe"],
#             "answer": 3
#         }
#     ]

#     # Prize money for each question
#     prize_money = [1000, 2000, 5000, 10000, 20000]

#     # Initialize total amount
#     total_amount = 0

#     print("Welcome to Kaun Banega Crorepati!")
#     print("Answer the following questions to win money.\n")

#     # Loop through each question
#     for index, q in enumerate(questions):
#         print(f"Q{index + 1}: {q['question']}")
#         for option in q['options']:
#             print(option)
        
#         try:
#             # Get user's answer
#             user_answer = int(input("Enter your answer (1-4): "))
#         except ValueError:
#             print("Invalid input! Moving to the next question.\n")
#             continue

#         # Check if the answer is correct
#         if user_answer == q["answer"]:
#             print(f"Correct! You win ₹{prize_money[index]}.\n")
#             total_amount += prize_money[index]
#         else:
#             print("Wrong answer! Better luck next time.\n")
#             break  # End the game on a wrong answer

#     # Display the final amount
#     print(f"Game Over! You are taking home ₹{total_amount}.")

# # Run the game
# kbc_game()
