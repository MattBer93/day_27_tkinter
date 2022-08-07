#Create first GUI (Graphical User Interface), a small app to convert US unities in European ones
from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)


# LABEL
my_label = Label(text="I am a Label", font=("Roboto", 24, "bold"))
my_label.pack() #needed to let the label display. In Tkinter, we need to create an element and then display it.

# How to change the kwargs defined atm of the my_label creation?
my_label["text"] = "New Text"
my_label.config(text="New Text")


# BUTTON
def button_clicked():
    text_in_input = input.get()
    my_label.config(text=f"{text_in_input}")

my_button = Button(text="Click me!", command=button_clicked) # Giving only the name of the fc, we're not calling the fc => no parenthesis
my_button.pack()


# ENTRY
entry = Entry(width=10)
entry.insert(END, string="Some text to begin with.") # => Add some initial text
entry.get() # => gets text in entry
entry.pack()


# TEXT
text = Text(height=5, width=30)
text.focus() # => Puts cursor in textbox
text.insert(END, "Example of multi-line text entry.")
text.get("1.0", END) # => Gets current value in textbox at line 1, character 0
text.pack()


# SPINBOX
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# SCALE
def scale_used():
    print(scale.get())
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# CHECKBOX
def checkbutton_used():
    print(checked_state.get()) # => 1 if checked, 0 if not
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()


# RADIO BUTTON
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=1, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# LISTBOX
def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

#How to keep window on the screen
window.mainloop()



# *** NOTES ***
# Default Values and Kwargs (keyword arguments)
# When a fc is created with default values, we don't need to change them when calling it. We can still do it,
# and the original order won't be needed.

# How to create fcs with Unlimited (positional) Arguments
#Ex:
# def add(*args):
#     return sum(args)
#
# sum = add(2, 4, 6, 14, 87)
# print(sum)

#**kwargs: Many Positional Arguments

# ===========
# ***LAYOUT MANAGERS***

# If not used, widgets won't be shown!

# .pack()
# => Places widgets in the most logical way;
#    Difficult to place them in a specific location

# .place(x, y)
# => Places widget in provided coordinates
# (x=0, y=0) => Top left corner

# .grid() - BEST***
# => Divides space in columns and rows
# grid(column=2, row=3)

