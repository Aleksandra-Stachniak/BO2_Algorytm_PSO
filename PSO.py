# !/usr/bin/python
# -*- coding: utf-8 -*-
import utils
import random
import numpy as np
import time

def particle_swarm(Nmax, products_num, num, product_weights, time_1, time_2, time_3, profits, total_time_1,
                   total_time_2, total_time_3, total_weight, w, c1, c2, r1, r2):
    """
    :param Nmax: maksymalna liczba iteracji
    :param products_num: liczba produktów
    :param num: liczba cząstek
    :param product_weights: lista wag produktów
    :param time_1: lista odpowiadających czasów dla etapu 1
    :param time_2: lista odpowiadających czasów dla etapu 2
    :param time_3: lista odpowiadających czasów dla etapu 3
    :param profits: lista zysków
    :param total_time_1: całkowity czas etapu 1
    :param total_time_2: całkowity czas etapu 2
    :param total_time_3: całkowity czas etapu 3
    :param total_weight:  wartość całkowitej masy dostępnego surowca
    """

    # najlepsze rozwiązanie globalne
    global_solution = utils.production_volume(products_num, product_weights, time_1, time_2, time_3,
                                              profits, total_time_1, total_time_2, total_time_3, total_weight)

    start_solution = global_solution
    print(f"ROZWIĄZANIE POCZĄTKOWE: \n{start_solution}")

    p = []  # najlepsze rozwiazania cząsteczek
    x = []  # rój pozycja
    v = []  # predkosc

    costPoints = []

    for i in range(num):
        p.append(global_solution)
        x.append(global_solution)
        v.append(1)

    iter = 0
    counter = 0  # zliczanie powtórzeń rozwiązań

    while iter < Nmax:
        prev = global_solution  # zapamietanie poprzedniego rozwiązania w celu zapobiegania utknięciu w minimum
        for i in range(num):
            # r1 = random.random()
            # r2 = random.random()
            #
            # w = 0.8  # – współczynnik inercji ruchu cząstki,
            # c1 = 1  # – stała dodatnia, tzw.wskaźnik samooceny,
            # c2 = 1  # – stała dodatnia, wskaźnik społecznościowy (zaufanie położeniu sąsiadów)

            # aktualizacja prędkosci cząsteczek
            v[i] = np.around(w * v[i - 1] + c1 * r1 * (p[i - 1] - x[i - 1]) + c2 * r2 * (global_solution - x[i - 1]))
            # aktualizacja pozycji cząsteczek
            x[i] = x[i - 1] + v[i]

            obj_f_x = utils.function(x[i], profits, product_weights, time_1, time_2, time_3, total_time_1,
                                     total_time_2, total_time_3, total_weight)
            obj_f_p = utils.function(p[i], profits, product_weights, time_1, time_2, time_3, total_time_1,
                                     total_time_2, total_time_3, total_weight)
            obj_f_g = utils.function(global_solution, profits, product_weights, time_1, time_2, time_3,
                                     total_time_1, total_time_2, total_time_3, total_weight)

            if obj_f_x > obj_f_p:
                p[i] = x[i]  # aktualizacja najlepszego rozwiązania cząsteczki
                if obj_f_p > obj_f_g:
                    global_solution = p[i]  # aktualizacja najlepszego rozwiązania roju

        obj_f_prev = utils.function(prev, profits, product_weights, time_1, time_2, time_3, total_time_1,
                                    total_time_2, total_time_3, total_weight)
        obj_f_g = utils.function(global_solution, profits, product_weights, time_1, time_2, time_3,
                                 total_time_1, total_time_2, total_time_3, total_weight)

        if obj_f_prev == obj_f_g:
            counter += 1
        else:
            counter = 0

        if counter >= 15:  # po 10 iteracjach o tym samym wyniku ponownie losuję rozwiązanie
            # aby nie utknąć w lokalnym minimum
            new_sol = utils.production_volume(products_num, product_weights, time_1, time_2, time_3,
                                              profits, total_time_1, total_time_2, total_time_3, total_weight)
            new_obj_f = utils.function(new_sol, profits, product_weights, time_1, time_2, time_3,
                                       total_time_1, total_time_2, total_time_3, total_weight)
            timeout = time.time() + 2
            while new_obj_f <= obj_f_g:

                if time.time() >= timeout:
                    new_sol = global_solution
                    break

                new_sol = utils.production_volume(products_num, product_weights, time_1, time_2, time_3,
                                                  profits, total_time_1, total_time_2, total_time_3, total_weight)
                new_obj_f = utils.function(new_sol, profits, product_weights, time_1, time_2, time_3,
                                           total_time_1, total_time_2, total_time_3, total_weight)

            global_solution = new_sol
            counter = 0

        obj_f_g = utils.function(global_solution, profits, product_weights, time_1, time_2, time_3,
                                 total_time_1, total_time_2, total_time_3, total_weight)
        costPoints.append(obj_f_g)

        iter += 1

    print(f"ROZWIĄZANIE KOŃCOWE: \n{global_solution}")
    print(f'FUNKCJA CELU = {obj_f_g}')
    print(f"FUNKCJE CELU W KOLEJNYCH ITERACJACH: \n{costPoints}")
    return start_solution, global_solution, obj_f_g, costPoints, Nmax
