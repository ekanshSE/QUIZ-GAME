# Define the quiz questions, choices, and answers
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ['A) London', 'B) Paris', 'C) Rome', 'D) Berlin'],
        "answer": "B"
    },
    {
        "question": "Which language is primarily used for Android app development?",
        "choices": ['A) Java', 'B) Swift', 'C) Kotlin', 'D) C#'],
        "answer": "C"
    },
    {
        "question": "Who wrote the novel '1984'?",
        "choices": ['A) Aldous Huxley', 'B) George Orwell', 'C) Isaac Asimov', 'D) Stephen King'],
        "answer": "B"
    }
]
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["question"])
        for choice in question["choices"]:
            print(choice)
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.")
        print()  # Print a blank line for spacing
    
    print(f"Your final score is {score}/{len(questions)}.")

# Run the quiz
run_quiz(questions)
