import tkinter as tk
def zeiterfassung():
    root = tk.Tk()
    root.title("Time Tracking Form")

    # Create a variable to store the selected project
    project_var = tk.StringVar(root)
    # Set the default project
    project_var.set("Project 1")

    # Create a dropdown menu for project selection
    project_dropdown = tk.OptionMenu(root, project_var, "Project 1", "Project 2", "Project 3")
    project_dropdown.grid(row=0, column=0)

    # Create entry widgets for date, start, end, employee, and description
    date_entry = tk.Entry(root)
    date_entry.grid(row=1, column=0)
    start_entry = tk.Entry(root)
    start_entry.grid(row=2, column=0)
    end_entry = tk.Entry(root)
    end_entry.grid(row=3, column=0)
    employee_entry = tk.Entry(root)
    employee_entry.grid(row=4, column=0)
    description_entry = tk.Entry(root)
    description_entry.grid(row=5, column=0)

    # Create a submit button
    submit_button = tk.Button(root, text="Submit")#, command=submit_form)
    submit_button.grid(row=6, column=0)

    root.mainloop()