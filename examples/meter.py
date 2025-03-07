import tkinter as tk
import ttkbootstrap as tb

mroot = tb.Window(themename="superhero")
mroot.title("Meter")
mroot.geometry('500x500')

global counter
counter = 5 

def clicker():
    global counter
    if counter <= 100:
        fuel_meter.configure(amountused=counter)
        counter += 5
        f_btn.configure(text=f'Click me {fuel_meter.amountusedvar.get()}')

def up():
    current_value = fuel_meter.amountusedvar.get() 
    if current_value >= 0 and current_value <= 100:
        fuel_meter.step(5) 

def down():
    current_value = fuel_meter.amountusedvar.get() 
    if current_value >= 0 and current_value <= 100:
        fuel_meter.step(-5)

fuel_meter = tb.Meter(mroot, bootstyle="danger", 
                      subtext="Fuel Available",
                      interactive=True,
                      textright="%",
                      stripethickness=10,
                      #metersize=100,
                      amountused=0,
                      )
fuel_meter.pack(pady=50)

f_btn = tb.Button(mroot, text="Click me 5", command=clicker)
f_btn.pack(pady=20)

f_btn_2 = tb.Button(mroot, text="Step Up 5", command=up)
f_btn_2.pack(pady=20)

f_btn_2 = tb.Button(mroot, text="Step Down 5", command=down)
f_btn_2.pack(pady=20)
mroot.mainloop()