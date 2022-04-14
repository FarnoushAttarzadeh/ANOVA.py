import numpy as np
import math as mt
import pylab
import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker


matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'



#####  Time array #####
xat = np.loadtxt('e:/Data/longdatat.dat', delimiter=',', unpack=True)
#print(xat)
# read # rows and columns from rowcol array - used for
# all files EXCEPT the time file, which has 5 columns

nrc = np.loadtxt('e:/Data/rowcol.dat', delimiter=',', unpack=True)
#print(nrc)
# Note nrc[0] is not actually used but keep it for sanity checks.

#print(nrc[0], nrc[1])

# split up string into the desired 2-D array
# -create a new 2-D array with 5 columns and nrc[1] rows

time_array = np.reshape(xat, (-1, 5))


# ========================================================
######  Repeat for 3 remaining arrays ######
#    - note nrc[] is good for all arrays.

# Wind magnitudes
xav = np.loadtxt('e:/Data/longdatav.dat', delimiter=',', unpack=True)
#print(xav)

# split up string into the desired 2-D array
# -create a new 2-D array with nrc[0] rows and nrc[1] columns
# (though the program re-calculates nrc[0] for itself)
vmag_array = np.reshape(xav, (-1, int(nrc[1])))


# Wind directions
xaph = np.loadtxt('e:/Data/longdataph.dat', delimiter=',', unpack=True)

#print(xaph)
# split up string into the desired 2-D array

vphi_array = np.reshape(xaph, (-1, int(nrc[1])))



## vertical winds
xaw = np.loadtxt('e:/Data/longdataw.dat', delimiter=',', unpack=True)

xaw=xaw/10.0

#print(xaw)
# split up string into the desired 2-D array

w_array = np.reshape(xaw, (-1, int(nrc[1])))



# ====================================================

# sample extraction of rows and columns for vmag
# a row is data for all heights at a given time
# a column is all data for all times at a given height
# ** Note first rows and columns are index = 0 (ZERO!)


n=9
vcol=vmag_array[:,n ]

   # print(vcol)

wcol =w_array[:, n]

    #print((wcol))

phcol=vphi_array[:,n]

    #print((phcol))
tlen=len(wcol)

    #print (len(vcol),len(wcol),len(phcol))


#print (vcol, wcol, phcol)



teta = 10  # angle of  beam from vertical
p = np.pi
phi0=0.0
PH=[]
WColi=[]
WMag=[]

while phi0 < 360.0:

    Wcoli = []
    Wmag=[]
    I = []
    ncount=0.0
    i=0

    while i < tlen:
            if vcol[i] >-1000.0:
                if phcol[i]>-1000.0:
                   if wcol[i]>-100.0:
                        I.append(i)
                        Wcoli.append(wcol[i])


                        #print (i,vcol[i],phcol[i],wcol[i],phi0)

                        wmag = vcol[i]* (np.sin(teta * p / 180)) * (np.cos((phcol[i] + 180 - phi0) * p / 180))
                        Wmag.append(wmag)

            i=i+1

    phi0=phi0+10
    PH.append(phi0)
WColi.append(Wcoli)
WMag.append(Wmag)

#WCOLI= np.reshape(WColi, (-1,44))
#WMAG= np.reshape(WMag, (-1, 44))


#plt.figure(1)                # the first figure
#plt.subplot(211)             # the first subplot in the first figure
plt.scatter(Wcoli,Wmag)
#plt.subplot(212)             # the second subplot in the first figure
#plt.scatter(PH,WMAG)


plt.xlabel('Wcoli')
plt.ylabel('Wmag')
plt.show()