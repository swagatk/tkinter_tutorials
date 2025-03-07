import tkinter as tk

def display_msg():
    msg = text_box.get(1.0, tk.END)
    label_2.config(text=msg)
    text_box.delete(1.0, tk.END)

window = tk.Tk()
label = tk.Label(text="Text Box")
text_box = tk.Text()
btn = tk.Button(text="Submit", command=display_msg)
label.pack()
text_box.pack()
btn.pack(padx=10, pady=10)
lf = tk.LabelFrame(window, text="Output:")
lf.pack(fill="both", expand="no")
btn_2 = tk.Button(text="Quit", command=window.destroy)
label_2 = tk.Label(lf, text="Your message appears here! ")
label_2.pack()
btn_2.pack(padx=10, pady=10)
window.mainloop()