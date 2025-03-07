import tkinter as tk
def display_name():
    name = entry.get()
    print('Your name is: ', name)

window = tk.Tk()
label = tk.Label(text="Name")
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.insert(0, "Enter your name here!")

btn = tk.Button(text="Submit", command=display_name)
label.pack()
entry.pack()
btn.pack()
window.mainloop()