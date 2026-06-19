from query import query_rag

print("=" * 50)
print("Document Q&A Bot")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    answer, citations, context = query_rag(question)

    print("\nAnswer:")
    print(answer)

    print("\nSources:")

    for source in citations:
        print("-", source)
