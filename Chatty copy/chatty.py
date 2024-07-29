import openai
import speech_recognition as sr
from tkinter.constants import DISABLED, NORMAL
import tkinter as tk
from tkinter import scrolledtext
import subprocess
import sys

# Set up OpenAI API credentials
openai.api_key = 'API_KEY'

def ask_openai(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].message['content'].strip()
    return message

# Function to recognize speech using microphone
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand you."
    except sr.RequestError:
        return "Sorry, my speech recognition service is currently down."

class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chatty App")
        self.window.geometry("400x600")
        self.window.attributes('-fullscreen', True)

        self.scroll_frame = tk.Frame(self.window)
        self.scroll_frame.pack(side="top", fill="both", expand=True)

        self.chat_history = tk.Text(self.scroll_frame, wrap="word", state="disabled")
        self.chat_history.pack(side="left", fill="both", expand=True)
        self.chat_history.configure(bg="#5ce1e6")

        self.scrollbar = tk.Scrollbar(self.scroll_frame, orient="vertical", command=self.chat_history.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.chat_history.configure(yscrollcommand=self.scrollbar.set)

        self.question_entry = tk.Entry(self.window, width=200, font=("Arial", 12))
        self.question_entry.pack(pady=10)

        self.ask_button = tk.Button(self.window, text="Ask", width=200, command=self.ask_question, font=("Arial", 12), padx=20, pady=10)
        self.ask_button.pack(pady=10)

        self.clear_button = tk.Button(self.window, text="Clear", width=200, command=self.clear_all, font=("Arial", 12), padx=20, pady=10)
        self.clear_button.pack(pady=10)

        self.listen_button = tk.Button(self.window, text="Speak", width=200, command=self.listen_question, font=("Arial", 12), padx=20, pady=10)
        self.listen_button.pack(pady=10)

        self.window.mainloop()

    def clear_all(self):
        self.chat_history.configure(state="normal")
        self.chat_history.delete("1.0", tk.END)
        self.chat_history.configure(state="disabled")

    def ask_question(self):
        question = self.question_entry.get().strip()
        if question != "":
            response = ask_openai(question)
            self.update_chat_history(question, response)

    def listen_question(self):
        question = recognize_speech()
        self.question_entry.delete(0, tk.END)
        self.question_entry.insert(0, question)
        response = ask_openai(question)
        self.update_chat_history(question, response)

    def update_chat_history(self, question, response):
        self.chat_history.configure(state="normal")
        if self.chat_history.index('end') != None:
            self.chat_history.insert('end', "You: " + question + "\n", 'bold')
            self.chat_history.insert('end', "Zeus: " + response + "\n\n")
            self.chat_history.tag_configure('bold', font=("Arial", 12, 'bold'))
            self.chat_history.configure(state="disabled")
            self.chat_history.yview('end')

class ChatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat App")

        # Create a scrolled text widget to display messages
        self.message_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=40, height=20)
        self.message_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Entry widget for typing messages
        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(side=tk.Left, padx=10, pady=10, fill=tk.X, expand=True)

        # Button to send messages
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10, pady=10)

    def send_message(self):
        message = self.entry.get()
        if message:
            self.display_message("You: " + message)
            self.entry.delete(0, tk.END)

    def display_message(self, message):
        self.message_area.configure(state=tk.NORMAL)
        self.message_area.insert(tk.END, f"{message}\n")
        self.message_area.configure(state=tk.DISABLED)
        self.message_area.yview(tk.END)



if __name__ == "__main__":
    gui = ChatbotGUI()