from tkinter import *

def miles_to_km():
    miles = float(numb_miles.get())
    km = miles * 1.609
    numb_km.config(text=f"{km}")

window = Tk()
window.title("Mile to Km Converter")
# window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

numb_miles = Entry(width=10)
numb_miles.grid(column=1, row=0)

my_label = Label(text="is equal to", font=("Arial", 15, "bold"))
my_label.grid(column=0, row=1)

miles = Label(text="Miles", font=("Arial", 12, "bold"))
miles.grid(column=2, row=0)

numb_km = Label(text="0")
numb_km.grid(column=1, row=1)

km_l = Label(text="Km")
km_l.grid(column=2, row=1)
# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)



window.mainloop()