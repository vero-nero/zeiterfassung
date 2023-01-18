import tkinter as tk
from Projekterstellungscreen import projectscreen
from zeiterfassungscreen import zeiterfassung
def homescreen(loggeduser):
    root = tk.Tk()
    root.geometry("500x350")
    root.title("Wilkommen "+loggeduser)

    #Create a frame to hold the elements
    frame = tk.Frame(root)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    login_button = tk.Button(frame, text="Zeiterfassung", command=zeiterfassung)
    register_button = tk.Button(frame, text="Projekterstellung", command=projectscreen)
    login_button.pack()
    register_button.pack()
    root.mainloop()