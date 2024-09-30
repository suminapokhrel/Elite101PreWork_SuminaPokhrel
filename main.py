import random

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

def get_advice():
    print("\nWhat type of advice do you need? Choose one: ")
    print("1. Relationship")
    print("2. Friendship ")
    print("3. Family")
    print("4. Mental Health")
    choice = input("Enter a number that represents what you need: ")
    return choice

def get_random_fun_fact():
    facts = [
        "The fear of long words is called Hippopotomonstrosesquippedaliophobia, which is also a long word. 😂",
        "Snails have between 1,000 and 12,000 teeth. 🐌",
        "A chicken once lived for 18 MONTHS without his head! 😨",
        "Deaf people are known to use sign language in their sleep.😴",
        "Being bored is actually a 'high arousal state' physiologically. 🧠",
        "LEGO bricks withstand compression better than concrete. 🧱",
        "A lightning bolt is five times hotter than the surface of the Sun. ️⛈",
        "Someone left a family photo on the Moon. 🌑",
        "You have a 50 percent chance of sharing a birthday with a friend. 🎂",
        "Pine trees can tell if it's about to rain. 🌲",
    ]
    return random.choice(facts)