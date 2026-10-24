print("Chatbot: Hello! I am a chatbot. Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hi" or user == "hello":
        print("Chatbot: Hello! How can I help you?")
    elif "name" in user:
        print("Chatbot: I am a Python chatbot.")
    elif "how are you" in user:
        print("Chatbot: I am fine, thank you!")
    elif "python" in user:
        print("Chatbot: Python is a great programming language.")
    elif user == "bye":
        print("Chatbot: Goodbye! Have a nice day.")
        break
    else:
        print("Chatbot: Sorry, I did not understand that.")