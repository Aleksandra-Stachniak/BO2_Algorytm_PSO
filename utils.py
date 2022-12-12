import numpy as np

def function(sollution:np.array, profits:np.array):
    """
      Funkcja obliczająca wartość funkcji celu. 
      Naszą funkcją celu jest sumaryczny iloczyn wielkości produkcji i zysku ze sprzedaży dla poszczególnego produktu.
`    """
    
    sollution_T = sollution.transpose()
    fun = profits.dot(sollution_T)
    return np.array(fun)

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

