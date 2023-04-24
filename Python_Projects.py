"""
Here is a Python project using Currency Converter app for 30 countries with a calculator and price sets for each currency:

Project Title: Currency Converter with Calculator

Project Description: This project involves building a currency converter app that can convert between 30 different currencies.
The app also includes a calculator that allows users to perform basic mathematical operations. Users can enter the price of
a product in one currency and the app will convert it to the selected currency.

Project Steps:

1. Install the forex-python library using pip.
2. Create a Python file and import the necessary libraries such as tkinter for GUI, forex_python for currency conversion and
 math for performing mathematical operations.
3. Define a dictionary with 30 different currencies and their corresponding currency codes.
4. Create a GUI using tkinter that includes a drop-down menu to select the input currency, a drop-down menu to
select the output currency, a text box to enter the price, and a label to display the converted price.
5. Create a function to convert the input currency to the output currency using the forex-python library.
6. Create a function to perform mathematical operations such as addition, subtraction, multiplication, and division.
7. Add functionality to the GUI so that when the user enters a price and selects the input and output currencies,
the app will convert the price and display the converted price.
8. Add functionality to the GUI so that when the user performs a mathematical operation, the app will display the result.
9. Set the price of each currency in the dictionary.

10. Test the app by selecting different input and output currencies and performing different mathematical operations.

## Project Output:

The app will display a GUI that allows users to select the input and output currencies, enter the price, and
perform mathematical operations. The app will also display the converted price based on the selected currencies
and the price sets.

"""

import tkinter as tk
from forex_python.converter import CurrencyRates
import math

# Create a dictionary of 30 different currencies and their corresponding currency codes
currencies = {'USD': 'US Dollar', 'EUR': 'Euro', 'GBP': 'British Pound', 'AUD': 'Australian Dollar',
              'CAD': 'Canadian Dollar',
              'SGD': 'Singapore Dollar', 'CHF': 'Swiss Franc', 'INR': 'Indian Rupee', 'JPY': 'Japanese Yen',
              'CNY': 'Chinese Yuan',
              'MXN': 'Mexican Peso', 'MYR': 'Malaysian Ringgit', 'NZD': 'New Zealand Dollar', 'PHP': 'Philippine Peso',
              'THB': 'Thai Baht', 'BRL': 'Brazilian Real', 'HKD': 'Hong Kong Dollar', 'IDR': 'Indonesian Rupiah',
              'KRW': 'South Korean Won', 'TRY': 'Turkish Lira', 'RUB': 'Russian Ruble', 'ZAR': 'South African Rand',
              'AED': 'UAE Dirham', 'ARS': 'Argentine Peso', 'CLP': 'Chilean Peso', 'COP': 'Colombian Peso',
              'EGP': 'Egyptian Pound', 'ILS': 'Israeli Shekel', 'NOK': 'Norwegian Krone', 'SEK': 'Swedish Krona'}

# Create an instance of the CurrencyRates class
c = CurrencyRates()


# Create a function to convert the input currency to the output currency
def convert():
    try:
        input_currency = input_currency_var.get()
        output_currency = output_currency_var.get()
        price = float(price_entry.get())

        # Convert the input currency to USD first, then to the output currency
        usd_price = c.convert(input_currency, 'USD', price)
        result = c.convert(output_currency, 'USD', usd_price)

        result_label.config(text=f'{round(result, 2)} {output_currency}')
    except ValueError:
        result_label.config(text='Invalid input')


# Create a function to perform mathematical operations
def calculate():
    try:
        input_value = float(price_entry.get())
        operation = operation_var.get()
        if operation == 'sqrt':
            result = math.sqrt(input_value)
        elif operation == 'log':
            result = math.log10(input_value)
        elif operation == 'exp':
            result = math.exp(input_value)
        else:
            operand = float(operand_entry.get())
            if operation == '+':
                result = input_value + operand
            elif operation == '-':
                result = input_value - operand
            elif operation == '*':
                result = input_value * operand
            elif operation == '/':
                result = input_value / operand
            result = round(result, 2)

        result_label.config(text=result)
    except ValueError:
        result_label.config(text='Invalid input')


# Create a GUI using tkinter
root = tk.Tk()
root.title('Currency Converter with Calculator')
root.geometry('500x300')

# Create a label for the input currency drop-down menu
input_currency_label = tk.Label(root, text='Input Currency')
input_currency_label.grid(row=0, column=0, padx=10, pady=10)

# Create a variable for the input currency drop-down menu
input_currency_var = tk.StringVar()
input_currency_var.set('USD')

#Create a drop-down menu for the input currency
input_currency_dropdown = tk.OptionMenu(root, input_currency_var, *currencies.keys())
input_currency_dropdown.grid(row=0, column=1, padx=10, pady=10)

#Create a label for the output currency drop-down menu
output_currency_label = tk.Label(root, text='Output Currency')
output_currency_label.grid(row=1, column=0, padx=10, pady=10)

#Create a variable for the output currency drop-down menu
output_currency_var = tk.StringVar()
output_currency_var.set('USD')

#Create a drop-down menu for the output currency
output_currency_dropdown = tk.OptionMenu(root, output_currency_var, *currencies.keys())
output_currency_dropdown.grid(row=1, column=1, padx=10, pady=10)

#Create a label for the price entry field
price_label = tk.Label(root, text='Price')
price_label.grid(row=2, column=0, padx=10, pady=10)

#Create an entry field for the price
price_entry = tk.Entry(root)
price_entry.grid(row=2, column=1, padx=10, pady=10)

#Create a button to convert the currency
convert_button = tk.Button(root, text='Convert', command=convert)
convert_button.grid(row=3, column=0, padx=10, pady=10)

#Create a label to display the result of the currency conversion
result_label = tk.Label(root, text='')
result_label.grid(row=3, column=1, padx=10, pady=10)

#Create a label for the calculator section
calculator_label = tk.Label(root, text='Calculator')
calculator_label.grid(row=4, column=0, padx=10, pady=10)

#Create a variable for the mathematical operation drop-down menu
operation_var = tk.StringVar()
operation_var.set('+')

#Create a drop-down menu for the mathematical operation
operation_dropdown = tk.OptionMenu(root, operation_var, '+', '-', '*', '/', 'sqrt', 'log', 'exp')
operation_dropdown.grid(row=5, column=0, padx=10, pady=10)

#Create a label for the operand entry field
operand_label = tk.Label(root, text='Operand')
operand_label.grid(row=5, column=1, padx=10, pady=10)

#Create an entry field for the operand
operand_entry = tk.Entry(root)
operand_entry.grid(row=5, column=2, padx=10, pady=10)

#Create a button to perform the calculation
calculate_button = tk.Button(root, text='Calculate', command=calculate)
calculate_button.grid(row=6, column=0, padx=10, pady=10)

#Create a label to display the result of the calculation
result_label = tk.Label(root, text='')
result_label.grid(row=6, column=1, padx=10, pady=10)

root.mainloop()