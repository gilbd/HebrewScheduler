import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import configuration


class HebrewSchedulerGUI(object):
    def __init__(self, input_handler):
        self.input_handler = input_handler
        self.root = tk.Tk(className=' HebrewScheduler')
        s = ttk.Style(self.root)
        s.theme_use('clam')
        tk.Label(self.root, text="Summary").grid(row=0)
        tk.Label(self.root, text="Description").grid(row=1)
        tk.Label(self.root, text="Location").grid(row=2)
        tk.Label(self.root, text="Number of years").grid(row=3)
        tk.Label(self.root, text="Color").grid(row=4)
        ttk.Button(self.root, text='Calendar', command=self.open_calendar).grid(row=5)

        self.summary = tk.Entry(self.root)
        self.desc = tk.Entry(self.root)
        self.loc = tk.Entry(self.root)
        self.num_of_years = tk.Entry(self.root)

        self.color_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, height=len(configuration.COLOR_CODES))
        for i, (c_n, c) in enumerate(zip(configuration.COLOR_CODES_LEGEND.keys(), configuration.COLOR_CODES)):
            self.color_listbox.insert("end", c_n)
            self.color_listbox.itemconfig(i, {'bg': c})

        self.summary.grid(row=0, column=1)
        self.desc.grid(row=1, column=1)
        self.loc.grid(row=2, column=1)
        self.num_of_years.grid(row=3, column=1)
        self.color_listbox.grid(row=4, column=1)

        self.top = None
        self.cal = None

    def open_calendar(self):
        self.top = tk.Toplevel(self.root)
        ttk.Label(self.top, text='Choose date').pack(padx=10, pady=10)
        self.cal = Calendar(self.top,
                            font="Arial 14", selectmode='day',
                            cursor="hand1")
        self.cal.pack(fill="both", expand=True)
        ttk.Button(self.top, text="ok", command=self.process_inputs).pack()

    def process_inputs(self):
        picked_vals = (self.cal.selection_get(),
                       self.summary.get(),
                       self.desc.get(),
                       self.loc.get(),
                       configuration.COLOR_CODES_LEGEND[self.color_listbox.selection_get()],
                       int(self.num_of_years.get()))
        print(picked_vals)
        self.top.destroy()
        self.root.destroy()
        self.input_handler(*picked_vals)

    def run_gui(self):
        self.root.mainloop()
