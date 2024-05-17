import nltk
from nltk.corpus import wordnet
from tkinter import *
import tkinter as tk

def find_synsets(s):
    text_result.delete('1.0', END)
    sn = 0
    for i in range(len(s)):
        if not(s[i].examples() == []):
            sn += 1
            text_result.insert(tk.END, f"{sn}. {s[i].name().split('.')[0]}\nPosition: {s[i].pos()}\nDefinition: {s[i].definition()}\nExamples: {s[i].examples()}\n--------------------------\n")

root = tk.Tk()
root.title("Dictionary")
root.geometry("700x500")
root.resizable(False, False)

label_enter = Label(root, text="Enter a word:")
entry = Entry(root)
button = Button(root, text="Search", command= lambda: find_synsets(wordnet.synsets(entry.get())))
text_result = Text(root, wrap=tk.WORD)

label_enter.pack()
entry.pack()
button.pack()
text_result.pack()

root.mainloop()