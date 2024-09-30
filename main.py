import random
import time

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

def random_fun_fact():
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

# https://www.sciencefocus.com/science/fun-facts

def random_joke():
    jokes = [
        "What did the shark say when he ate the clownfish? This tastes a little funny. 😂",
        "Have you heard the rumor about butter? Nevermind, I shouldn't be spreading it. 🧈",
        "What does a spider's bride wear? A webbing dress. 👰",
        "What kind of shoes do spies wear? Sneak-ers. 🤣",
        "Which letter of the alphabet has the most water? The 'C'! 🌊",
        "Why can't your head be 12 inches long? Because then it would be a foot. 🦶",
        "What is fast, loud, and crunchy? A rocket chip. 🚀",
        "Why couldn't the little boy go see the pirate movie? Because it was rated 'Arrgh'! 🛳",
        "Which days are the strongest? Saturday and Sunday. The rest are weekdays. 💪",
        "What's blue and not very heavy? Light blue. 💙",
    ]
    return random.choice (jokes)

# https://www.comicrelief.org/posts/150-jokes-for-kids
# https://thecompanyofdads.com/dad-jokes/

def main(): 
    welcome()
    name, age = user_info()

    while True:
        ask_how_can_help(name)
        choice = input("What will it be? (Enter one of the numbers provided): ")

        if choice == '1':
            print(random_fun_fact())
        elif choice == '2':
            print(random_joke())
        elif choice == '3':
            advice_choice = get_advice()
            if advice_choice == '1':
                print("Relationships can be tough, but it is important to know when it's time to move on or not. If someone is being toxic or hurtful (physically or mentally), you should leave. If you're happy overall and it's just a bump in the road, then try to work it out.")
            elif advice_choice == '2':
                print("Friendships can sometimes be challenging. Surround yourself with those who uplift you, and don't hesitate to distance yourself from negativity.")
            elif advice_choice == '3':
                print("Family can be complicated. Communication is key, so try to express your feelings openly and seek understanding.")
            elif advice_choice == '4':
                print("Mental health is crucial. Remember to take care of yourself, reach out to loved ones, or seek professional help if needed. And remember, you're not alone.")
            else:
                print("Invalid choice for advice category. Please try again.")
        elif choice == '4':
            print(f"Thank you for chatting with me, {name}! I enjoyed our conversation and I hope to see you soon! Goodbye 👋")
            break
        else:
            print("Oops! That didn't seem right. Try again.")
        
        time.sleep(4)

if __name__ == "__main__":
    main()