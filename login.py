import MySQLdb
import bcrypt
import mysql.connector
import tkinter as tk
from tkinter import messagebox
from choosescreen import homescreen
def check_credentials(username, password_rec, root):
    password_to_check = password_rec.encode()
    # Connect to the MariaDB
    connsting = MySQLdb.connect(
        host='localhost',
        user='root',
        password='nine',
        db='zeiterfassung',
        charset='utf8mb4',
    )
    cursor = connsting.cursor()
    try:
        # Check if the user exists in the database
        sql = "SELECT Passwort FROM Mitarbeiter WHERE Username = %s"
        cursor.execute(sql, (username,))
        dbpass = cursor.fetchone()
        result = bcrypt.checkpw(password_to_check, dbpass[0].encode())
        if result:
            # If a match is found, display a message and open the main window
            tk.messagebox.showinfo("Login Successful", "Welcome, " + username)
            root.destroy()
            homescreen(username)
        else:
            # If no match is found, display an error message
            tk.messagebox.showerror("Error", "Invalid username or password.")
    finally:
        cursor.close()
        connsting.close()