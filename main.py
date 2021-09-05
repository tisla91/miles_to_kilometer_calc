from tkinter import *

mile = Tk()
mile.title("Mile to Kilometer calculator")
mile.minsize(width = 300, height = 300)
mile.config(padx = 20, pady = 20)

mile_label = Label(text = "Is equal to", font = ("Arial", 15, "italic"))
mile_label.grid(column = 0, row = 1)
mile_label.config(padx = 10, pady = 10)

mile_entry = Entry(width = 8)
mile_entry.get()
mile_entry.grid(column = 1, row = 0)

mile_label2 = Label(text = "  ")
mile_label2.grid(column = 1, row = 1)


def calculate():
    mile = float(mile_entry.get())
    km = mile * 1.60934
    mile_label2.config(text = f"{km}")
mile_button = Button(text = "Calculate", height = 2, width = 7, command = calculate)
mile_button.grid(column = 1, row = 3)
mile_button.config(padx = 10, pady = 10)


mile_label3 = Label(text = "Mile", font =("Arial", 10))
mile_label3.grid(column = 3, row = 0)
mile_label3.config(padx = 10, pady = 10)

mile_label4 = Label(text = "Km", font =("Arial", 10))
mile_label4.grid(column = 3, row = 1)
mile_label4.config(padx = 10, pady = 10)

mile.mainloop()