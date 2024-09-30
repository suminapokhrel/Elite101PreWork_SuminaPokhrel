def welcome():
    print("HIII! Welcome to SumaChat, your friendly chatbot! 🎀")
    print("I'm here to make you smile and your day a little brighter! Before you can start using SumaChat, I have to get to know you!")

def user_info():
    name = input("What's your name? ")
    age = input(f"What a beautiful name, {name}, it has a nice ring to it! And how old are you? ")
    return name, age

def ask_how_can_help(name):
    print(f"\nThank you, {name}! How can I help you smile today??")
    print("Choose one of the options:")
    print("1. Tell me a fun fact!")
    print("2. Tell me a joke!")
    print("3. I need some advice.")
    print("4. Exit the conversation 🙁")