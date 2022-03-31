import tkinter as tk

window = tk.Tk()
window.title("Dollar to Euro Converter")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_dollars = tk.Entry(master = frm_entry, width = 10)
lbl_dollars = tk.Label(master = frm_entry, text = "\N(US Dollars)"

ent_dollars.grid(row=0, column=0, sticky="e")
lbl_dollars.grid(row=0, column=1, sticky="w")

btn_convert = tk.button(
    master = window,
    text =  "\N{RIGHTWARDS BLACK ARROW}"
)
lbl_result = tk.Label(master=window, text="\N{Euros}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()

import tkinter as tk
