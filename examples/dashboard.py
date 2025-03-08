import tkinter as tk
import ttkbootstrap as tb



def dashboard():

    root = tb.Window(themename="superhero")
    root.title("Dashboard")
    root.geometry('800x700')

    # meter frame
    label_1 = tb.Label(root, text="Meters", bootstyle="primary", font=("Arial", 16))
    label_1.pack(pady=10)
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
                        amountused=50,
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

    sep_1 = tb.Separator(root, orient="horizontal", bootstyle="primary")
    sep_1.pack(fill="x", padx=10, pady=10)

    label_2 = tb.Label(root, text="Flood Gauges ", bootstyle="primary", font=("Arial", 16))
    label_2.pack(pady=10)

    # gauge frame
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

    gvar1 = tk.IntVar()
    gvar2 = tk.IntVar()
    gvar3 = tk.IntVar()
    gvar4 = tk.IntVar()
    gvar5 = tk.IntVar()
    g_btn_1 = tb.Checkbutton(fframe, bootstyle="success, square-toggle",
                        variable=gvar1, onvalue=1, offvalue=0, 
                        command=lambda :  gauge_1.start() if gvar1.get() == 1 else gauge_1.stop())
    g_btn_1.grid(row=1,column=0, padx=10, pady=10)
    g_btn_2 = tb.Checkbutton(fframe, bootstyle="default, square-toggle",
                        variable=gvar2, onvalue=1, offvalue=0, 
                        command=lambda :  gauge_2.start() if gvar2.get() == 1 else gauge_2.stop())
    g_btn_2.grid(row=1,column=1, padx=10, pady=10)
    g_btn_3 = tb.Checkbutton(fframe, bootstyle="warning, square-toggle",
                        variable=gvar3, onvalue=1, offvalue=0, 
                        command=lambda :  gauge_3.start() if gvar3.get() == 1 else gauge_3.stop())
    g_btn_3.grid(row=1,column=2, padx=10, pady=10)
    g_btn_4 = tb.Checkbutton(fframe, bootstyle="dark, square-toggle",
                        variable=gvar4, onvalue=1, offvalue=0, 
                        command=lambda :  gauge_4.start() if gvar4.get() == 1 else gauge_4.stop())
    g_btn_4.grid(row=1,column=3, padx=10, pady=10)
    g_btn_5 = tb.Checkbutton(fframe, bootstyle="secondary, square-toggle",
                        variable=gvar5, onvalue=1, offvalue=0, 
                        command=lambda :  gauge_5.start() if gvar5.get() == 1 else gauge_5.stop())  
    g_btn_5.grid(row=1,column=4, padx=10, pady=10)

    fframe.pack(padx=10, pady=10)

    sep_2 = tb.Separator(root, orient="horizontal", bootstyle="success")
    sep_2.pack(fill="x", padx=10, pady=10)
    label_3 = tb.Label(root, text="Progress Bars & Scalers", bootstyle="warning", font=("Arial", 16))
    label_3.pack(pady=10)
    # progressbar frame
    pbframe = tb.Frame(root, bootstyle="default")
    pb_1 = tb.Progressbar(pbframe, bootstyle="danger",
                          maximum=100,
                          mode="determinate",
                          length=300,
                          value=20)
    pb_1.grid(row=0, column=0, padx=10, pady=10)

    var1 = tk.IntVar()
    pb_btn_1 = tb.Checkbutton(pbframe, bootstyle="danger, round-toggle",
                        variable=var1, onvalue=1, offvalue=0, 
                        command=lambda :  pb_1.start() if var1.get() == 1 else pb_1.stop())
    pb_btn_1.grid(row=0,column=1, padx=10, pady=10)

    pb_2 = tb.Progressbar(pbframe, bootstyle="warning",
                          maximum=100,
                          mode="determinate",
                          length=300,
                          value=20)
    pb_2.grid(row=1, column=0, padx=10, pady=10)
    var2 = tk.IntVar()
    pb_btn_2 = tb.Checkbutton(pbframe, bootstyle="warning, round-toggle",
                        variable=var2, onvalue=1, offvalue=0, 
                        command=lambda :  pb_2.start() if var2.get() == 1 else pb_2.stop())
    pb_btn_2.grid(row=1,column=1, padx=10, pady=10)
    pb_3 = tb.Progressbar(pbframe, bootstyle="default",
                          maximum=100,
                          mode="determinate",
                          length=300,
                          value=20)
    pb_3.grid(row=2, column=0, padx=10, pady=10)

    var3 = tk.IntVar()
    pb_btn_3 = tb.Checkbutton(pbframe, bootstyle="warning, round-toggle",
                        variable=var3, onvalue=1, offvalue=0, 
                        command=lambda :  pb_3.start() if var3.get() == 1 else pb_3.stop())
    pb_btn_3.grid(row=2,column=1, padx=10, pady=10)

    scale_1 = tb.Scale(pbframe, bootstyle="success",
                        from_=0, to=100,
                        orient="vertical",
                        length=100,
                        value=80)
    scale_1.grid(row=0, column=2, rowspan=3, padx=10, pady=10)
    scale_2 = tb.Scale(pbframe, bootstyle="primary",
                        from_=0, to=100,
                        orient="vertical",
                        length=100,
                        value=10)
    scale_2.grid(row=0, column=3, rowspan=3, padx=10, pady=10)
    scale_3 = tb.Scale(pbframe, bootstyle="warning",
                        from_=0, to=100,
                        orient="vertical",
                        value=20,
                        length=100)
    scale_3.grid(row=0, column=4, rowspan=3, padx=10, pady=10)
    scale_4 = tb.Scale(pbframe, bootstyle="danger",
                        from_=0, to=100,
                        orient="vertical",
                        length=100,
                        value=50)
    scale_4.grid(row=0, column=5, rowspan=3, padx=10, pady=10)
    pbframe.pack()
    sep_3 = tb.Separator(root, orient="horizontal", bootstyle="danger")
    sep_3.pack(fill="x", padx=10, pady=10)

    btn = tb.Button(root, text="Exit", bootstyle="danger", command=root.destroy)
    btn.pack(padx=10, pady=10)

    # sizegrip
    sizegrip = tb.Sizegrip(root, bootstyle="default")
    sizegrip.pack(side="bottom", anchor="se", fill="both", expand=True, padx=10, pady=10)
    root.mainloop()


if __name__ == '__main__':
    dashboard()