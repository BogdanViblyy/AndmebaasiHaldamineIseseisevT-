from tkinter import *
import sqlite3
from MyModul import *
import tkinter as tk
# Loome andmebaasiühenduse (faili my_database.db luuakse)
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor() 
# Kategooriate tabeli loomine
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Kategooriad (
        kategooria_id INTEGER PRIMARY KEY AUTOINCREMENT,
        kategooria_nimi TEXT NOT NULL
    )
''')
# Brändide tabeli loomine
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Brandid (
        brandi_id INTEGER PRIMARY KEY AUTOINCREMENT,
        brandi_nimi TEXT NOT NULL
    )
''')
## Toodete tabeli loomine
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tooted (
        toode_id INTEGER PRIMARY KEY AUTOINCREMENT,
        toode_nimi TEXT NOT NULL,
        hind REAL NOT NULL,
        kategooria_id INTEGER,
        brandi_id INTEGER,
        FOREIGN KEY (kategooria_id) REFERENCES Kategooriad(kategooria_id),
        FOREIGN KEY (brandi_id) REFERENCES Brandid(brandi_id)
    )
''')
cursor.execute('''
    INSERT INTO Kategooriad (kategooria_id, kategooria_nimi) VALUES (?, ?), ( 1, 'riided')''')





#TK kasutajaliides
root = Tk()
root.title('Viblyy shop')
root.wm_attributes('-alpha',0.7)
root.geometry('300x200')



canvas = tk.Canvas(root, height=200, width=300)
canvas.pack(fill=tk.BOTH, expand=True)


canvas.create_text(150, 10, text="Viblyy Shop", font=('Helvetica', 16), anchor='n')


button1 = tk.Button(root, text="Kategooriad", font=('Helvetica', 12), command=naitaTabel(Kategooriad):)
button1.pack()


button2 = tk.Button(root, text="Brandid", font=('Helvetica', 12), command=naitaTabel(Brandid):)
button2.pack()


button3 = tk.Button(root, text="Tooted", font=('Helvetica', 12), command=naitaTabel(Tooted):)
button3.pack()
root.mainloop()