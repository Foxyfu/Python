import numpy as np


array = np.random.randint(0, 20, (10))
print(array)
print('...................................')

print(f'maximum: {np.max(array)}, minimum: {np.min(array)}')

minimum_ind = np.argmin(array)
maximum_ind = np.argmax(array)

if maximum_ind < minimum_ind:
    answer = np.sum(array[maximum_ind:minimum_ind]) 
    answer -=np.max(array)
else:
    answer = np.sum(array[minimum_ind:maximum_ind])
    answer -=np.min(array)
print('Summa:', answer)
