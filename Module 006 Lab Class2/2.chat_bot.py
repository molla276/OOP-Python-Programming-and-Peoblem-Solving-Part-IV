"""  Chatbot.

    steps:
    1. input/listen
    2. process/decide
    3. output/talkback
"""
greet_words = ['hi', 'hello', 'yo']
bye_words = ['bye', 'tata', 'la re bedhere']
bad_words = ['dog', 'cat', 'goat', 'cow']


def listen():
    return input("Say something: ")

def decide(command):
    #print (command)
    command = command.lower()
    broken_word = command.split(" ")
    # print(broken_word)

    for word in broken_word:

        if word in greet_words:
            print("Hi man")

        elif word in bye_words:
            print("Tata bye bye")
            
        elif word in bad_words:
            print("You are bad guy")

def talkback():
    pass

while True:
    command = listen()
    decide(command) 