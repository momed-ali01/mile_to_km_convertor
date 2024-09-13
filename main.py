from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.689)
    kilometer_result_label["text"] = f"{km}"

window = Tk()
window.title("Miles to Kilometers Convertor")
# window.minsize(width=400, height=250)
window.config(padx=22, pady=22)

miles_input = Entry(width=12)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2, row=1)

calculate_btn = Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(column=1, row=2)

window.mainloop()
