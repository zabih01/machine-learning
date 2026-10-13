
import json
from difflib import get_close_matches

# Load your question-answer dataset
with open("data.json", "r", encoding="utf-8") as file:
    examples = json.load(file)

def get_answer(user_question):
    question = user_question.strip().lower()

    if not question:
        return "Please enter a question."

    # Match questions while ignoring capitalization
    questions = {
        item["question"].strip().lower(): item["answer"]
        for item in examples
    }

    if question in questions:
        return questions[question]

    # Find a similar question
    matches = get_close_matches(
        question,
        list(questions.keys()),
        n=1,
        cutoff=0.6
    )

    if matches:
        return questions[matches[0]]

    return "Sorry, I don't know the answer to that question yet."

# Interactive question-answer loop
while True:
    question = input("\nAsk a question (or type 'exit'): ").strip()

    if question.lower() == "exit":
        print("Goodbye!")
        break

    print("Answer:", get_answer(question))
