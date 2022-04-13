from enum import unique
import numpy as np

array = np.random.randint(0, 30, (7, 5))
print(f'{array} \n ........................')

uniq = np.unique(array, return_counts = True )[1] == 1


print(np.unique(array)[uniq])


