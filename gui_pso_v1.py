#!/usr/bin/python
# -*- coding: utf-8 -*-

import tkinter
import utils
import PSO
from PSO import particle_swarm
import data_structures
import random
import numpy as np

from matplotlib.backends.backend_tkagg import (
   FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

okno1 = tkinter.Tk()
okno1.title('Optymalizacja zysków z produkcji')
okno1.geometry('480x800')

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
l_num = tkinter.Label(okno1, text='Liczba cząstek')
p_num = tkinter.Entry(okno1)
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
l_num.pack()
p_num.pack()
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

def oblicz(p_n,p_N_max,p_omega,p_c1,p_c2,p_r1,p_r2,e_s,e_g,e_fc,e_e):
    def f():
        number_products = int(p_n.get())
        Nmax = int(p_N_max.get())
        w = float(p_omega.get())
        c1 = float(p_c1.get())
        c2 = float(p_c2.get())
        r1 = float(p_r1.get())
        r2 = float(p_r2.get())
        num = int(p_num.get())

        # ========== zmiany =================
        # pobieranie parametrów:

        product_weights, time_1, time_2, time_3, profits, total_time_1, total_time_2, total_time_3, total_weight = data_structures.parameters(number_products)
        start_solution, global_solution, fun, costPoints, iter = PSO.particle_swarm(Nmax, number_products, num, product_weights, time_1, time_2, time_3, profits, total_time_1,
                           total_time_2, total_time_3, total_weight, w, c1, c2, r1, r2)

        # ====================================
        # ograniczenia
        if type(number_products) != int or type(Nmax) != int or type(w) != float or type(c1) != float or type(c2) != float or type(
                r1) != float or type(c2) != float:
            e_e['text'] = 'błędne dane'
            e_s['text'] = 'err404 XD'
            e_g['text'] = 'err404 XD'
            e_fc['text'] = 'err404 XD'

        if number_products < 1 or r2 < 0 or r2 > 1 or Nmax < 1 or w < 0 or w > 1 or c1 < 0 or c2 < 0 or r1 < 0 or r1 > 1:
            e_e['text'] = 'błędne dane'
            e_s['text'] = 'err404 XD'
            e_g['text'] = 'err404 XD'
            e_fc['text'] = 'err404 XD'
        else:
            e_s['text'] = str(start_solution)
            e_g['text'] = str(global_solution)
            e_fc['text'] = str(fun)
            chart(Nmax, costPoints, fun)
    return f

#funkcja czyszcząca parametry
def button_func(e1, e2, e3, e4, e5, e6, e7, l1, l2, l3, l4):
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
    return func

#Pola do wyświetlenia wyników
l_start_solution = tkinter.Label(okno1, text='Rozwiązanie początkowe:')
e_start_solution = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)

l_global_solution = tkinter.Label(okno1, text='Rozwiązanie optymalne:')
e_global_solution = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)

l_fun_celu = tkinter.Label(okno1, text='Wartość funkcji celu:')
e_fun_celu = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)

l_error_info = tkinter.Label(okno1, text='Informacja o błędzie')
e_error = tkinter.Label(okno1, bg="#C0CBCB", width=55, anchor="w", borderwidth=2)

b_clear = tkinter.Button(okno1, text='clear', command=button_func(p_n, p_N_max, p_omega, p_c1, p_c2, p_r1, p_r2, e_start_solution, e_global_solution, e_fun_celu, e_error))

b_gen = tkinter.Button(okno1, text='wynik', command=oblicz(p_n,p_N_max,p_omega,p_c1,p_c2,p_r1,p_r2,e_start_solution,e_global_solution, e_fun_celu, e_error))

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
ls4 = tkinter.Label(okno1, text='')
ls4.pack()
l_error_info.pack()
e_error.pack()

#=====================WYKRES=====================

def chart(Nmax, costPoints, fun):
    okno_wykres = tkinter.Tk()
    okno_wykres.wm_title("Wykres funkcji celu")

    fig = Figure(figsize=(5, 4), dpi=100)

    iter_tab = list(range(1, Nmax+1))
    f_celu_tab = costPoints

    fig.add_subplot(111).plot(iter_tab, f_celu_tab)

    canvas = FigureCanvasTkAgg(fig, master=okno_wykres)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    toolbar = NavigationToolbar2Tk(canvas, okno_wykres)
    toolbar.update()
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    def on_key_press(event):
       print("you pressed {}".format(event.key))
       key_press_handler(event, canvas, toolbar)

    canvas.mpl_connect("key_press_event", on_key_press)

    def _quit():
       root.quit()     # stops mainloop
       root.destroy()  # this is necessary on Windows to prevent

    button_quit = tkinter.Button(master=okno_wykres, text="Quit", command=_quit)
    button_quit.pack(side=tkinter.BOTTOM)

    okno_wykres.mainloop()
#================================================

okno1.mainloop()