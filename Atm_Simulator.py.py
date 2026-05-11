from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Simple ATM Simulator")
root.geometry("400x350")
root.resizable(False, False)

balance = 0.0

def check_balance():
    messagebox.showinfo("Balance", f"Your current balance is: ${balance:.2f}")


def deposit():
    global balance

    try:
        amount = float(entry_amount.get())

        if amount <= 0:
            messagebox.showerror("Error", "Deposit amount must be greater than 0.")
        else:
            balance += amount
            messagebox.showinfo("Success", f"Successfully deposited ${amount:.2f}")
            update_balance()

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

    entry_amount.delete(0, END)


def withdraw():
    global balance

    try:
        amount = float(entry_amount.get())

        if amount <= 0:
            messagebox.showerror("Error", "Withdrawal amount must be greater than 0.")

        elif amount > balance:
            messagebox.showerror("Error", "Insufficient balance.")

        else:
            balance -= amount
            messagebox.showinfo("Success", f"Successfully withdrew ${amount:.2f}")
            update_balance()

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

    entry_amount.delete(0, END)


def update_balance():
    balance_label.config(text=f"Current Balance: ${balance:.2f}")


title_label = Label(
    root,
    text="SIMPLE ATM SIMULATOR",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=15)

balance_label = Label(
    root,
    text="Current Balance: $0.00",
    font=("Arial", 14)
)
balance_label.pack(pady=10)

entry_amount = Entry(root, font=("Arial", 14), justify="center")
entry_amount.pack(pady=10)

btn_check = Button(
    root,
    text="Check Balance",
    font=("Arial", 12),
    width=20,
    command=check_balance
)
btn_check.pack(pady=5)

btn_deposit = Button(
    root,
    text="Deposit",
    font=("Arial", 12),
    width=20,
    bg="lightgreen",
    command=deposit
)
btn_deposit.pack(pady=5)

btn_withdraw = Button(
    root,
    text="Withdraw",
    font=("Arial", 12),
    width=20,
    bg="lightcoral",
    command=withdraw
)
btn_withdraw.pack(pady=5)

btn_exit = Button(
    root,
    text="Exit",
    font=("Arial", 12),
    width=20,
    bg="gray",
    fg="white",
    command=root.destroy
)
btn_exit.pack(pady=15)

root.mainloop()