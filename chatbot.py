# Simple Rule-Based Chatbot

print("Chatbot: Hello! I'm PyBot. Type 'bye' anytime to exit.")

while True:
    user_input = input("You: ").lower()  # collect and normalize input

    if user_input in ["hi", "hello", "hey"]:
        print("Chatbot: Hello there! How can I help you today?")

    elif "your name" in user_input:
        print("Chatbot: I’m PyBot, your simple chatbot assistant.")

    elif "how are you" in user_input:
        print("Chatbot: I'm just a bunch of code, but I'm doing great! How about you?")

    elif "time" in user_input:
        print("Chatbot: Sorry, I can't tell time yet — maybe in my next version!")

    elif "bye" in user_input or "exit" in user_input:
        print("Chatbot: Goodbye! Have a nice day! 👋")
        break

    else:
        print("Chatbot: I'm not sure I understand. Can you rephrase?")
