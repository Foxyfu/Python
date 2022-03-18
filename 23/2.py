import numpy as np
from random import uniform

array = np.array([round(uniform(-10, 10), 2) for i in range(45)], float)    #Создание массива
array = array.reshape(9,5)              #Преобразование в двух мерный
array[0].fill(1)                #Замены первой строки на 1

print('Массив:',array,'\n',
    "Последняя строка массива:", array[-1],'\n',
    'Кол-во строк и столбцов:', array.shape)