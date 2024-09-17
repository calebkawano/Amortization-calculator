import tkinter as tk
from tkinter import messagebox

'''
DEVELOPER: Caleb Kawano
'''
""" This program can be used to create an amortization schedule for a loan.
"""

##### FUNCTION DEFINITIONS #####
def create_schedule(principle, rate, loan_term):
    output = str.format(f"{'Payment Number':^15}{'Payment':^15}{'Interest':^15}{'Principle':^15}{'Balance':^15}\n")

    payment = principle * ((rate * (1 + rate) ** (loan_term * 12)) / ((1 + rate) ** (loan_term * 12) - 1))
    balance = principle

    for i in range(1, 12 * loan_term + 1):
        interest_payment = balance * rate
        principle_payment = payment - interest_payment
        balance -= principle_payment

        output += str.format(f"{i:^15} ${payment:^15,.2f} ${interest_payment:^15,.2f} ${principle_payment:^15,.2f} {balance:^15,.2f}\n")

    return output

##### MAIN PROGRAM #####
def calculate_schedule():
    try:
        principle = float(principle_entry.get())
        if principle <= 0:
            messagebox.showerror("Input Error", "Please enter a positive loan amount.")
            return

        annual_rate = float(rate_entry.get())
        if annual_rate <= 0:
            messagebox.showerror("Input Error", "Please enter a positive annual interest rate.")
            return
        if annual_rate > 30:
            user_response = messagebox.askyesno("High Interest Rate", "The interest rate is high. Are you sure you want to continue?")
            if user_response:
                pass
            else:
                return
        rate = annual_rate / 12 / 100

        loan_term = int(term_entry.get())
        if loan_term <= 0:
            messagebox.showerror("Input Error", "Please enter a positive loan term in years.")
            return

        schedule = create_schedule(principle, rate, loan_term)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, schedule)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Amortization Calculator")

# Add a scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=4, column=2, sticky='ns')

result_text = tk.Text(root, wrap=tk.NONE, width=80, height=20, yscrollcommand=scrollbar.set)
result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

scrollbar.config(command=result_text.yview)

# Create and place the widgets
tk.Label(root, text="Loan Amount: $").grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
principle_entry = tk.Entry(root)
principle_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Annual Interest Rate (%):").grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Loan Term (years):").grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
term_entry = tk.Entry(root)
term_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_schedule)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_text = tk.Text(root, wrap=tk.NONE, width=80, height=20)
result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()


