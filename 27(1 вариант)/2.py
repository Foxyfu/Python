import pandas as pd
import numpy as np

nda1 = np.array([2, 5, 12, 9, 14, 19, 45, 22])
sr = pd.Series(nda1, index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print(sr[np.logical_and(10 < sr, sr < 20)].values) #вывод элементо от 10 до 20
sr.loc[(sr.values % 2 == 0)] +=3 # Прибавляем 3 к четным элементам
print(sr)


