# !/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np


def function(sollution: np.array, profits: np.array, weights: np.array, time_1: np.array, time_2: np.array,
             time_3: np.array, total_time_1: int, total_time_2: int, total_time_3: int, total_weight: int):
    """
      Funkcja obliczająca wartość funkcji celu. 
      Naszą funkcją celu jest sumaryczny iloczyn wielkości produkcji i zysku ze sprzedaży dla poszczególnego produktu.
`    """

    sollution_T = sollution.transpose()

    # Sprawdzenie spełnienia warunków rozwiązania
    for el in sollution_T:
        if el < 0:
            return 0

    if time_1.dot(sollution_T) > total_time_1:
        return 0

    if time_2.dot(sollution_T) > total_time_2:
        return 0

    if time_3.dot(sollution_T) > total_time_3:
        return 0

    if weights.dot(sollution_T) > total_weight:
        return 0

    fun = int(profits.dot(sollution_T)[0][0])
    return fun


def production_volume(number_products: int, product_weights: np.array, time_1: np.array, time_2: np.array,
                      time_3: np.array,
                      profits: np.array, total_time_1: int, total_time_2: int, total_time_3: int, total_weight: int):
    """
      Funkcja uwzględnia ograniczenia dla zadanego rozwiązania i sprawdza jego dopuszczalność
      
      Zwracamy rozwiązanie, którym jest wektor zawierający wielkość produkcji dla poszczególnego produktu 
`    """

    while True:
        products = np.random.randint(1, 100, size=(1, number_products))
        products_T = products.transpose()
        if time_1.dot(products_T) <= total_time_1 and time_2.dot(products_T) <= total_time_2:
            if time_3.dot(products_T) <= total_time_3 and product_weights.dot(products_T) <= total_weight:
                return products
