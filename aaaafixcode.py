import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def add_item():
    item = entry.get()
    if item:
        listbox.insert(tk.END, item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Item", "Please enter an item before adding.")

def remove_item():
    selected_indices = listbox.curselection()
    for index in selected_indices[::-1]:
        listbox.delete(index)
        
def login():
    entered_pin = pin_entry.get()
    if entered_pin == "1234":
        messagebox.showinfo("Login Successful", "You have successfully logged in!")
        pin_entry.delete(0, tk.END)
        show_item_manager()
    else:
        messagebox.showerror("Login Failed", "Incorrect PIN. Please try again.")

def sign_up():
    username = username_entry.get()
    password = password_entry.get()
    pin = pin_entry.get()
    if username and password and pin:
        messagebox.showinfo("Sign Up", f"Welcome, {username}! You have successfully signed up.")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        pin_entry.delete(0, tk.END)
        root.withdraw()
        show_item_manager()
    else:
        messagebox.showwarning("Empty Fields", "Please enter username, password, and PIN to sign up.")

def logout():
    global item_manager_window
    item_manager_window.destroy()
    root.deiconify()

def show_item_manager():
    global item_manager_window
    item_manager_window = tk.Toplevel()
    item_manager_window.title("Item Manager")
    item_manager_window.configure(background='lightgreen')  # Set background color
    
    global entry  
    entry = ttk.Entry(item_manager_window, width=60, style='Custom.TEntry', font=("Arial", 12))
    entry.pack(pady=5)
    
    add_item_button = ttk.Button(item_manager_window, text="Add Item", command=add_item, style='Custom.TButton')
    add_item_button.pack(pady=8)
    
    global listbox  
    listbox = tk.Listbox(item_manager_window, selectmode=tk.MULTIPLE, width=70, bg='deeppink', fg='black', font=("Arial", 12))
    listbox.pack(expand=True, fill="both", padx=12)

    remove_item_button = ttk.Button(item_manager_window, text="Remove Item", command=remove_item, style='Custom.TButton')
    remove_item_button.pack(pady=8)
    
    logout_button = ttk.Button(item_manager_window, text="Log Out", command=logout, style='Custom.TButton')
    logout_button.pack(pady=8, side=tk.RIGHT)

root = tk.Tk()
root.title("List Manager")
root.configure(background='lightblue')

pin_label = ttk.Label(root, text="PIN:", font=("Arial", 12))
pin_label.pack(pady=5)
pin_entry = ttk.Entry(root, width=10, show="*", font=("Arial", 12))
pin_entry.pack()

username_label = ttk.Label(root, text="Username:", font=("Arial", 12))
username_label.pack(pady=5)
username_entry = ttk.Entry(root, width=30, font=("Arial", 12))
username_entry.pack()

password_label = ttk.Label(root, text="Password:", font=("Arial", 12))
password_label.pack(pady=5)
password_entry = ttk.Entry(root, width=30, show="*", font=("Arial", 12))
password_entry.pack()

sign_in_button = ttk.Button(root, text="Sign In", command=login, style='Custom.TButton')
sign_in_button.pack(pady=8)

sign_up_button = ttk.Button(root, text="Sign Up", command=sign_up, style='Custom.TButton')
sign_up_button.pack(pady=8)

style = ttk.Style()
style.configure('Custom.TEntry', foreground='purple', background='yellow', font=("Arial", 12))
style.configure('Custom.TButton', foreground='black', background='violet', font=("Arial", 12))

root.mainloop()
