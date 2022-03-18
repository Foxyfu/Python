import numpy as np

array = np.random.randint(-10, 10, (20))
print(f'{array} \n ........................')

maximum = np.max(array)
print('Максимум', maximum)

array = np.abs(array)
print('Элементов по модулю больше максимума', np.sum(array > maximum))