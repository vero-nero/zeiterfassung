import MySQLdb
import mysql.connector
import re
import tkinter as tk
import bcrypt

def register_user():
    register_window = tk.Tk()
    register_window.title("Register")

    vorname_label = tk.Label(register_window, text="Vorname:")
    vorname_label.grid(row=0, column=0)

    vorname_entry = tk.Entry(register_window)
    vorname_entry.grid(row=0, column=1)

    nachname_label = tk.Label(register_window, text="Nachname:")
    nachname_label.grid(row=1, column=0)

    nachname_entry = tk.Entry(register_window)
    nachname_entry.grid(row=1, column=1)

    password_label = tk.Label(register_window, text="Passwort:")
    password_label.grid(row=3, column=0)

    password_entry = tk.Entry(register_window, show="*")
    password_entry.grid(row=3, column=1)

    username_label = tk.Label(register_window, text="Username:")
    username_label.grid(row=4, column=0)

    uname_entry = tk.Entry(register_window)
    uname_entry.grid(row=4, column=1)

    register_button = tk.Button(register_window, text="Register", command=lambda: create_user(vorname_entry.get(), nachname_entry.get(), password_entry.get(),uname_entry.get()))
    register_button.grid(row=5, column=1)

def create_user(vorname, nachname, password, uname):
    # Check the password for certain conditions
    if ( len(vorname) != 0) & (len(nachname) != 0):
        if re.search("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{10,}$", password):
            # Connect to the MariaDB database
            # Create a cursor object
            connsting = MySQLdb.connect(
                host='localhost',
                user='root',
                password='nine',
                db='zeiterfassung',
                charset='utf8mb4',
            )
            cursor = connsting.cursor()
            #password wird in bytes verwandelt um sie weiterzuverarbeiten
            bytepassword = password.encode()
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(bytepassword, salt)
            # Insert the user's data into the users table
            sql = "INSERT INTO Mitarbeiter ( Username, Vorname, Nachname, Passwort) VALUES (%s, %s, %s, %s)"
            val = (uname, vorname, nachname, hashed_password)
            cursor.execute(sql, val)
            # Commit the changes to the database
            connsting.commit()
            # Close the cursor and database connection
            cursor.close()
            connsting.close()
            tk.messagebox.showinfo("Success","User created successfully!")
        else:
            # Password is invalid
            tk.messagebox.showerror("Error","Password must be at least 10 characters long and contain numbers and special characters.")