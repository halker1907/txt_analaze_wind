import tkinter as tk
import text_analyzer


def run():
    text_analyzer.TextAnalyzer(
        source_file='text.txt', 
        parts_of_speech=["NOUN", "VERB"],
        words_ammount=int(words_ammount.get())       
    )

window = tk.Tk()
button = tk.Button(window, text="hi!", command=run)
words_ammount = tk.Entry(window)
words_ammount.pack()
button.pack()

window.mainloop()