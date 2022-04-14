import sys
sys.path.append('E:\Data')
import subprocess
import numpy as np


import correlation as cr

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print(sys.path)


####################################                        PHies                     ######################################################################################



PHIARRAY=cr.PHIARRAY

print(len(PHIARRAY))

y=[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13]

i=1

while i <len(PHIARRAY):
    plt.plot(PHIARRAY[i],y,'.-',label=cr.column_labels[i])
    i=i+1

plt.xlabel('Max Phi')
plt.ylabel('Height')
plt.title('Max Phi for different heights and months')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0,400, 50))
plt.yticks(np.arange(0, max(y)+1,2.5))

plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()




plt.show()



#########################################################                        Slopes            ############################################################################

SLOPEARRAY=cr.SLOPEARRAY

y=[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13]

i=1

while i <len(SLOPEARRAY):
    plt.plot(SLOPEARRAY[i],y,'.-',label=cr.column_labels[i])
    i=i+1

plt.xlabel('Slope where the Phi is Max')
plt.ylabel('Height')
plt.title('Max slope for different heights and months')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0,cr.MAX+0.5, 0.25))
plt.yticks(np.arange(0, max(y)+1,2.5))

plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()




plt.show()
