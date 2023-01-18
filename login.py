import mysql.connector
import tkinter as tk
from logging import root



def check_credentials(username, password):
    # Connect to the MariaDB
    # normalerweise würde ich es auslagern
    connection = mysql.connector.connect(
        host='hostname',
        user='root',
        password='nine',
        database='database_name',
        charset='utf8mb4',
    )

    try:
        with connection.cursor() as cursor:
            # Check if the user exists in the database
            sql = "SELECT * FROM `users` WHERE `mitarbeiter_id`=%s AND `password`=%s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            if result:
                # If a match is found, display a message and open the main window
                tk.messagebox.showinfo("Login Successful", "Welcome, " + username)
                root.destroy()
            else:
                # If no match is found, display an error message
                tk.messagebox.showerror("Error", "Invalid username or password.")

    finally:
        connection.close()