import tkinter as tk

window = tk.Tk()

label = tk.Label(text="Hello World!",
                fg="white",  # Set the text color to white
                bg="black" , # Set the background color to black)
                width=10,
                height=10
                )
label.pack()
window.mainloop()