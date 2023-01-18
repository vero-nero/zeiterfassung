from projdbhandler import saveproject
import tkinter as tk

def projectscreen():
    register_window = tk.Tk()
    register_window.title("Register")

    projnummer_label = tk.Label(register_window, text="Projektnummer:")
    projnummer_label.grid(row=0, column=0)

    projnummer_entry = tk.Entry(register_window)
    projnummer_entry.grid(row=0, column=1)

    descr_label = tk.Label(register_window, text="Beschreibung:")
    descr_label.grid(row=1, column=0)

    descr_entry = tk.Entry(register_window)
    descr_entry.grid(row=1, column=1)

    customer_label = tk.Label(register_window, text="Auftraggeber:")
    customer_label.grid(row=3, column=0)

    customer_entry = tk.Entry(register_window)
    customer_entry.grid(row=3, column=1)

    register_button = tk.Button(register_window, text="Register", command=lambda:saveproject(projnummer_entry.get(),descr_entry.get(),customer_entry.get()))
    register_button.grid(row=5, column=1)