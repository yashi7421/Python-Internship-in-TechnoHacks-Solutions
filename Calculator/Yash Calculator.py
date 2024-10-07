import tkinter as tk

# Function to update the input field when buttons are clicked
def button_click(value):
    current = input_field.get()
    input_field.delete(0, tk.END)
    input_field.insert(0, current + str(value))

# Function to clear the input field
def button_clear():
    input_field.delete(0, tk.END)

# Function to evaluate the expression entered in the input field
def button_equal():
    try:
        result = eval(input_field.get())
        input_field.delete(0, tk.END)
        input_field.insert(0, str(result))
    except:
        input_field.delete(0, tk.END)
        input_field.insert(0, "Error")

# Creating the main window
root = tk.Tk()
root.title("Yash Calculator")  # Adding your name to the title

# Input field where the expression will be displayed
input_field = tk.Entry(root, width=40, borderwidth=5)
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Defining buttons
buttons = [
    ('%', 1, 0), ('CE', 1, 1), ('C', 1, 2), ('⌫', 1, 3),
    ('1/x', 2, 0), ('x²', 2, 1), ('√x', 2, 2), ('/', 2, 3),
    (7, 3, 0), (8, 3, 1), (9, 3, 2), ('*', 3, 3),
    (4, 4, 0), (5, 4, 1), (6, 4, 2), ('-', 4, 3),
    (1, 5, 0), (2, 5, 1), (3, 5, 2), ('+', 5, 3),
    ('+/-', 6, 0), (0, 6, 1), ('.', 6, 2), ('=', 6, 3)
]

# Adding buttons to the grid
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=30, pady=20, command=button_equal)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=30, pady=20, command=button_clear)
    else:
        btn = tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: button_click(t))
    btn.grid(row=row, column=col)

# Running the application
root.mainloop()