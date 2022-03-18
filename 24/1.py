import numpy as np

rows = int(input('Введите кол-во cтрок:'))
columns = int(input('Введите кол-во столбцов:'))

array = np.random.randint(-10, 0, (rows, columns))

print(array)  #Вывод матрицы
print('................................................')

summ = np.sum(array,axis = 0)   #находим сумма в столбце
position = np.argmax(summ)      #находим номер столбца
position +=1

print('Сумма:', summ, 'Столбец номер:', position )