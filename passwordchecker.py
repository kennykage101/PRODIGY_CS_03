import string
import re

def check_password_complexity(password, min_length=8):
    strength = 0
    feedback = []

    if len(password) < min_length:
        feedback.append(f"Password is too short. It should be at least {min_length} characters long.")
    else:
        strength += 1

    if not any(char in string.ascii_uppercase for char in password):
        feedback.append("Password should contain at least one uppercase letter.")
    else:
        strength += 1

    if not any(char in string.ascii_lowercase for char in password):
        feedback.append("Password should contain at least one lowercase letter.")
    else:
        strength += 1

    if not any(char in string.digits for char in password):
        feedback.append("Password should contain at least one number.")
    else:
        strength += 1

    if not any(char in string.punctuation for char in password):
        feedback.append("Password should contain at least one special character.")
    else:
        strength += 1

    return strength, "\n".join(feedback)

def get_password_strength(strength):
    strength_map = {
        0: "Weak",
        1: "Weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Strong"
    }
    return strength_map.get(strength, "Weak")

import tkinter as tk
from tkinter import messagebox

class PasswordComplexityChecker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Complexity Checker")

        self.password_label = tk.Label(self.window, text="Enter a password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.window, show="*")
        self.password_entry.pack()

        self.check_button = tk.Button(self.window, text="Check Password", command=self.check_password)
        self.check_button.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

    def check_password(self):
        password = self.password_entry.get()
        strength, feedback = check_password_complexity(password)
        password_strength = get_password_strength(strength)
        self.result_label.config(text=f"Password strength: {password_strength}\n{feedback}")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    checker = PasswordComplexityChecker()
    checker.run()
