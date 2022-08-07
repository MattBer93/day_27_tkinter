from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


# Converting function
def convert(parameter):
    value = int(entry.get())
    value_in_miles = round(value * 1.60934, 2)
    converted_unit.config(text=f"{value_in_miles}")


# LABELS
label = Label(text="Is equal to:", font=("Roboto", 15))
label.grid(column=0, row=1)

miles_label = Label(text="Miles", font=("Roboto", 15, "bold"))
miles_label.grid(column=2, row=0)

km_label = Label(text="Km", font=("Roboto", 15, "bold"))
km_label.grid(column=2, row=1)

converted_unit = Label(text="0")
converted_unit.grid(column=1, row=1)


calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)


# ENTRY
entry = Entry(width=5)
entry.grid(column=1, row=0)

window.bind("<Return>", convert)


window.mainloop()