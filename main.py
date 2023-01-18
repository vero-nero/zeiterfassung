import tkinter as tk
import tkinter.messagebox as messagebox
import MySQLdb.cursors
import re
import mysql.connector


def create_user():
    # Get the user's input
    vorname = vorname_entry.get()
    nachname = nachname_entry.get()
    mitarbeiter_id = mitarbeiter_id_entry.get()
    password = password_entry.get()

    # Connect to the MariaDB database
    mydb = mysql.connector.connect(
        host="hostname",
        user="username",
        password="password",
        database="database_name"
    )

    # Create a cursor object
    cursor = mydb.cursor()

    # Insert the user's data into the users table
    sql = "INSERT INTO users (vorname, nachname, mitarbeiter_id, password) VALUES (%s, %s, %s, %s)"
    val = (vorname, nachname, mitarbeiter_id, password)
    cursor.execute(sql, val)

    # Commit the changes to the database
    mydb.commit()

    # Close the cursor and database connection
    cursor.close()
    mydb.close()


def chekc_user_pass(): #userdata are checked and sent to the db in this method
    password = password_entry.get()
    if re.search("^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{10,}$", password):
        # password is valid
        # insert data into the database
        pass
    else:
        # password is invalid
        tk.messagebox.showerror("Error", "Password must be at least 10 characters long and contain numbers and special characters.")

def register_user():
    register_window = tk.Toplevel(root)
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

    register_button = tk.Button(register_window, text="Register", command=create_user)
    register_button.grid(row=4, column=1)


def check_credentials():
    # get the user input
    username = username_entry.get()
    password = password_entry.get()

    # connect to the MariaDB
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        password='nine',
        db='zeiterfassung',
        charset='utf8mb4',
    )

    try:
        with connection.cursor() as cursor:
            # check if the user exists in the database
            sql = "SELECT * FROM `Mitarbeiter` WHERE `Mitarbeiter_ID`=%s AND `Passwort`=%s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()

            if result:
                # if a match is found, display a message and open the main window
                tk.messagebox.showinfo("Login Successful", "Welcome, " + username)
                root.destroy()
                main_window()
            else:
                # if no match is found, display an error message
                tk.messagebox.showerror("Login Failed", "Invalid username or password.")
    finally:
        connection.close()

def main_window():
    # code for your main window goes here
    pass

root = tk.Tk()
root.geometry("500x350")
root.title("Conzens Zeiterfassung")

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

login_button = tk.Button(frame, text="Login", command=check_credentials)
register_button = tk.Button(frame, text="Register", command=register_user)
login_button.pack()
register_button.pack()
root.mainloop()
