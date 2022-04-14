import subprocess
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import csv




Site='Walsingham'
Year='2011'
output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\plots\Walsingham\Moving Averages2\Phies\2011'


dff = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Phies\Walsingham\Maxp-2011-Wal.csv')




column_labels = list(dff.columns.get_values())




Phiarray=[]

for column in dff:
    #print(np.array(df[column]))
    Phiarray.append(np.array(dff[column]))
Phiarray=np.array(Phiarray)
PHIARRAY=np.reshape(Phiarray,(-1,26))



[r,c]=PHIARRAY.shape

PHIARRAY2=PHIARRAY.copy()

for i in np.arange(r):
    for j in np.arange(c):
        if PHIARRAY2[i][j] >=180:
            PHIARRAY2[i][j]=PHIARRAY[i][j]-360





##########################################  dff ########################################################################

del dff['Heights']

dff.drop(dff.columns[[12]],axis=1,inplace=True)

dff["LastColumn"] = np.nan

#adjusted_columns (11)
print('dff:', dff)





##################################################        (1)       DataFrame  (Running   Mean)            #############

m = dff >180
#df.where(m, -df)

dff=dff.where(m>180, 180-dff)

print(dff)

dfm = dff.rolling(3, axis=1, min_periods=1).mean()
dfm.drop(dfm.columns[[0, 1]], axis=1, inplace=True)
print(dfm)