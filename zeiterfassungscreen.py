import tkinter as tk

import MySQLdb

from projdbhandler import getprojects
import tkinter as tk
from datetime import datetime


def toggle_time(time_label, toggle_button):
    # Get the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    # Update the label with the current time
    time_label.config(text=current_time)
    # Change the button text
    if toggle_button["text"] == "Start":
        toggle_button.config(text="Stop")
    else:
        toggle_button.config(text="Start")

def submit_form():
    connsting = MySQLdb.connect(
        host='localhost',
        user='root',
        password='nine',
        db='zeiterfassung',
        charset='utf8mb4')
    cursor = connsting.cursor()
    todaydate = datetime.date()
    time = datetime.now()
    # Insert the user's data into the users table
    sql = "INSERT INTO Arbeitszeiten( Mitarbeiter_ID, Projekt_ID, Datum, Zeitstempel_Begin, Zeitstempel_Ende, Beschreibung_der_Arbeiten) VALUES (%s, %s, %s, %s, %s, %s)"
    val = ("username", "projnumber", todaydate, time, time, "description")
    cursor.execute(sql, (val,))
    # Commit the changes to the database
    connsting.commit()
    # Close the cursor and database connection
    cursor.close()
    connsting.close()
def zeiterfassung(username):
    zroot = tk.Tk()
    zroot.title("Time Tracking Form")

    # Create a variable to store the selected project
    project_var = tk.StringVar(zroot)
    # Set the default project
    projects = getprojects()
    # Create a dropdown menu for project selection
    project_dropdown = tk.OptionMenu(zroot, project_var, *projects)
    project_dropdown.pack()
    # Create a label to display the current time
    time_label = tk.Label(zroot, text="00:00:00")
    time_label.pack()

    # Create a button to toggle the time
    toggle_button = tk.Button(zroot, text="Start", command=lambda: toggle_time(time_label, toggle_button))
    toggle_button.pack()

    descr_label = tk.Label(zroot, text="Beschreibung der Aufgaben:")
    descr_label.grid(row=1, column=0)
    descr_entry = tk.Entry(zroot)
    descr_entry.grid(row=1, column=1)
    # Create a submit button
    submit_button = tk.Button(zroot, text="Submit", command=lambda: submit_form)#bin nicht fertig gworden deswegen mach ich so dass die arbeitsdauer immer 1 stunde ist
    #normalerweiße würde ich ein button mit start arbeit und stop arbeit das bei jedem click zur datenbank schickt
    #dafür müsste aber auch das DB design geändert werden
    submit_button.pack()

    zroot.mainloop()

