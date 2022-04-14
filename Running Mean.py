import numpy as np
import matplotlib.pyplot as plt

dataset=[1,5,3,7,5,7,7,10,9,1,12,15,17,25,16,16,27,31,35,37,38,39,41,42,45,47]

def runningmean (value, window):
    weights=np.repeat(1.0,window)/window
    smas=np.convolve(value,weights,'valid')
    return smas





A=[]
A= runningmean (dataset,5)
print(A,len(runningmean(dataset,5)))

plt.plot(dataset)
plt.plot(runningmean(dataset,5))
plt.show()

#y=[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13]
y=[1.75,2.25,2.75,3.25,3.75,4.25,5.25,5.75,6.25,6.75,7.42,6.5,8.75,9.42,10.1,10.75]

print(len(y))