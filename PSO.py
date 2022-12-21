# !/usr/bin/python
# -*- coding: utf-8 -*-
import utils
import random
import numpy as np


def particle_swarm(Nmax, num, product_weights, time_1, time_2, time_3, profits, total_time_1, total_time_2, total_time_3, total_weight):

    """
    :param Nmax: maksymalna liczba iteracji
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
    global_solution = utils.production_volume(num, product_weights, time_1, time_2, time_3,
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

    while iter < Nmax:
        for i in range(num):
            r1 = random.random()
            r2 = random.random()

            w = 1  # – współczynnik inercji ruchu cząstki,
            c1 = 1  # – stała dodatnia, tzw.wskaźnik samooceny,
            c2 = 1  # – stała dodatnia, wskaźnik społecznościowy (zaufanie położeniu sąsiadów)

            # aktualizacja prędkosci cząsteczek
            v[i] = np.around(w * v[i - 1] + c1 * r1 * (p[i - 1] - x[i - 1]) + c2 * r2 * (global_solution - x[i - 1]))
            # aktualizacja pozycji cząsteczek
            x[i] = x[i - 1] + v[i]

            if utils.function(x[i], profits, product_weights, time_1, time_2, time_3, total_time_1,
                              total_time_2, total_time_3, total_weight) > utils.function(p[i], profits, product_weights,
                                                                                         time_1, time_2, time_3,
                                                                                         total_time_1, total_time_2, total_time_3,
                                                                                         total_weight):
                p[i] = x[i]  # aktualizacja najlepszego rozwiązania cząsteczki

                if utils.function(p[i], profits, product_weights, time_1, time_2, time_3, total_time_1,
                                  total_time_2, total_time_3, total_weight) > utils.function(global_solution, profits, product_weights,
                                                                                             time_1, time_2, time_3,
                                                                                             total_time_1, total_time_2, total_time_3,
                                                                                             total_weight):
                    global_solution = p[i]  # aktualizacja najlepszego rozwiązania roju

        costPoints.append(utils.function(global_solution, profits, product_weights, time_1, time_2, time_3, total_time_1, total_time_2, total_time_3, total_weight))
        iter += 1

    print(f"ROZWIĄZANIE KOŃCOWE: \n{global_solution}")
    print(f'FUNKCJA CELU = {utils.function(global_solution, profits, product_weights, time_1, time_2, time_3, total_time_1, total_time_2, total_time_3, total_weight)}')
    return global_solution
