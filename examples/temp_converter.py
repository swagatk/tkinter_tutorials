import tkinter as tk
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# entry frame 1 
frm_1_entry = tk.Frame(master=window)
ent_1_temperature = tk.Entry(master=frm_1_entry, width=10)
lbl_1_temp = tk.Label(master=frm_1_entry, text="\N{DEGREE FAHRENHEIT}")

ent_1_temperature.grid(row=0, column=0, sticky="e")
lbl_1_temp.grid(row=0, column=1, sticky="w")

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_1_temperature.get()
    celsius = (5. / 9) * (float(fahrenheit) - 32)
    lbl_1_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


btn_1_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)

lbl_1_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frm_1_entry.grid(row=0, column=0, padx=10)
btn_1_convert.grid(row=0, column=1, pady=10)
lbl_1_result.grid(row=0, column=2, padx=10)

# entry frame 2
frm_2_entry = tk.Frame(master=window)
ent_2_temperature = tk.Entry(master=frm_2_entry, width=10)
lbl_2_temp = tk.Label(master=frm_2_entry, text="\N{DEGREE CELSIUS}")

ent_2_temperature.grid(row=0, column=0, sticky="e")
lbl_2_temp.grid(row=0, column=1, sticky="w")

def celsius_to_fahrenheit():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    celsius = ent_2_temperature.get()
    fahrenheit = 9* float(celsius) / 5 + 32
    lbl_2_result["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"

btn_2_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=celsius_to_fahrenheit
)
lbl_2_result = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")

frm_2_entry.grid(row=1, column=0, padx=10)
btn_2_convert.grid(row=1, column=1, pady=10)
lbl_2_result.grid(row=1, column=2, padx=10)


window.mainloop()