import sys
sys.path.append(r'C:\Users\Farnoush\Desktop\DataCodes')
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import correlation

Slope=correlation.SLOPERESHAPE
Correlation=correlation.CORARRAY

pearson = np.corrcoef(Slope,Correlation)
print('pearson=',pearson)
print(len(pearson))

np.savetxt(r'C:\Users\Farnoush\Desktop\Data\LaCie\Pearson-Wil-201011.csv',pearson , delimiter=",")

