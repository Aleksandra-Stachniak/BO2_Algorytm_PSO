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
okno1.geometry('480x680')

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

def oblicz(p_n,p_N_max,p_omega,p_c1,p_c2,p_r1,p_r2,e_s,e_g,e_fc,e_i,e_e):
    def f():
        n = p_n.get()
        N_max = p_N_max.get()
        w = p_omega.get()
        c1 = p_c1.get()
        c2 = p_c2.get()
        r1 = p_r1.get()
        r2 = p_r2.get()

        n_ = int(n)
        N_max_ = int(N_max)
        w_ = float(w)
        c1_ = float(c1)
        c2_ = float(c2)
        r1_ = float(r1)
        r2_ = float(r2)

        # ========== zmiany =================
        # pobieranie parametrów:

        # products = utils.production_volume()
        # *parametry* = parameters(n)
        # fun = utils.function( *parametry* )
        #
        # global_solution, iter = PSO.particle_swarm( *parametry*, w_, c1_, c2_, r1_, r2_)
        # można dodać do argumentów parametry omega, c1, c2, r1, r2,
        # a do wartosci zwracanych rozw. początkowe i ilość iteracji
        #

        # ====================================
        # ograniczenia
        if type(n_) != int or type(N_max_) != int or type(w_) != float or type(c1_) != float or type(c2_) != float or type(
                r1_) != float or type(c2_) != float:
            e_e['text'] = 'błędne dane'

        if n_ < 1 or N_max_ < 1:
            e_e['text'] = 'błędne dane'
        if w_ < 0 or w_ > 1:
            e_e['text'] = 'błędne dane'
        if c1_ < 0 or c1_ > 1:
            e_e['text'] = 'błędne dane'
        if c2_ < 0 or c2_ > 1:
            e_e['text'] = 'błędne dane'
        if r1_ < 0 or r1_ > 1:
            e_e['text'] = 'błędne dane'
        if r2_ < 0 or r2_ > 1:
            e_e['text'] = 'błędne dane'
        #if iter > N_max_:
        #   e_e['text'] = 'przekroczono ilość iteracji'
        #else:
        # e_s['text'] = str(start_solution)
        # e_g['text'] = str(global_solution)
        # e_fc['text'] = str(iter)
        # e_i['text'] = str(fun)

        else:
            a = n_ + N_max_
            b = w_ + n_
            c = c1_ + c2_
            d = r1_ + r2_

            e_s['text'] = str(a)
            e_g['text'] = str(b)
            e_fc['text'] = str(c)
            e_i['text'] = str(d)

    return f
#funkcja czyszcząca parametry
def button_func(e1, e2, e3, e4, e5, e6, e7, l1, l2, l3, l4, l5):
    def func():
        e1.delete(0, tkinter.END)
        e2.delete(0, tkinter.END)
        e3.delete(0, tkinter.END)
        e4.delete(0, tkinter.END)
        e5.delete(0, tkinter.END)
        e6.delete(0, tkinter.END)
        e7.delete(0, tkinter.END)
        l1['text'] = ''
        l2['text'] = ''
        l3['text'] = ''
        l4['text'] = ''
        l5['text'] = ''
    return func

#Pola do wyświetlenia wyników
l_start_solution = tkinter.Label(okno1, text='Rozwiązanie początkowe:')
e_start_solution = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)

l_global_solution = tkinter.Label(okno1, text='Rozwiązanie optymalne:')
e_global_solution = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)

l_fun_celu = tkinter.Label(okno1, text='Wartość funkcji celu:')
e_fun_celu = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)

l_iter = tkinter.Label(okno1, text='Ilosć iteracji:')
e_iter = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)

l_error_info = tkinter.Label(okno1, text='Informacja o błędzie')
e_error = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)

b_clear = tkinter.Button(okno1, text='clear', command=button_func(p_n, p_N_max, p_omega, p_c1, p_c2, p_r1, p_r2, e_start_solution, e_global_solution, e_fun_celu, e_iter, e_error))

b_gen = tkinter.Button(okno1, text='wynik', command=oblicz(p_n,p_N_max,p_omega,p_c1,p_c2,p_r1,p_r2,e_start_solution,e_global_solution, e_fun_celu, e_iter, e_error))

b_clear.pack()
ls1b = tkinter.Label(okno1, text='')
ls1b.pack()
b_gen.pack()
ls2 = tkinter.Label(okno1, text='')
ls2.pack()
l_start_solution.pack()
e_start_solution.pack()
l_global_solution.pack()
e_global_solution.pack()
l_fun_celu.pack()
e_fun_celu.pack()
l_iter.pack()
e_iter.pack()
ls4 = tkinter.Label(okno1, text='')
ls4.pack()
l_error_info.pack()
e_error.pack()

#wykres = tkinter.Tk()
#wykres.title('Wykres funkci celu')
#wykres.geometry('480x480')

#do zdefiniowania wyświetlanie wykresu (matplotlib)

okno1.mainloop()