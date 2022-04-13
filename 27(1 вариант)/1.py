import pandas as pd
import numpy as np
nda1 = np.array([1, 2, 5, 9, -8, -9, -7, 0, 4])
df4 = pd.Series(nda1, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'])
print(df4.values)
print(df4.index)
df4[0]
df4[2]
df4[4]
print('Элементы больше 2', df4[df4>2])
df4.loc[df4>0] = 0      # Меняем отрицательные элементы на 1
df4.loc[df4<0] = 1      # Меняем положительные элементы на 0
print(df4)
