import tkinter as tk
from tkinter import messagebox

# Function to handle login
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Simple validation with a hardcoded username and password
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")

# Create the main window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")
root.configure(bg="light pink")

# Create and place labels and text entry widgets
label_username = tk.Label(root, text="Username", bg="light pink")
label_username.pack(pady=10)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password", bg="light pink")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*")  # Password field with hidden characters
entry_password.pack(pady=5)

# Create and place the login button
login_button = tk.Button(root, text="Login", command=login, bg="purple", fg="white")
login_button.pack(pady=20)

# Run the application
root.mainloop()
