print("=" * 50)
print("🤖 AI ASSISTANT CHATBOT")
print("=" * 50)

responses = {
    "hello": {
        "message": "Hello! Nice to meet you.",
        "related": ["help", "about"]
    },

    "hi": {
        "message": "Hi there! How can I help you today?",
        "related": ["help", "python"]
    },

    "python": {
        "message": "Python is a powerful programming language used in AI, Data Science, Web Development, and Automation.",
        "related": ["ai", "machine learning"]
    },

    "ai": {
        "message": "Artificial Intelligence enables computers to learn, reason, and make decisions.",
        "related": ["machine learning", "python"]
    },

    "machine learning": {
        "message": "Machine Learning is a branch of AI that allows systems to learn from data.",
        "related": ["ai", "data science"]
    },

    "data science": {
        "message": "Data Science combines statistics, programming, and analytics to extract insights from data.",
        "related": ["python", "machine learning"]
    },

    "internship": {
        "message": "Internships provide practical experience and help build industry-ready skills.",
        "related": ["python", "ai"]
    },

    "about": {
        "message": "I am an AI chatbot developed using Python and rule-based logic.",
        "related": ["help"]
    },

    "help": {
        "message": "Available topics: hello, python, ai, machine learning, data science, internship, about",
        "related": []
    }
}

conversation_count = 0

print("\nType 'help' to view topics.")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ").lower().strip()

    if user_input == "exit":
        print("\nBot: Goodbye! Have a wonderful day.")
        print(f"Total Conversations: {conversation_count}")
        break

    conversation_count += 1

    if user_input in responses:

        print("\nBot:", responses[user_input]["message"])

        related = responses[user_input]["related"]

        if related:
            print("\nRelated Topics:")
            for topic in related:
                print("✓", topic)

    else:

        print("\nBot: Sorry, I don't understand that.")

        print("\nSuggestions:")
        print("✓ help")
        print("✓ python")
        print("✓ ai")
        print("✓ machine learning")

    print("\n" + "-" * 50)