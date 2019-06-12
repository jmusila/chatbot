import random
Greeting_words = ('hello', 'hi', 'wassup', 'greetings')
Greetint_response = ['Hey', 'Good Morning?', 'Wassup?']


def check_for_greeting(sentence):
    for word in sentence.split(","):
        if word.lower() in Greeting_words:
            return random.choice(Greetint_response)
        else:
            return 'Sorry, I did not understand'


def exit_chat():
    return 'Goodbye see you later'


while True:
    sentence = input('You: ')
    response = check_for_greeting(sentence)
    print("YourBot: " + response)

    if "Bye" in sentence:
        print("YourBot: " + exit_chat())
        break
