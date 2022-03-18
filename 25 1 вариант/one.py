import numpy as np

size = int(input('Введите размерность:'))

array = np.random.randint(0, 10, (size, size))

print(array, '\n', '.....................')

array_two = np.random.randint(0, 10, (size, size))

print(array_two, '\n', '.....................')

summ = array + array_two

print('Сумма матриц:','\n', summ, '\n', '.....................')


composition = (array.T * array_two.T)

print('Произведение транспонированных матриц','\n', composition)

sum_first_array = np.sum(array)     #Сумма элементов первого массива
sum_second_array = np.sum(array_two)    #Сумма элементов второго массива

print('Сумма элементов первого массива:',sum_first_array)
print('Сумма элементов второго массива:',sum_second_array)
print('первая сумма больше?',sum_first_array > sum_second_array)




