import tkinter as tk
from tkinter import scrolledtext
import random

class Chatbox:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbox")
        self.root.geometry("400x500")
        
        self.chat_log = scrolledtext.ScrolledText(self.root, width=40, height=20)
        self.chat_log.pack(padx=10, pady=10)

        self.input_field = tk.Entry(self.root, width=30)
        self.input_field.pack(padx=10, pady=10)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

        self.chat_log.insert(tk.END, "Welcome to the chatbox! I'm happy to chat with you.\n")

    def send_message(self):
        message = self.input_field.get()
        self.chat_log.insert(tk.END, "You: " + message + "\n")
        self.input_field.delete(0, tk.END)

        responses = [
            "That's interesting!",
            "I'm not sure I understand. Can you please rephrase?",
            "I'm happy to help with that!",
            "Sorry, I'm not sure I can help with that.",
            "That's a great question!",
            "I'm not sure I understand. Can you please provide more context?"
        ]
        response = random.choice(responses)
        self.chat_log.insert(tk.END, "AI: " + response + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    chatbox = Chatbox(root)
    root.mainloop()
