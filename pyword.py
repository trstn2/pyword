from tkinter import Button, Text, Scrollbar
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.messagebox import askyesnocancel
from tkinter.simpledialog import askinteger, askstring
from tkinter.ttk import *
import tkinter as tk

def py_word():

    # Makes the window
    window = tk.Tk()
    window.title("PyWord")
    window.configure(background="white")
    window.minsize(500, 500)
    window.maxsize(1440, 1000)

    # New file function
    def new_file():
        window.title("New File")
        text_box.delete(1.0, tk.END)
        window.update()

    # Open file function
    def open_file():
        filepath = askopenfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        with open(filepath, "r") as input_file:
            text = input_file.read()
            text_box.delete(1.0, tk.END)
            text_box.insert(tk.END, text)
        window.title(f"Open - {filepath}")

    # Save function
    def save():
        filepath = asksaveasfilename(defaultextension="txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = text_box.get(1.0, tk.END)
            output_file.write(text)
        window.title(f"Entitled - {filepath}")

    def size():
        window.title("Change Size")
        ask_size = askinteger("Font Size", "Enter the font size:")
        if ask_size:  # Ensure a value was entered
            current_font = text_box.cget("font").split()
            text_box.config(font=(current_font[1], ask_size))

    def font():
        window.title("Change Font")
        ask_file_font = askyesnocancel("Font list", "Would you like to see the available fonts (Y/N)?")
        if ask_file_font:  # Check if the user clicked 'Yes'
            file_path = f"/fonts.txt"

            if file_path:
                # Read the file and show the available fonts
                with open(file_path, "r") as input_file:
                    text = input_file.read()
                    text_box.delete(1.0, tk.END)
                    text_box.insert(tk.END, text)
                window.title(f"Open - {file_path}")
        elif ask_file_font is False:  # Check if the user clicked 'No'
            ask_font = askstring("Font Name", "Enter the font name:")
            if ask_font:
                current_font = text_box.cget("font").split()
                text_box.config(font=(ask_font, current_font[1]))

    # Button to make a new file
    new_file_btn = Button(window, text="New File", command=new_file)
    new_file_btn.place(x=20, y=0)

    # Button to save a file
    save_btn = Button(window, text="Save", command=save)
    save_btn.place(x=120, y=0)

    # Button to open a file
    new_btn = Button(window, text='Open File', command=open_file)
    new_btn.place(x=220, y=0)

    # Buttons to change size and font
    size_button = Button(window, text="Change Size", command=size)
    size_button.place(x=444, y=0)

    font_button = Button(window, text="Change Font", command=font)
    font_button.place(x=324, y=0)

    # Text box for content
    text_box = Text(window, bg="white", fg="black", font=("Arial", 12))
    text_box.pack(expand=True, fill='both', padx=20, pady=30)

    # Scroll bar to view more.
    scroll = Scrollbar(text_box, orient='vertical', command=text_box.yview)
    scroll.pack(side='right', fill='y')


    window.mainloop()

py_word()