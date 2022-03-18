import numpy as np

array = np.random.randint(-5, 4, (5, 8))

print(f'{array} \n .........................')

print ('Количество нулей:', len(np.nonzero(array == 0)[0]))
print ('Количество положительных элементов:', len(np.nonzero(array > 0)[0]))
print ('Количество отрицательных элементов:', len(np.nonzero(array < 0)[0]))

