from tkinter import *
import sqlite3
def naitaTabel(tabel_name):
    tableButtonsRemove()

    #tühista eelmised asjad
    output_text.insert(END,f"Tabel {tabel_name}:\n")

    query = readQery(connection, f"SELECT * FROM {tabel_name}")
    for row in query:
        output_text.insert(END,f"{row}\n")
    output_text.pack()




def insert_andmeid_Kategooriad():
    add_kategooria_id=int(input())
    add_kategooria_nimi=input()
    cursor.execute('''
    INSERT INTO Kategooriad (kategooria_id, kategooria_nimi) VALUES (?, ?), ( {add_kategooria_id}, '{add_kategooria_nimi}')''')







def insert_andmeid_Brandid():
    add_kategooria_id=int(input())
    add_kategooria_nimi=input()
    cursor.execute('''
    INSERT INTO Kategooriad (kategooria_id, kategooria_nimi) VALUES (?, ?), ( {add_kategooria_id}, '{add_kategooria_nimi}')''')









def insert_andmeid_Tooted():
    add_toode_id=int(input())
    add_toode_nimi=input()
    add_toode_hind=input()
    add_toode_kategooria=input()
    add_toode´_brand
    cursor.execute('''
    INSERT INTO Tooted (toode_id, toode_nimi, hind, kategooria_id, brandi_id) VALUES (?, ?, ?, ?, ?), ( {add_kategooria_id}, '{add_kategooria_nimi}')''')








def update_andmeid_Kategooriad():
    pass







def update_andmeid_Brandid():
    pass








def update_andmeid_Tooted():
    pass








def delite_andmeid_Kategooriad():
    pass







def delite_andmeid_Brandid():
    pass








def delite_andmeid_Tooted():
    pass