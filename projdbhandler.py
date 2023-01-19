import tkinter as tk
import MySQLdb

global connsting
connsting = MySQLdb.connect(
            host='localhost',
            user='root',
            password='nine',
            db='zeiterfassung',
            charset='utf8mb4' )
def saveproject(projnum, description, customer):
    # Check the password for certain conditions
    try:
        cursor = connsting.cursor()
        # Insert the user's data into the users table
        sql = "INSERT INTO Projekte ( Projektnummer, Beschreibung, Name_des_Auftraggebers) VALUES (%s, %s, %s)"
        val = (projnum, description, customer)
        cursor.execute(sql, val)
        # Commit the changes to the database
        connsting.commit()
        # Close the cursor and database connection
        cursor.close()
        connsting.close()
        tk.messagebox.showinfo("Success", "Project created successfully!")
    except:
        # Password is invalid
        tk.messagebox.showerror("Error", "Projektcreation went wrong.")
def getprojects():
    connsting = MySQLdb.connect(
        host='localhost',
        user='root',
        password='nine',
        db='zeiterfassung',
        charset='utf8mb4')
    cursor = connsting.cursor()
    sql = "SELECT Projektnummer FROM Projekte" #Select Projektnummer From Projekte
    cursor.execute(sql)
    dbpass = cursor.fetchone()
    cursor.close()
    connsting.close()
    return dbpass