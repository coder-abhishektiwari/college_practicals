import tkinter as tk

def addition():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        sum = num1 + num2
        result_label.config(text=f"Result: {sum}")
    except ValueError:
        result_label.config(text="Please enter valid integers.")
def subtraction():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        sum = num1 - num2
        result_label.config(text=f"Result: {sum}")
    except ValueError:
        result_label.config(text="Please enter valid integers.")
def multiplication():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        sum = num1 * num2
        result_label.config(text=f"Result: {sum}")
    except ValueError:
        result_label.config(text="Please enter valid integers.")       
def division():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        sum = num1 / num2
        result_label.config(text=f"Result: {sum}")
    except ValueError:
        result_label.config(text="Please enter valid integers.")


window = tk.Tk()
window.title("Hisab Kitab")
window.geometry("400x300")

#label
label = tk.Label(window, text="Lets's Calculate two numbers!", font=("Verdana", 16))
label.pack()

#txtframe
txtframe = tk.Frame(window)
txtframe.pack(pady=10)

entry1 = tk.Entry(txtframe, width=25, font=("Verdana"))
entry1.grid(row=1)

entry2 = tk.Entry(txtframe, width=25, font=("Verdana"))
entry2.grid(row=2)

#btnframe
btnframe = tk.Frame(window)
btnframe.pack(pady=10)

#add button
btnAdd = tk.Button(btnframe, text="  +  ", font=("Verdana", 16), command=addition)
btnAdd.grid(row=3)

#subtract button
btnSub = tk.Button(btnframe, text="  -  ", command=subtraction, font=("Verdana", 16))
btnSub.grid(row=3, column=1)

#add button
btnMul = tk.Button(btnframe, text="  x  ", command=multiplication, font=("Verdana", 16))
btnMul.grid(row=3, column=2)

#add button
btnDiv = tk.Button(btnframe, text="  /  ", command=division, font=("Verdana", 16))
btnDiv.grid(row=3, column=3)


#result label
result_label = tk.Label(window, text="Result: ", font=("Verdana", 14))
result_label.pack(pady=40)


window.mainloop()