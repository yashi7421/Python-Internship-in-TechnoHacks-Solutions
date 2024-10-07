import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

# Function to convert currency
def convert_currency():
    try:
        # Check if amount is entered and is a valid number
        amount = amount_entry.get()
        if not amount:
            converted_amount_var.set("Enter amount")
            return
        try:
            amount = float(amount)
        except ValueError:
            converted_amount_var.set("Invalid amount")
            return

        # Get the selected currencies
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()
        
        # Check if both currencies are selected
        if from_currency == '' or to_currency == '':
            converted_amount_var.set("Select both currencies")
            return
        
        # Fetch the exchange rate and convert the amount
        c = CurrencyRates()
        converted_amount = c.convert(from_currency, to_currency, amount)
        
        # Display the result
        converted_amount_var.set(f"{converted_amount:.2f}")
    except Exception as e:
        print(f"Error occurred: {e}")  # This will print the actual error in the terminal/console
        converted_amount_var.set("Conversion error")

# Function to clear all fields
def clear_all():
    amount_entry.delete(0, tk.END)
    from_currency_combo.set('Select currency')
    to_currency_combo.set('Select currency')
    converted_amount_var.set('')

# Creating the main window
root = tk.Tk()
root.title("Currency Converter Developed By YASH")

# Create and set variables for storing the converted amount
converted_amount_var = tk.StringVar()

# Labels
tk.Label(root, text="Amount :", font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
tk.Label(root, text="From Currency :", font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
tk.Label(root, text="To Currency :", font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
tk.Label(root, text="Converted Amount :", font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10, sticky=tk.W)

# Entry box for amount
amount_entry = tk.Entry(root, width=20)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

# Currency dropdowns
currency_options = ['INR', 'USD', 'CAD', 'CNY', 'DKK', 'EUR']

from_currency_combo = ttk.Combobox(root, values=currency_options, width=17)
from_currency_combo.grid(row=1, column=1, padx=10, pady=10)
from_currency_combo.set('Select currency')

to_currency_combo = ttk.Combobox(root, values=currency_options, width=17)
to_currency_combo.grid(row=2, column=1, padx=10, pady=10)
to_currency_combo.set('Select currency')

# Converted amount label
converted_amount_label = tk.Label(root, text="", textvariable=converted_amount_var, font=('Arial', 12), width=20)
converted_amount_label.grid(row=4, column=1, padx=10, pady=10)

# Convert and Clear buttons
convert_button = tk.Button(root, text="Convert", font=('Arial', 12), bg="light blue", command=convert_currency)
convert_button.grid(row=3, column=1, padx=10, pady=10, sticky=tk.W)

clear_button = tk.Button(root, text="Clear All", font=('Arial', 12), bg="light blue", command=clear_all)
clear_button.grid(row=5, column=1, padx=10, pady=10, sticky=tk.W)

# Running the application
root.mainloop()
