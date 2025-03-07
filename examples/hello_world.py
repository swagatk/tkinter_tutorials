import tkinter as tk

# create root window
root = tk.Tk()

# frame inside root window
frame = tk.Frame(root)

# geometry method
frame.pack()

# button inside frame which is
# inside root
button = tk.Button(frame, text='Hello World!')
button.pack()

# Tkinter event loop
root.mainloop()

