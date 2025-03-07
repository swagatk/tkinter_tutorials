import tkinter as tk
import ttkbootstrap as tb



def dashboard():

    root = tb.Window(themename="superhero")
    root.title("Dashboard")
    root.geometry('800x500')

    mframe= tb.Frame(root, bootstyle="default")

    f_meter = tb.Meter(mframe, bootstyle="danger", 
                        subtext="Fuel Available",
                        interactive=True,
                        textright="%",
                        stripethickness=10,
                        metersize=150,
                        amountused=20,
                        )
    f_meter.grid(row=0, column=0, padx=10, pady=10)

    t_meter = tb.Meter(mframe, bootstyle="primary", 
                        subtext="Temperature",
                        interactive=True,
                        textright="\N{DEGREE CELSIUS}",
                        #stripethickness=10,
                        metersize=150,
                        amountused=20,
                        metertype="semi",
                        amounttotal=50
                        )

    t_meter.grid(row=0, column=1, padx=10, pady=10)

    v_meter = tb.Meter(mframe, bootstyle="warning", 
                        subtext="Ventilation",
                        interactive=True,
                        textright="%",
                        stripethickness=5,
                        metersize=150,
                        amountused=20,
                        metertype="full",
                        amounttotal=100
                        )

    v_meter.grid(row=0, column=2, padx=10, pady=10)

    c_meter = tb.Meter(mframe, bootstyle="success", 
                        subtext="Capacity",
                        interactive=True,
                        textright="%",
                        stripethickness=2,
                        metersize=150,
                        amountused=20,
                        metertype="full",
                        amounttotal=100
                        )

    c_meter.grid(row=0, column=3, padx=10, pady=10)
    mframe.pack(padx=10, pady=10)

    fframe = tb.Frame(root, bootstyle="default")

    gauge_1 = tb.Floodgauge(fframe, bootstyle="success",
                            mask="Progress: {}%",
                            maximum=100,
                            orient="horizontal",
                            value=20)
    gauge_1.grid(row=0, column=0, padx=10, pady=10)
    gauge_2 = tb.Floodgauge(fframe, bootstyle="default",
                            mask="Memory Used: {}%",
                            maximum=100,
                            orient="horizontal",
                            value=70)
    gauge_2.grid(row=0, column=1, padx=10, pady=10)

    gauge_3 = tb.Floodgauge(fframe, bootstyle="warning",
                            mask=" Workload: {}%",
                            maximum=100,
                            orient="horizontal",
                            value=30)
    gauge_3.grid(row=0, column=2, padx=10, pady=10)

    gauge_4 = tb.Floodgauge(fframe, bootstyle="dark",
                            mask=" Storage: {}%",
                            maximum=100,
                            orient="horizontal",
                            value=30)
    gauge_4.grid(row=0, column=3, padx=10, pady=10)
    gauge_5 = tb.Floodgauge(fframe, bootstyle="secondary",
                            mask=" Boost: {}%",
                            maximum=100,
                            orient="horizontal",
                            value=30)
    gauge_5.grid(row=0, column=4, padx=10, pady=10)

    fframe.pack(padx=10, pady=10)

    pbframe = tb.Frame(root, bootstyle="default")
    pb_1 = tb.Progressbar(pbframe, bootstyle="danger",
                          maximum=100,
                          mode="determinate",
                          length=300,
                          value=20)
    pb_1.grid(row=0, column=0, padx=10, pady=10)

    pb_btn_1 = tb.Button(pbframe, text="Start", bootstyle="default", command=lambda: pb_1.start())
    pb_btn_2 = tb.Button(pbframe, text="Stop", bootstyle="default", command=lambda: pb_1.stop())
    pb_btn_1.grid(row=0,column=1, padx=10, pady=10)
    pb_btn_2.grid(row=0,column=2, padx=10, pady=10)

    pb_2 = tb.Progressbar(pbframe, bootstyle="warning",
                          maximum=100,
                          mode="determinate",
                          length=300,
                          value=20)
    pb_2.grid(row=1, column=0, padx=10, pady=10)

    pb_3 = tb.Progressbar(pbframe, bootstyle="default",
                          maximum=100,
                          mode="determinate",
                          length=300,
                          value=20)
    pb_3.grid(row=2, column=0, padx=10, pady=10)

    pbframe.pack()
    root.mainloop()

if __name__ == '__main__':
    dashboard()