import tkinter as tk
from tkinter import ttk, messagebox #ttk stands for Themed Tkinter
import requests

# Function to open the currency converter window
def open_currency_converter():
    # Check if the window is already open
    if hasattr(open_currency_converter, "window") and open_currency_converter.window.winfo_exists():
        messagebox.showinfo("Info", "Currency Converter is already open!")
        return
    
    # Create the secondary window
    open_currency_converter.window = tk.Toplevel()
    open_currency_converter.window.title("Currency Converter")
    open_currency_converter.window.geometry("400x300")

    # tk.Toplevel() creates a new window that is separate from the main Tkinter window.
# window.title("Currency Converter") sets the title of this new window to "Currency Converter".
# window.geometry("400x300") sets the dimensions of this window to 400 pixels wide by 300 pixels high.
    
    # Currency Converter Layout
    tk.Label(open_currency_converter.window, text="Amount:").pack(pady=5)
    amount_entry = tk.Entry(open_currency_converter.window)
    amount_entry.pack(pady=5)

    tk.Label(open_currency_converter.window, text="From Currency (e.g., USD):").pack(pady=5)

#     tk.Label() creates a label widget to display static text in the window.
# tk.Entry() creates an input field where the user can type their input (like an amount of currency or currency code).
# .pack() is used to organize the placement of widgets in the window with some space (pady=5) around them to make the layout cleaner and more visually appealing.
    
    # Currency options (List of currency codes)
    currencies = ["USD", "INR", "EUR", "GBP", "AUD", "CAD", "JPY"]
    
    from_currency_combobox = ttk.Combobox(open_currency_converter.window, values=currencies)
    from_currency_combobox.pack(pady=5)
    from_currency_combobox.set("USD")  # Default to USD

    tk.Label(open_currency_converter.window, text="To Currency (e.g., INR):").pack(pady=5)
    to_currency_combobox = ttk.Combobox(open_currency_converter.window, values=currencies)
    to_currency_combobox.pack(pady=5)
    to_currency_combobox.set("INR")  # Default to INR

    # Function to fetch exchange rate
    def get_rates(base, target):
        url = f"https://v6.exchangerate-api.com/v6/3269676337e86c378bc829a3/latest/{base}"
        response = requests.get(url)
        data = response.json()
        return data["conversion_rates"].get(target, None)

    def convert_currency():
        try:
            amount = float(amount_entry.get())
            base = from_currency_combobox.get().upper()
            target = to_currency_combobox.get().upper()

            rate = get_rates(base, target)
            if rate:
                result = amount * rate
                result_label.config(text=f"{amount} {base} = {result:.2f} {target}")
            else:
                result_label.config(text="Conversion failed. Check inputs.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid amount.")

    # Conversion result label
    result_label = tk.Label(open_currency_converter.window, text="")
    result_label.pack(pady=10)

    # Convert button
    convert_button = tk.Button(open_currency_converter.window, text="Convert", command=convert_currency)
    convert_button.pack(pady=10)

# Main Window
root = tk.Tk()
root.title("Main Window")
root.geometry("300x200")

# Add Widgets to the Main Window
tk.Label(root, text="Welcome to the Currency Converter App!").pack(pady=20)
tk.Button(root, text="Open Currency Converter", command=open_currency_converter).pack(pady=20)

# Run the Tkinter main loop
root.mainloop()