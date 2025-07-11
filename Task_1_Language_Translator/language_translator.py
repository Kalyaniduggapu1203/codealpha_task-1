from tkinter import *
from translate import Translator

def translate_text():
    input_lang = from_lang.get()
    output_lang = to_lang.get()
    text_to_translate = input_text.get("1.0", END)

    try:
        translator = Translator(from_lang=input_lang, to_lang=output_lang)
        translation = translator.translate(text_to_translate)
        output_text.delete("1.0", END)
        output_text.insert(END, translation)
    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, f"Error: {str(e)}")

# GUI setup
root = Tk()
root.title("Language Translator - CodeAlpha")
root.geometry("400x400")
root.config(bg="#f0f0f0")

Label(root, text="Enter Text:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
input_text = Text(root, height=5, width=40)
input_text.pack()

Label(root, text="From Language (e.g., en):", bg="#f0f0f0", font=("Arial", 10)).pack(pady=5)
from_lang = Entry(root)
from_lang.pack()

Label(root, text="To Language (e.g., hi):", bg="#f0f0f0", font=("Arial", 10)).pack(pady=5)
to_lang = Entry(root)
to_lang.pack()

Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white", font=("Arial", 12)).pack(pady=10)

Label(root, text="Translated Text:", bg="#f0f0f0", font=("Arial", 12)).pack()
output_text = Text(root, height=5, width=40)
output_text.pack()

root.mainloop()
