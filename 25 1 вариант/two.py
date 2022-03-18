import numpy as np


array = np.random.randint(-99, 100, (8, 6))
print(array)
print('...................................')

minimum = np.min(array)
minimum_index = np.where(array == minimum)
print(f'minimum: {minimum}, index: {minimum_index}')

maximum = np.max(array)
maximum_index = np.where(array == maximum)
print(f'maximmum: {maximum}, index: {maximum_index}')

array[maximum_index] = minimum
array[minimum_index] = maximum
print(f"modified: \n {array}")

