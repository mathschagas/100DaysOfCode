from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)

def miles_to_km(miles):
    return miles * 1.609

def button_clicked():
    miles = float(miles_input.get())
    new_result = miles_to_km(miles)
    result_label.config(text=new_result)

# Label "is equal to"
equal_to_label = Label(text="is equal to", font=("Verdana"))
equal_to_label.grid(column=0, row=1)

# Label Result
result_label = Label(text="0", font=("Verdana"))
result_label.grid(column=1, row=1)

# Label Km
km_label = Label(text="Km", font=("Verdana"))
km_label.grid(column=2, row=1)

# Label Miles
Miles_label = Label(text="Miles", font=("Verdana"))
Miles_label.grid(column=2, row=0)

# Button Calculate
calculate_button = Button(text="Calculate", font=("Verdana"), command=button_clicked)
calculate_button.grid(column=1, row=2)

# Entry Miles
miles_input = Entry(width=7, font=("Verdana"))
miles_input.grid(column=1, row=0)


window.mainloop()