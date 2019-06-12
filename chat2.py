import random
import sys
from termcolor import colored

Questions = [
    "How are you?",
    "What are you doing?",
    "How is the going?"
]

Answers = [
    "I'm good and you?",
    "I am answering silly questions being asked by a human",
    "It is good, I can't complain"
]

print(colored(
    "**_________________________________________**" '\n' "Welcome to chatbot:" '\n', 'blue'))


def list_faq():
    for q in range(len(Questions)):
        print(str(q) + ":" + Questions[q])


def check_for_faq_by_index():
    list_faq()
    question_id = input("Which question do you want to answer?")

    response = ""

    if "bye" in question_id:
        sys.exit()
    elif int(question_id) < len(Questions):
        response = Answers[int(question_id)]
    else:
        response = "I dont understand"
    return response


def check_for_faq(question):
    response = ""
    if question in Questions:
        index = Questions.index(question)
        response = Answers[index]
    else:
        response = "I don't understand"
    return response


while True:
    response = check_for_faq_by_index()
    print("Bot: " + response)
