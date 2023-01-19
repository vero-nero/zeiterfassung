import tkinter as tk
from projdbhandler import getprojects
import tkinter as tk


def toggle_time(time_label, toggle_button):
    pass

def submit_form():
    pass
def zeiterfassung():
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
    # Create a submit button
    submit_button = tk.Button(zroot, text="Submit", command=lambda: submit_form)
    submit_button.pack()

    zroot.mainloop()

