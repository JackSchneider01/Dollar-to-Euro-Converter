import tkinter as tk

def dollar_to_euros():
    """Convert the users given value for US Dollars to Euros and insert
    the result into lbl_result.
    """
    usd = ent_dollars.get()
    euros = (1.1045) * (float(usd))
    lbl_result["text"] = f"{round(euros, 3)} euros"

window = tk.Tk()
window.title("Dollar to Euro Converter")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_dollars = tk.Entry(master = frm_entry, width = 10)
lbl_dollars = tk.Label(master = frm_entry, text = "US Dollar")

ent_dollars.grid(row=0, column=0, sticky="e")
lbl_dollars.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(
master=window,
text="\N{RIGHTWARDS BLACK ARROW}",
command = dollar_to_euros
)
lbl_result = tk.Label(master=window, text="euros")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()