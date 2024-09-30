import random

def welcome():
    print("HII! Welcome to Sumachat, your friendly chatbot!")
    print("I'm here to make a smile on your face and make your day a little bit brighter, so let's get started.")

def user_info():
    name = input("I'm so glad that you are here to chat with me, but first I have to get to know you a little. What's your name?")
    while True:
        age = input ("What a beautiful name you have! Now, what is your age?")
        if age.isdigit():
            break
        else:
            print("Enter a valid number for your age.")
    return name, age