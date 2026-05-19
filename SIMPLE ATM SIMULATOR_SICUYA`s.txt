import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ATM:
    def __init__(self):
        self.balance = 1000
        self.pin = "1234"

    def check_pin(self, entered_pin):
        return entered_pin == self.pin

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount!"
        self.balance += amount
        return f"₱{amount:.2f} deposited successfully."

    def withdraw(self, amount):
        if amount <= self.balance and amount > 0:
            self.balance -= amount
            return f"₱{amount:.2f} withdrawn successfully."
        elif amount <= 0:
            return "Invalid amount!"
        else:
            return "Insufficient balance!"

    def get_balance(self):
        return self.balance


atm = ATM()

root = tk.Tk()
root.title("Modern ATM Machine")
root.geometry("500x600")
root.configure(bg="#0f172a")
root.resizable(False, False)

style = ttk.Style()
style.theme_use("clam")

BG = "#0f172a"
CARD = "#1e293b"
BTN = "#2563eb"
BTN2 = "#16a34a"
BTN3 = "#dc2626"
TEXT = "#f8fafc"
ENTRY = "#334155"

login_frame = tk.Frame(root, bg=BG)
menu_frame = tk.Frame(root, bg=BG)

login_card = tk.Frame(
    login_frame,
    bg=CARD,
    padx=40,
    pady=40
)
login_card.place(relx=0.5, rely=0.5, anchor="center")

title = tk.Label(
    login_card,
    text="🏧 ATM MACHINE",
    font=("Helvetica", 22, "bold"),
    bg=CARD,
    fg=TEXT
)
title.pack(pady=20)

subtitle = tk.Label(
    login_card,
    text="Secure Banking System",
    font=("Helvetica", 11),
    bg=CARD,
    fg="#cbd5e1"
)
subtitle.pack(pady=5)

tk.Label(
    login_card,
    text="Enter PIN",
    font=("Helvetica", 12),
    bg=CARD,
    fg=TEXT
).pack(pady=10)

pin_entry = tk.Entry(
    login_card,
    show="●",
    font=("Helvetica", 16),
    width=18,
    justify="center",
    bd=0,
    bg=ENTRY,
    fg="white",
    insertbackground="white"
)
pin_entry.pack(ipady=8, pady=10)


def login():
    pin = pin_entry.get()

    if atm.check_pin(pin):
        messagebox.showinfo("Success", "Login Successful!")
        login_frame.pack_forget()
        menu_frame.pack(fill="both", expand=True)
    else:
        messagebox.showerror("Error", "Incorrect PIN!")


login_btn = tk.Button(
    login_card,
    text="LOGIN",
    font=("Helvetica", 12, "bold"),
    bg=BTN,
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    bd=0,
    width=18,
    height=2,
    cursor="hand2",
    command=login
)
login_btn.pack(pady=20)

login_frame.pack(fill="both", expand=True)

# ================= MENU PAGE =================
header = tk.Frame(menu_frame, bg="#111827", height=80)
header.pack(fill="x")

header_label = tk.Label(
    header,
    text="WELCOME TO ATM",
    font=("Helvetica", 20, "bold"),
    bg="#111827",
    fg="white"
)
header.pack(pady=20)

balance_card = tk.Frame(
    menu_frame,
    bg=CARD,
    padx=30,
    pady=25
)
balance_card.pack(pady=30)

balance_title = tk.Label(
    balance_card,
    text="Current Balance",
    font=("Helvetica", 14),
    bg=CARD,
    fg="#cbd5e1"
)
balance_title.pack()

balance_label = tk.Label(
    balance_card,
    text=f"₱{atm.get_balance():,.2f}",
    font=("Helvetica", 28, "bold"),
    bg=CARD,
    fg="#38bdf8"
)
balance_label.pack(pady=10)

tk.Label(
    menu_frame,
    text="Enter Amount",
    font=("Helvetica", 13),
    bg=BG,
    fg=TEXT
).pack()

amount_entry = tk.Entry(
    menu_frame,
    font=("Helvetica", 16),
    justify="center",
    width=18,
    bd=0,
    bg=ENTRY,
    fg="white",
    insertbackground="white"
)
amount_entry.pack(ipady=10, pady=15)


def update_balance():
    balance_label.config(text=f"₱{atm.get_balance():,.2f}")


def get_amount():
    try:
        return float(amount_entry.get())
    except:
        messagebox.showerror("Error", "Enter a valid number!")
        return None


def deposit_money():
    amount = get_amount()

    if amount is not None:
        result = atm.deposit(amount)
        messagebox.showinfo("Deposit", result)
        update_balance()
        amount_entry.delete(0, tk.END)


def withdraw_money():
    amount = get_amount()

    if amount is not None:
        result = atm.withdraw(amount)
        messagebox.showinfo("Withdraw", result)
        update_balance()
        amount_entry.delete(0, tk.END)


button_frame = tk.Frame(menu_frame, bg=BG)
button_frame.pack(pady=20)

deposit_btn = tk.Button(
    button_frame,
    text="Deposit",
    font=("Helvetica", 12, "bold"),
    bg=BTN2,
    fg="white",
    width=15,
    height=2,
    bd=0,
    cursor="hand2",
    command=deposit_money
)
deposit_btn.grid(row=0, column=0, padx=10, pady=10)

withdraw_btn = tk.Button(
    button_frame,
    text="Withdraw",
    font=("Helvetica", 12, "bold"),
    bg=BTN3,
    fg="white",
    width=15,
    height=2,
    bd=0,
    cursor="hand2",
    command=withdraw_money
)
withdraw_btn.grid(row=0, column=1, padx=10, pady=10)

check_btn = tk.Button(
    button_frame,
    text="Check Balance",
    font=("Helvetica", 12, "bold"),
    bg=BTN,
    fg="white",
    width=32,
    height=2,
    bd=0,
    cursor="hand2",
    command=lambda: messagebox.showinfo(
        "Balance",
        f"Current Balance:\n₱{atm.get_balance():,.2f}"
    )
)
check_btn.grid(row=1, column=0, columnspan=2, pady=10)

exit_btn = tk.Button(
    menu_frame,
    text="EXIT",
    font=("Helvetica", 12, "bold"),
    bg="#475569",
    fg="white",
    width=20,
    height=2,
    bd=0,
    cursor="hand2",
    command=root.quit
)
exit_btn.pack(pady=20)

footer = tk.Label(
    menu_frame,
    text="© 2026 Secure ATM System",
    font=("Helvetica", 9),
    bg=BG,
    fg="#94a3b8"
)
footer.pack(side="bottom", pady=10)

root.mainloop()