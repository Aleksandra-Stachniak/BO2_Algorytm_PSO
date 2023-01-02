# -*- coding: utf-8 -*-
"""Python_GUI

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EOjoFroQ5Ckrnq2dpKuZDv5zPVdDX07Z
"""

import tkinter

okno1 = tkinter.Tk() #tworzy okno
okno1.geometry('480x480') #ustawiamy wymiary okna

l1 = tkinter.Label(okno1, text='Liczba produktów') #tworzenie napisu powiązanego z danym oknem
l1.pack() #dodajemy utworzony obiekt do okna
#p1 = tkinter.Entry(okno1) #pole do wpisania liczby produktów (można dodać par, który wyśrodkuje tekst: justify='center')
#p1.pack() #ręcznie ustawiamy położenie obiektu: grid(row=0, column=0)

def funkcja_przycisku():
    print('wciśnięto przycisk') #(pojawia się komunikat - wypisany w konsoli)

b1 = tkinter.Button(okno1, text='xxx1', command=funkcja_przycisku) #tworzenie przycisku z jakąś funkcjonalnością
b1.pack(side=tkinter.RIGHT) #dodaje przycisk do okna i ustawia jego położenie
#zamiennie można użyć b1.place(x=0, y=0) - lewy górny róg (pixele)
b2 = tkinter.Button(okno1, text='xxx2', width=20, bg="red", fg="green", command=funkcja_przycisku)
b2.pack(side=tkinter.BOTTOM)
#ustawiamy także długość przycisku, kolor tła i napisu
b3 = tkinter.Button(okno1, text='xxx3', command=funkcja_przycisku)
b3.pack(side=tkinter.LEFT)
b3.bind('<Button-1>') #przycisk b3 zareaguje tylko po nacśnięciu LPM (można dodać command= jak w def. guzika)
#analogicznie bind('<Button-3>') reguje tylko na PPM
#do jednego obiektu moze być przypisane więcej niż jedno zdarzenie (kliknięcie LPM robi co innego i PPM co innego)

#budowa i obsługa menu (paska zadań)

menu1 = tkinter.Menu() #tworzenie jakiegoś menu
okno1.config(menu=menu1) #powiązanie go z oknem
#file_menu = tkinter.Menu(menu1) #utworzenie paska powiązanego z danym menu
#menu1.add_cascade(label='File', menu=file_menu) #ustawiamy sposób rozwijania menu do dołu
#uzupełniamy zakładkę
#file_menu.add_command(label='New File')
#file_menu.add_command(label='Open')
#file_menu.add_command(label='Save')
#file_menu.add_separator()
def oblicz(e1, e2, l):
    def f():
        a = e1.get()
        b = e2.get()
        a_int = int(a)
        b_int = int(b)
        c = str(a_int + b_int)
        l['text'] = c
    return f

entry1 = tkinter.Entry(okno1)
entry2 = tkinter.Entry(okno1)
entry1.pack()
entry2.pack()
s1 = tkinter.Label(okno1, text=" ")
s1.pack()
wyswietl = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)
button_rowna_sie = tkinter.Button(okno1, text="=", command=oblicz(entry1, entry2, wyswietl))
button_rowna_sie.pack()
s2 = tkinter.Label(okno1, text=" ")
s2.pack()
wyswietl.pack()
#tworzenie podmenu zakładki
#pod_menu = tkinter.Menu(file_menu)
#file_menu.add_cascade(label='Recent Files', menu=pod_menu)
#pod_menu.add_command(label='X')
#pod_menu.add_command(label='Y')
#pod_menu.add_command(label='Z')

#inna zakładka
#edit_menu = tkinter.Menu(menu1)
#menu1.add_cascade(label='Edit', menu=edit_menu)
#edit_menu.add_command(label='Undo')
#edit_menu.add_command(label='Redo')
#edit_menu.add_separator()
#edit_menu.add_command(label='Cut')
#edit_menu.add_command(label='Copy')
#edit_menu.add_command(label='Paste')

#suwak doadajemy w nastepujący sposób:
#można zdefiniować funkcję do zmiany zakresu slidera w trakcie wykonywania programu
#def = jakas_funkcja(a):
#    global liczba
#    liczba = random.randint(1, int(a))
#s = tkinter.Scale(okno1, command = jakas_funkcja, orient = 'horizontal')

okno1.mainloop() #okno powinno otwierać się przez dłuższy czas 
#(bez tego aplikacja od razu się zamknie)