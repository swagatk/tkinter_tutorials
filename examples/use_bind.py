import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)

# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)

lbl = tk.Label(master=window, text="Press any key!")
lbl.pack(padx=20, pady=20)

def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)

button.pack(padx=10, pady=10)

window.mainloop()