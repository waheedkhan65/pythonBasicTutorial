questions = [
    {"question": "What is the capital city of Australia?", "answers": ["a:Islamabad  ", "b:Canberra  ", "c:Cairo  ", "d:Sydney  "], "correct": "b"},
    {"question": "Who wrote the play \"Romeo and Juliet\"?", "answers": ["a: William Shakespeare  ", "b: Charles Dickens  ", "c: George Orwell  ", "d: Virginia Woolf  "], "correct": "a"},
    {"question": "What is the largest planet in our solar system?", "answers": ["a: Mercury  ", "b: Venus  ", "c: Mars  ", "d: Jupiter  "], "correct": "d"},
    {"question": "Which element has the chemical symbol 'O'?", "answers": ["a: Osmium  ", "b: Oxygen  ", "c: Oganesson  ", "d: Osmium  "], "correct": "b"},
    {"question": "In which year did the Titanic sink?", "answers": ["a: 1990  ", "b: 1991  ", "c: 1992  ", "d: 1989  "], "correct": "c"}
]

for q in questions:
    print(q["question"])
    for i in range (len(q["answers"])):
        print(q["answers"][i], end = '')
        if ( i+1 ) % 2==0 :
            print()
    user_input = input("Enter the letter for your answer : ").strip().lower()
    if user_input == q["correct"]:
        print("Correct answer")
    else:
     print("Incorrect answer")
    print()
    print()

