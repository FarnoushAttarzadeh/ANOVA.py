import sys
sys.path.append('E:\Data')
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


Site='Negrocreek'
Year='2010'



df = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Phies\Negrocreek\MaxP-2010-Negrocreek.csv')
column_labels =list( df.columns.get_values())

Phiarray=[]

for column in df:
    #print(np.array(df[column]))
    Phiarray.append(np.array(df[column]))

Phiarray=np.array(Phiarray)
PHIARRAY=np.reshape(Phiarray,(-1,26))
#PHIARRAY=np.delete(PHIARRAY,0,0)

#print(PHIARRAY)

#print(len(PHIARRAY))


'''''''''
PHIARRAY2=[]

for j  in PHIARRAY:
    for element in PHIARRAY[j] :
        #if Phiarray[j][k]> 180:
           print(PHIARRAY[j])


'''''''''

result = np.where(PHIARRAY > 180)

incol=result[0]

inrow=result[1]

#print('result:',result,result[0],result[1],incol,inrow)

[r,c]=PHIARRAY.shape

PHIARRAY2=PHIARRAY.copy()



for i in np.arange(r):
    for j in np.arange(c):
        if PHIARRAY2[i][j] >=180:
            PHIARRAY2[i][j]=PHIARRAY[i][j]-360
            #print(PHIARRAY2[i][j])




#print(Phiarray.dtype,len(PHIARRAY),column_labels )


y=[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13]

i=1

while i <len(PHIARRAY2):
    fig=plt.figure(1)
    plt.plot(PHIARRAY2[i],y,'.-',label=column_labels[i])
    i = i + 1



plt.xlabel('The Phi where corr is max at ')
plt.ylabel('Height')
plt.title('Phies where the correlation is maximum at')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(-190,190, 50))
plt.yticks(np.arange(0, max(y)+1,2.5))

plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()




txt= Site+' '+Year
fig.text(.8,.01, txt, ha='center')
#plt.show()


#print(PHIARRAY2,len(PHIARRAY2))



###############################################################                Running Mean           ###########################################################

def runningmean(value, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(value, weights, 'valid')
    return smas


B=[]
A = []
j=1

while j < len(PHIARRAY2):


    A = runningmean(PHIARRAY2[j],9)

    B=np.arange(1,len(A)+1,1)

    fig=plt.figure(2)
    plt.plot(A,B,'-*',label=column_labels[j])
    print(A,np.arange(1,17,1))



    j = j + 1


plt.xlabel('The Phi where corr is max at ')
plt.ylabel('Height')
plt.title('Moving average of Phis where the correlation is maximum at')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.xticks(np.arange(-190,190, 50))
plt.yticks(np.arange(0, max(y)+1,2.5))

plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()


txt= Site+' '+Year
fig.text(.8,.01, txt, ha='center')


plt.show()