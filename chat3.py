import sys
import pandas as pd
import numbers
from termcolor import colored
df = pd.read_'FAQS.docx', sheet_name=0)

Questions = df['Questions'].tolist()

Answers = df['Answers'].tolist()

print(colored("********************************"'\n'
              "--", 'red'))
print(colored("Hello, I am here to help you know the \
     frequently asked questions at Andela", 'blue'))


def list_faq():
    print("The following are some of th Andela FAQS")
    for q in range(len(Questions)):
        print(str(q) + ":" + Questions[q])


def check_for_faq_by_index():
    list_faq()
    question_id = input("Which question do you have for us?")

    response = ""

    if "no" in question_id:
        sys.exit()

    while not question_id.isdigit():
        print(colored("unfortunately I cannot \
             answer that question correctly", 'red'))
        text_file = open('questions.txt', 'a ')
        text_file.write(question_id * '\n')
        text_file.close()
        question_id = ('Do you have another question for us?')
        response = ''

        if 'no' in question_id:
            sys.exit()
    if 'bye' in question_id:
        sys.exit()
    elif int(question_id) < len(Questions):
        response = Answers[int(question_id)]

    else:
        response = 'Sorry, I do not understand'
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
