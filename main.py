# Adding two numbers

from tkinter import *

window = Tk()

first_number = Label(window, text="Enter first number")
first_number.grid(column=1, row=1)

second_number = Label(window, text="Enter second number")
second_number.grid(column=1, row=2)

answer_label = Label(window, text="Your answer")
answer_label.grid(column=1, row=3)

first_number_entry = Entry(window)
first_number_entry.grid(column=2, row=1)

second_number_entry = Entry(window)
second_number_entry.grid(column=2, row=2)

answer_entry = Entry(window, state="readonly")
answer_entry.grid(column=2, row=3)

def add_two_numbers():
    result = sum(int(i.get()) for i in (first_number_entry, second_number_entry))
    answer_entry.config(state="normal")
    answer_entry.insert(0, result)
    answer_entry.config(state="readonly")

def clear():
    first_number_entry.delete(0, END)
    second_number_entry.delete(0, END)
    answer_entry.config(state="normal")
    answer_entry.delete(0, END)
    answer_entry.config(state="readonly")

add = Button(window, text="add", command=add_two_numbers)
add.grid(column=1, row=4)

clear = Button(window, text="clear", command=clear)
clear.grid(column=2, row=4)

exit_button = Button(window, text="exit", command="exit")
exit_button.grid(column=3, row=4)

window.mainloop()
