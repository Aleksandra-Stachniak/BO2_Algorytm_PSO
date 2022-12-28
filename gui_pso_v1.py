#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
#import utils
#import PSO
#from PSO import particle_swarm
#import data_structures
#import random
#import numpy as np

okno1 = tkinter.Tk()
okno1.title('Optymalizacja zysków z produkcji')
okno1.geometry('480x620')

#Pole do wpisania liczby produktów
l_n = tkinter.Label(okno1, text='Podaj liczbę produktów:')
l_n.pack(side=tkinter.TOP)
p_n = tkinter.Entry(okno1)
p_n.pack(side=tkinter.TOP)

#Pola do wpisywania parametrów
ls1 = tkinter.Label(okno1, text='')
ls1.pack()
l_params = tkinter.Label(okno1, text='Podaj parametry:')
l_params.pack()

l_N_max = tkinter.Label(okno1, text='Maksymalna liczba iteracji:')
p_N_max = tkinter.Entry(okno1)
l_omega = tkinter.Label(okno1, text='\u03C9')
p_omega = tkinter.Entry(okno1)
l_c1 = tkinter.Label(okno1, text='c1')
p_c1 = tkinter.Entry(okno1)
l_c2 = tkinter.Label(okno1, text='c2')
p_c2 = tkinter.Entry(okno1)
l_r1 = tkinter.Label(okno1, text='r1')
p_r1 = tkinter.Entry(okno1)
l_r2 = tkinter.Label(okno1, text='r2')
p_r2 = tkinter.Entry(okno1)

l_N_max.pack()
p_N_max.pack()
l_omega.pack()
p_omega.pack()
l_c1.pack()
p_c1.pack()
l_c2.pack()
p_c2.pack()
l_r1.pack()
p_r1.pack()
l_r2.pack()
p_r2.pack()
ls1a = tkinter.Label(okno1, text='')
ls1a.pack()

#funkcja czyszcząca parametry
def button_func(a, b, c, d, e, f, g):
    def func():
        a.delete(0, tkinter.END)
        b.delete(0, tkinter.END)
        c.delete(0, tkinter.END)
        d.delete(0, tkinter.END)
        e.delete(0, tkinter.END)
        f.delete(0, tkinter.END)
        g.delete(0, tkinter.END)
    return func

b = tkinter.Button(okno1, text='clear', command=button_func(p_n, p_N_max, p_omega, p_c1, p_c2, p_r1, p_r2))
b.pack()

#Pobieranie parametrów
def get_params(p1, p2, p3, p4, p5, p6, p7):
    #if int(p_n.get()) > 0 and int(p_N_max.get()) > 0 and 0 < int(p_omega.get()) < 1 and 0 < int(p_c1.get()) < 1 and 0 < int(p_c2.get()) < 1 and 0 < int(p_r1.get()) < 1 and 0 < int(p_r2.get()) < 1:
    n = p1.get()
    N_max = p2.get()
    w = p3.get()
    c1 = p4.get()
    c2 = p5.get()
    r1 = p6.get()
    r2 = p7.get()
    return n, N_max, w, c1, c2, r1, r2
    #else:
        #p_error['text'] = 'Błąd - popraw dane'

n, N_max, w, c1, c2, r1, r2 = get_params(p_n, p_N_max, p_omega, p_c1, p_c2, p_r1, p_r2)

#test
ps = n + c1
gs = r1 + r2

#ps = particle_swarm.start_solution
#gs = particle_swarm.global_solution
#fun_celu = particle_swarm.utils.function
#i = particle_swarm.iter

#Pola do wyświtlenia wyników
ls2 = tkinter.Label(okno1, text='')
ls2.pack()
l_start_solution = tkinter.Label(okno1, text='Rozwiązanie początkowe:')
e_start_solution = tkinter.Label(okno1, text=ps, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)
l_start_solution.pack()
e_start_solution.pack()
l_global_solution = tkinter.Label(okno1, text='Rozwiązanie optymalne:')
e_global_solution = tkinter.Label(okno1, text=gs, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)
l_global_solution.pack()
e_global_solution.pack()
l_fun_celu = tkinter.Label(okno1, text='Wartość funkcji celu:')
e_fun_celu = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)
l_fun_celu.pack()
e_fun_celu.pack()
l_iter = tkinter.Label(okno1, text='Ilosć iteracji:')
e_iter = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)
l_iter.pack()
e_iter.pack()

ls4 = tkinter.Label(okno1, text='')
ls4.pack()
p_error = tkinter.Entry(okno1)
p_error.pack()

#wykres = tkinter.Tk()
#wykres.title('Wykres funkci celu')
#wykres.geometry('480x480')

#do zdefiniowania wyświetlanie wykresu (matplotlib)

okno1.mainloop()

#do rzeczy zwracanych przez particle_swarm trzeba by dodać global_solution, start_solution iter i wartość funkcji celu
#powiązać te wartości z odpowiednimi oknami, dodać ograniczenia dla wpisywanych wartości
#(najlepiej stworzyć funkcje do tworzenia pól itp.)
#dodac komunikat o błędzie, gdy zostaną wpisane złe dane,
#odać możliwość powtórnego wykonania algorytmu
#dodać okno do wyświetlania wykresu wartości funkcji celu