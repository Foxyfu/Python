import numpy as np

array = np.random.randint(1, 10, (10), int)

array = array.reshape(5, 2)
print(array)
print('..................')

np.fill_diagonal(array, 0)
print(array)