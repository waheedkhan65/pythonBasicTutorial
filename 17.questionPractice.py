# questions = [
#       "What is the capital city of Australia?"
#       "Who wrote the play \"Romeo and Juliet\"?"
#       "What is the largest planet in our solar system?"
#       "Which element has the chemical symbol /'O/'?"
#       "In which year did the Titanic sink?"
# ]


# answers = [
#       "a: Islamabad  b: Canberra  c: Cairo  d: Sydney"
#       "a:William Shakespeare b: Charles Dickens c: George Orwell d: Virginia Woolf"
#       "a: Mercury  b: Venus  c: Mars  d: Jupiter"
#       "a: Osmium  b: Oxygen  c: Oganesson  d:Osmium"
#       "a: 1990  b: 1991  c: 1992  d: 1989"
# ]

# correctAnswers = ["b","a","d","b","c"]

# for i in range(len(questions)):
#     print(f"Questions {i+1}")
#     print(questions[i])
#     print(answers[i])

#     userAnswers = input("Enter a letter for your answer: ").strip().lower()

#     if userAnswers == correctAnswers[i]:
#         print("Correct answer")
#     else:
#         print("Incorrect answer")


questions = [
    {"question": "What is the capital city of Australia?", "answers": ["a: Islamabad", "b: Canberra", "c: Cairo", "d: Sydney"], "correct": "b"},
    {"question": "Who wrote the play \"Romeo and Juliet\"?", "answers": ["a: William Shakespeare", "b: Charles Dickens", "c: George Orwell", "d: Virginia Woolf"], "correct": "a"},
    {"question": "What is the largest planet in our solar system?", "answers": ["a: Mercury", "b: Venus", "c: Mars", "d: Jupiter"], "correct": "d"},
    {"question": "Which element has the chemical symbol 'O'?", "answers": ["a: Osmium", "b: Oxygen", "c: Oganesson", "d: Osmium"], "correct": "b"},
    {"question": "In which year did the Titanic sink?", "answers": ["a: 1990", "b: 1991", "c: 1992", "d: 1989"], "correct": "c"}
]

for q in questions:
    print(q["question"])
    for ans in q["answers"]:
        print(ans)
    user_answer = input("Enter the letter for your answer: ").strip().lower()
    if user_answer == q["correct"]:
        print("Correct answer")
    else:
        print("Incorrect answer")
    print()  # Print a blank line for readability

