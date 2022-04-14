import sys
sys.path.append('E:\Data')
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Site='Walsingham'
Year='2012'

dff = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Corrs\Harrow\MaxC-2012-Wal.csv')
column_labels =list( dff.columns.get_values())

correarray=[]

for column in dff:
    #print(np.array(df[column]))
    correarray.append(np.array(dff[column]))
Correarray=np.array(correarray)
CORREARRAY=np.reshape(Correarray,(-1,26))

CORREARRAY=np.around(CORREARRAY, decimals=2)
print(CORREARRAY)


y=[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13]

i=1

while i <len(CORREARRAY):
    fig=plt.figure(1)
    plt.plot(CORREARRAY[i],y,'.-',label=column_labels[i])
    i=i+1

plt.xlabel('Value of maximum correlations')
plt.ylabel('Height')
plt.title('Max Correlation for different heights and months')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0,1.25, 0.25))
plt.yticks(np.arange(0, max(y)+1,2.5))

plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()


txt= Site+' '+Year
fig.text(.8,.01, txt, ha='center')


###############################################################                Running Mean           ###########################################################

def runningmean(value, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(value, weights, 'valid')
    return smas


B=[]
A = []
j=1

while j < len(CORREARRAY):


    A = runningmean(CORREARRAY[j],9)

    B=np.arange(1,len(A)+1,1)

    fig=plt.figure(2)
    plt.plot(A,B,'-*',label=column_labels[j])



    j = j + 1


plt.xlabel('Value of maximum correlations')
plt.ylabel('Height')
plt.title('Moving average of max correlation for different heights and months')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt= Site+' '+Year
fig.text(.8,.01, txt, ha='center')




plt.show()














