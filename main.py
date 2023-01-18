import tkinter as tk
from register import register_user
from login import check_credentials

root = tk.Tk()
root.geometry("500x350")
root.title("Conzens Zeiterfassung Password123*")

# Create a frame to hold the elements
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

username_label = tk.Label(frame, text="Username:")
username_label.pack()

username_entry = tk.Entry(frame)
username_entry.pack()

password_label = tk.Label(frame, text="Password:")
password_label.pack()

password_entry = tk.Entry(frame, show="*")
password_entry.pack()

login_button = tk.Button(frame, text="Login", command=lambda: check_credentials(username_entry.get(),
                                                                                password_entry.get(),
                                                                                root))
register_button = tk.Button(frame, text="Register", command=register_user)
login_button.pack()
register_button.pack()
root.mainloop()