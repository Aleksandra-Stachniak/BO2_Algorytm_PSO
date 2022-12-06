# -*- coding: utf-8 -*-
import numpy as np

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

def function(sollution:np.array, profits:np.array):
    """
      Funkcja obliczająca wartość funkcji celu. 
      Naszą funkcją celu jest sumaryczny iloczyn wielkości produkcji i zysku ze sprzedaży dla poszczególnego produktu.
`    """
    
    sollution_T = sollution.transpose()
    fun = profits.dot(sollution_T)
    return fun

def production_volume(number_products:int, product_weights:np.array, time_1:np.array, time_2:np.array, time_3:np.array,
                      profits:np.array, total_time_1:int, total_time_2:int, total_time_3:int, total_weight:int):
    """
      Funkcja uwzględnia ograniczenia dla zadanego rozwiązania i sprawdza jego dopuszczalność
      
      Zwracamy rozwiązanie, którym jest wektor zawierający wielkość produkcji dla poszczególnego produktu 
`    """
    
    products = np.random.randint(1, 100, size=(1,number_products))
    products_T = products.transpose()

    while True:
      products = np.random.randint(1, 100, size=(1,number_products))
      products_T = products.transpose()
      if time_1.dot(products_T) <= total_time_1:
        break

    while True:
      products = np.random.randint(1, 100, size=(1,number_products))
      products_T = products.transpose()
      if time_2.dot(products_T) <= total_time_2:
        break

    while True:
      products = np.random.randint(1, 100, size=(1,number_products))
      products_T = products.transpose()
      if time_3.dot(products_T) <= total_time_3:
        break

    while True:
      products = np.random.randint(1, 100, size=(1,number_products))
      products_T = products.transpose()
      if product_weights.dot(products_T) <= total_weight:
        break
    return products

def main():
    number_products = 10
    product_weights, time_1, time_2, time_3, profits, total_time_1, total_time_2, total_time_3, total_weight  = parameters(number_products)
    products = production_volume(number_products, product_weights, time_1, time_2, time_3,
                      profits, total_time_1, total_time_2, total_time_3, total_weight)
    products_T = products.transpose()

    print(total_time_1)
    print(time_1.dot(products_T))
    print(total_time_2)
    print(time_2.dot(products_T))
    print(total_time_3)
    print(time_3.dot(products_T))
    print(total_weight)
    print(product_weights.dot(products_T))
    print(function(profits, products))
    print(products) 

if __name__ == "__main__":
    main()