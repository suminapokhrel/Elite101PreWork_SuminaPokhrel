def welcome():
    print("HIII! Welcome to SumaChat, your friendly chatbot! 🎀")
    print("I'm here to make you smile and your day a little brighter! Before you can start using SumaChat, I have to get to know you!")

def user_info():
    name = input("What's your name? ")
    age = input(f"What a beautiful name, {name}, it has a nice ring to it! And how old are you? ")
    return name, age