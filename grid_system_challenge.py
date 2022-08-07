from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=60)
window.config(padx=100, pady=200)

# LABEL
my_label = Label(text="I am a Label", font=("Roboto", 24, "bold"))
my_label.grid(column=0, row=0)

# BUTTON
def button_clicked():
    my_label.config(text="First button was clicked")

my_button = Button(text="Click me!", command=button_clicked) # Giving only the name of the fc, we're not calling the fc => no parenthesis
my_button.grid(column=1, row=1)


# SECOND BUTTON
def second_button_clicked():
    my_label.config(text="Second Button was clicked")
new_button = Button(text="I'm the new one!", command=second_button_clicked)
new_button.grid(column=2, row=0)


# ENTRY
entry = Entry()
entry.insert(END, string="Some text to begin with.")
entry.grid(column=3, row=2)

window.mainloop()