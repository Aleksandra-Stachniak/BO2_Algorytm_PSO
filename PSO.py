# !/usr/bin/python
# -*- coding: utf-8 -*-
import utils
import random
import numpy as np


def particle_swarm(Nmax, num, weights, time, profits, total_time, total_weight):
    '''
    :param Nmax: maksymalna liczba iteracji
    :param num: liczba cząstek
    :param weights: lista wag produktów
    :param time: krotka list odpowiadających czasom dla poszczególnych etapów
    :param profits: lista zysków
    :param total_time:  lista całkowitych czasów dla poszczególnych etapów
    :param total_weight:  wartość całkowitej masy dostępnego surowca
    '''

    # najlepsze rozwiązanie globalne
    global_solution = utils.production_volume(num, weights, time[0], time[1], time[2],
                                              profits, total_time[0], total_time[1], total_time[2], total_weight)

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
            r1 = random.randint(0, 1)
            r2 = random.randint(0, 1)

            w = 1  # – współczynnik inercji ruchu cząstki,
            c1 = 1  # – stała dodatnia, tzw.wskaźnik samooceny,
            c2 = 1  # – stała dodatnia, wskaźnik społecznościowy (zaufanie położeniu sąsiadów)

            # aktualizacja prędkosci cząsteczek
            v[i] = w * v[i - 1] + c1 * r1 * (p[i - 1] - x[i - 1]) + c2 * r2 * (global_solution - x[i - 1])
            # aktualizacja pozycji cząsteczek
            x[i] = x[i - 1] + v[i]

            if utils.function(x[i], profits, weights, time[0], time[1], time[2], total_time[0], total_time[1],
                              total_time[2], total_weight) > utils.function(p[i], profits, weights, time[0], time[1],
                                                                            time[2], total_time[0], total_time[1],
                                                                            total_time[2], total_weight):
                p[i] = x[i]  # aktualizacja najlepszego rozwiązania cząsteczki

                if utils.function(p[i], profits, weights, time[0], time[1], time[2], total_time[0], total_time[1],
                                  total_time[2], total_weight) > utils.function(global_solution, profits, weights,
                                                                                time[0], time[1], time[2],
                                                                                total_time[0], total_time[1],
                                                                                total_time[2], total_weight):
                    global_solution = p[i]  # aktualizacja najlepszego rozwiązania roju

        costPoints.append(utils.function(global_solution, profits))
        iter += 1

    print(f"ROZWIĄZANIE KOŃCOWE: \n{global_solution}")
    print(f'FUNKCJA CELU = {utils.function(global_solution, profits)}')

    return global_solution
