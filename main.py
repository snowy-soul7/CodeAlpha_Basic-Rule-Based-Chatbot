def chatbot():
    print("BOT: Hello! I am a simple chatbot")
    while True:
        user_input = input("YOU:").lower().strip()

        if user_input in ["hello", "hi", "hey"]:
            print("BOT: Hi! Nice to meet you")
        elif user_input in ["how are you", "how are you?"]:
            print("BOT: I am fine, Thanks! How are you?")
        elif user_input in  ["fine","good","i am fine", 
                             "i am good","great"]:
            print("BOT: That's great to hear this!")
        elif user_input in ["what is your name", "What is you name?",
        " What's your name",]:
            print("BOT: I am a basic rule-based chatbot")
        elif user_input in ["bye", "byee", "goodbye", "see you" ]:
            print("BOT: See you soon! Have a nice day")        
            break
        else:
            print("BOT: Sorry, I don't understand")
chatbot()            
