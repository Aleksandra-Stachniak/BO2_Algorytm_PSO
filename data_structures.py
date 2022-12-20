# -*- coding: utf-8 -*-
import numpy as np
import utils
import PSO

def parameters(number_products:int):
    """
    Funkcja definiuje dane niezbędne w rozpatrywanym przez nas problemie
    number_products - liczba wytwarzanych produktów w zakładzie produkcyjnym

    Zwracamy:
    products_weights - wektor zawierający informacje o masie potrzebnej do wytworzenia jednej sztuki poszczególnego produktu
    time_1 - wektor zawierający informacje o czasie potrzebnym do wytworzenia jednej sztuki poszczególnego produktu w 1 etapie pracy
    time_2 - wektor zawierający informacje o czasie potrzebnym do wytworzenia jednej sztuki poszczególnego produktu w 2 etapie pracy
    time_3 - wektor zawierający informacje o czasie potrzebnym do wytworzenia jednej sztuki poszczególnego produktu w 3 etapie pracy
    profits - wektor zawierający informacje o zysku ze sprzedaży jednej sztuki poszczególnego produktu
    total_time_1 - całkowity czas przeznaczony do wytworzenia produktów w etapie 1
    total_time_2 - całkowity czas przeznaczony do wytworzenia produktów w etapie 2
    total_time_3 - całkowity czas przeznaczony do wytworzenia produktów w etapie 3
    total_weight - całkowita masa surowca, którą dysponujemy do wytworzenia produktów
`   """

    if number_products <= 0:
      print('Liczba produktów nie może przyjmować wartości niedodatnich')
    else:
      product_weights = np.random.randint(1, 40, size=(1,number_products))
      time_1 = np.random.randint(1, 10, size=(1,number_products))
      time_2 = np.random.randint(1, 5, size=(1,number_products))
      time_3 = np.random.randint(1, 3, size=(1,number_products))
      profits = np.random.randint(1, 100, size=(1,number_products))
      
    total_time_1 = np.random.randint(1, 10000)
    total_time_2 = np.random.randint(1, 5000)
    total_time_3 = np.random.randint(1, 5000)
    total_weight = np.random.randint(7000, 15000)
    return product_weights, time_1, time_2, time_3, profits, total_time_1, total_time_2, total_time_3, total_weight


def main():
    number_products = 5
    product_weights, time_1, time_2, time_3, profits, total_time_1, total_time_2, total_time_3, total_weight  = parameters(number_products)
    products = utils.production_volume(number_products, product_weights, time_1, time_2, time_3,
                      profits, total_time_1, total_time_2, total_time_3, total_weight)
    products_T = products.transpose()

    PSO.particle_swarm(10, 5, product_weights, time_1, time_2, time_3, profits, total_time_1, total_time_2,
                   total_time_3, total_weight)

    print(total_time_1)
    print(time_1.dot(products_T))
    print(total_time_2)
    print(time_2.dot(products_T))
    print(total_time_3)
    print(time_3.dot(products_T))
    print(total_weight)
    print(product_weights.dot(products_T))
    print(utils.function(profits, products))
    print(products) 

if __name__ == "__main__":
    main()
