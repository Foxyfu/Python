import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], int)

array[2] = 0            #Замена 3 элемента на 0
array=array.reshape(3, 3)        #Преобразование в двух мерный массив

print('Массив:', array)
print('Присутсвует ли двойка в массиве?', 2 in array)
print('Кол-во строк и столбцов:', array.shape)