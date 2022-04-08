import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Geography Review")
window.resizable(width=False, height=False)

frm_entry = tk.Frame(master=window)
ent_country = tk.Entry(master = frm_entry, width = 10)
lbl_country = tk.Label(
    master = frm_entry, 
    text = "Choose from china, india, usa, brazil, uk")

ent_country.grid(row=0, column=0, sticky="e")
lbl_country.grid(row=0, column=1, sticky="w")

def country_pic():
    user_country = ent_country.get()
    
    if user_country == "china":
        imgChina = Image.open("china.jpg")
        photoChina = ImageTk.PhotoImage(imgChina)
        lblChina = tk.Label(window, image = photoChina)
        lblChina.grid(row=0, column=5)
        lblChina()
    elif user_country == "india":
        imgIndia = Image.open("india.jpg")
        photoIndia = ImageTk.PhotoImage(imgIndia)
        lblIndia = tk.Label(window, image = photoIndia)
        lblIndia.grid(row=0, column=5)
        lblIndia()
    elif user_country == "usa":
        imgUSA = Image.open("usa.jpg")
        photoUSA = ImageTk.PhotoImage(imgUSA)
        lblUSA = tk.Label(window, image = photoUSA)
        lblUSA.grid(row=0, column=5)
        lblUSA()
    elif user_country == "brazil":
        imgBrazil = Image.open("brazil.jpg")
        photoBrazil = ImageTk.PhotoImage(imgBrazil)
        lblBrazil = tk.Label(window, image = photoBrazil)
        lblBrazil.grid(row=0, column=5)
        lblBrazil()
    elif user_country == "uk":
        imgUK = Image.open("uk.jpg")
        photoUK = ImageTk.PhotoImage(imgUK)
        lblUK = tk.Label(window, image = photoUK)
        lblUK.grid(row=0, column=5)
        lblUK()

lbl_result = tk.Label(master=window, text = " ")

btn_convert = tk.Button(
master=window,
text="\N{RIGHTWARDS BLACK ARROW}",
command = country_pic
)

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()