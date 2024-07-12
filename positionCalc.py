import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import font
from datetime import datetime


def calculate_x(total_capital, stop_loss_percentage, risk_percentage, leverage):
    stop_loss_decimal = stop_loss_percentage / 100
    risk_decimal = risk_percentage / 100

    
    x = (total_capital * risk_decimal) / (stop_loss_decimal * leverage)
    return x

def calculate_and_display():
    try:
        total_capital = float(total_capital_entry.get())
        stop_loss_percentage = float(stop_loss_entry.get())
        risk_percentage = float(risk_entry.get())
        leverage = float(leverage_entry.get())

        result = calculate_x(total_capital, stop_loss_percentage, risk_percentage, leverage)
        result_label.config(text=f"The value of x is: {result:.2f}")

        with open("calculations.txt", "a") as file:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{now} - x: {result:.2f}\n")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")


def close_app():
    root.destroy()

def restart_app():
    total_capital_entry.delete(0, tk.END)
    stop_loss_entry.delete(0, tk.END)
    risk_entry.delete(0, tk.END)
    leverage_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Position Calculator")
root.geometry("530x360")  # Set window size
root.bind("<Control-r>", lambda event: restart_app())
root.bind("<Escape>", lambda event: close_app())
root.bind("<Return>", lambda event: calculate_and_display())

# Set font to 'Kode Mono'

# font_style = ("Kode", 12)
# default_font=tkFont.Font(family="Kode",name="Kode",font="Kode",size=8)
default_font = ("Kode",10)



# Create input fields
total_capital_label = tk.Label(root, text="Total Capital:",font=default_font)
total_capital_entry = tk.Entry(root,font=default_font)
stop_loss_label = tk.Label(root, text="Stop Loss Percentage:",font=default_font)
stop_loss_entry = tk.Entry(root,font=default_font)
risk_label = tk.Label(root, text="Risk Percentage:",font=default_font)
risk_entry = tk.Entry(root,font=default_font)
leverage_label = tk.Label(root, text="Leverage:",font=default_font)
leverage_entry = tk.Entry(root,font=default_font)

# Create buttons
calculate_button = tk.Button(root, text="Calculate", command=calculate_and_display,font=default_font)
close_button = tk.Button(root, text="Close", command=close_app,font=default_font)
restart_button = tk.Button(root, text="Restart", command=restart_app,font=default_font)


# Create result label
result_label = tk.Label(root, text="",font=default_font,foreground="blue")

# Arrange widgets
total_capital_label.grid(row=0, column=0,ipadx=55,ipady=5)
total_capital_entry.grid(row=0, column=1)
stop_loss_label.grid(row=1, column=0,ipadx=55,ipady=5)
stop_loss_entry.grid(row=1, column=1)
risk_label.grid(row=2, column=0,ipadx=55,ipady=5)
risk_entry.grid(row=2, column=1)
leverage_label.grid(row=3, column=0,ipadx=55,ipady=5)
leverage_entry.grid(row=3, column=1)
calculate_button.grid(row=4, pady=10)
result_label.grid(row=5, column=0, columnspan=2,pady=10,ipadx=50)
close_button.grid(row=6, column=0,pady=20)
restart_button.grid(row=6, column=1,pady=20)

current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
date_label = tk.Label(root, text=f"Date: {current_date}", font=default_font)
date_label.grid(row=7, column=0, columnspan=2, pady=10)
root.mainloop()
