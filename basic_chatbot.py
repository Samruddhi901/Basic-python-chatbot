print("BASIC CHATBOT")
from datetime import datetime
now = datetime.now()
print("current date and time: ",now)
while True:
    user = input("You: ").lower()
    if user == "hello":
        print("Bot: Hi")
    elif user == "tell me the value of PI":
        print("Bot: PI=3.142")
    elif user == "byy":
        print("Bot: Byy.Have a nice day")
    else:
        print("Sorry i didn't understand")
