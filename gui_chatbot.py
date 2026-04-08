import tkinter as tk
from datetime import datetime

# Function to save chat history
def save_chat(message):
    with open("chat_history.txt", "a") as file:
        file.write(message + "\n")

# Function to send message
def send_message():
    user_message = entry_box.get()

    if user_message == "":
        return

    # Show user message
    chat_box.insert(tk.END, "You: " + user_message + "\n")
    save_chat("You: " + user_message)

    # Bot responses
    if user_message.lower() == "hi":
        bot_reply = "Hello!"

    elif user_message.lower() == "hello":
        bot_reply = "Hi there!"

    elif user_message.lower() == "how are you":
        bot_reply = "I'm doing great!"

    elif user_message.lower() == "time":
        bot_reply = datetime.now().strftime("Current time: %H:%M:%S")

    elif user_message.lower() == "date":
        bot_reply = datetime.now().strftime("Today's date: %d-%m-%Y")

    elif user_message.lower() == "help":
        bot_reply = "You can ask: hi, time, date, bye"

    elif user_message.lower() == "bye":
        bot_reply = "Goodbye! Have a nice day."

    else:
        bot_reply = "Sorry, I don't understand."

    # Show bot reply
    chat_box.insert(tk.END, "Bot: " + bot_reply + "\n")
    save_chat("Bot: " + bot_reply)

    entry_box.delete(0, tk.END)

# Function to clear chat
def clear_chat():
    chat_box.delete('1.0', tk.END)

# Create window
window = tk.Tk()
window.title("AI Chatbot")
window.geometry("400x500")

# Chat display
chat_box = tk.Text(window, height=20, width=50)
chat_box.pack()

# Entry box
entry_box = tk.Entry(window, width=40)
entry_box.pack()

# Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

# Clear button
clear_button = tk.Button(window, text="Clear Chat", command=clear_chat)
clear_button.pack()

window.mainloop()