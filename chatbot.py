import random
import nltk
from nltk.chat.util import Chat, reflections
import datetime

# Download required data
nltk.download('punkt')

pairs = [

    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],

    [
        r"what is your name?",
        ["I am an AI Chatbot created by Deepika."]
    ],

    [
        r"how are you ?",
        ["I'm doing great!", "I'm fine, thank you!"]
    ],

    [
        r"what can you do?",
        ["I can chat with you, tell time, and answer simple questions."]
    ],

    [
        r"help",
        ["You can ask me about time, date, or general questions."]
    ],

    [
        r"time",
        [lambda: "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")]
    ],

    [
        r"date",
        [lambda: "Today's date is " + datetime.datetime.now().strftime("%d-%m-%Y")]
    ],

    [
        r"bye",
        ["Goodbye!", "See you later!"]
    ]

]

chatbot = Chat(pairs, reflections)

print("Hello! I am your AI Chatbot. Type 'bye' to exit.")

chatbot.converse()