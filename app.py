from rag_engine import ask_question

while True:
    question = input("Ask a question: ")

    answer = ask_question(question)

    print("\nAnswer:\n")
    print(answer)
    print("\n")