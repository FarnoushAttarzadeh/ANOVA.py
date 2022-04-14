import sys
#sys.path.append('E:\Data')
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

Site='Negrocreek'
Year='2010'




dff = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-2010-Negrocreek.csv')
column_labels =list( dff.columns.get_values())

slopearray=[]

for column in dff:
    #print(np.array(df[column]))
    slopearray.append(np.array(dff[column]))
Slopearray=np.array(slopearray)
SLOPEARRAY=np.reshape(Slopearray,(-1,26))

SLOPEARRAY=np.around(SLOPEARRAY, decimals=2)
#SLOPEARRAY=np.delete(SLOPEARRAY,0,0)
print(SLOPEARRAY)




SLOPEARRAY2=SLOPEARRAY.copy()

#A=[]

#for j in np.arange(r):
#    for k in np.arange(c):

np.warnings.filterwarnings('ignore')
A=np.argwhere(SLOPEARRAY2 > 2)
print(A)

[r,c]=A.shape
print(r,c)

'''''
for i in  np.arange(r):
    for j in r:
        for k in np.arange(c):
            for n in c:


'''''


y=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5,8,8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12,12.5,13]

print(len(y),SLOPEARRAY[1],len(SLOPEARRAY[1]))

i=1

while i <len(SLOPEARRAY):
    fig=plt.figure(1)
    plt.plot(SLOPEARRAY[i],y,'.-',label=column_labels[i])
    i=i+1

plt.xlabel('Slope where the Phi is Max')
plt.ylabel('Height')
plt.title('Max slope for different heights and months')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0,+2.5, 0.25))
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


B = []
A = []
j = 1

while j < len(SLOPEARRAY):
    A = runningmean(SLOPEARRAY[j],9)

    B = np.arange(1, len(A) + 1, 1)

    fig= plt.figure(2)
    plt.plot(A, B, '-*', label=column_labels[j])

    j = j + 1

plt.xlabel('Slope where the correlation is Max')
plt.ylabel('Height')
plt.title('Moving average of max slope for different heights and months')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt= Site+' '+Year
fig.text(.8,.01, txt, ha='center')

plt.show()

print(len(A))