import numpy as np
import math as mt
import pylab
import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker
import pandas as pd


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
xaw=xaw/10.
#print(xaw)
# split up string into the desired 2-D array

w_array = np.reshape(xaw, (-1, int(nrc[1])))



# ====================================================


n=10

vcol=vmag_array[:, n]

#print(vcol)

wcol =w_array[:,n]

#print((wcol))

phcol=vphi_array[:,n]

#print((phcol))
tlen=len(wcol)

#print (len(vcol),len(wcol),len(phcol))


#print (vcol, wcol, phcol)



teta =1.5
# angle of  beam from vertical
p = np.pi


Sumw=[]
Sumwmag=[]
ncount=[]
averw=[]
avermag=[]

phi0=340.
Cor=[]
Slope=[]


Wcoli = []
Vcoli=[]
Phcoli=[]
Wmag=[]
I = []
wmag2=0.0
sumw=0.0
sumwmag=0.0
sumwmag2=0.0
multisum=0.0
ncount=0.0

i=0

while i < tlen:
    if vcol[i] >-1000.0:
        if phcol[i]>-1000.0:
            if wcol[i]>-100.0:
                        I.append(i)
                        Wcoli.append(wcol[i])
                        Vcoli.append(vcol[i])
                        Phcoli.append(phcol[i])

                #print (i,vcol[i],phcol[i],wcol[i],phi0)

                        wmag = (vcol[i]) * (np.sin(teta * p / 180)) * (np.cos((phcol[i] + 180 - phi0) * p / 180))
                        Wmag.append(wmag)
                        ncount=ncount+1.0
                        sumw=sumw+wcol[i]      #sum of measured w
                        sumwmag=sumwmag+wmag   #sum of modeled w (wmag)
                        wmag2 = wmag2 + wmag * wmag

                        multisum=multisum+wcol[i]*wmag


    i=i+1

a = np.array(Vcoli)
b = np.array(Phcoli)
c = np.array(Wcoli)
I = np.array(I)

d = np.array(Wmag)



df = pd.DataFrame({"Vcoli": a, "Phcoli": b, "Wcoli": c, "Wmag": d, "I": I})


df.to_csv("E:\Data\Slope\ test-13-340-t1.5.csv", index=False)

summulti=sumwmag*sumw
sumwmag2 = sumwmag * sumwmag
averw= sumw/ncount
avermag = sumwmag/ncount

slope=((ncount*multisum-summulti)/(ncount*wmag2-sumwmag2))
print(slope)

#print(multisum)
#print(summulti)
#print(lope)
#print(Wcoli)
#print(len(Wcoli))

#print (ncount,',',sumw,',',sumwmag,',',averw,',',avermag)
# print(Wcoli[1])
#print(Wmag)

sumwdev2=0
sumwmagdev2=0
sumcross=0
j=0
while j<len(Wcoli):

            wdev=Wcoli[j]-averw
            wmagdev=Wmag[j]-avermag

            cross=wdev*wmagdev
            sumcross=sumcross+cross

            wdev2=wdev*wdev
            wmagdev2=wmagdev*wmagdev

            sumwdev2=sumwdev2+wdev2
            sumwmagdev2=sumwmagdev2+wmagdev2

            #print(wdev,',', wdev2,',',wmagdev,',',wmagdev2)
            #print(sumwdev2,',', sumwmagdev2,',',sumcross)

            j=j+1

            rw=mt.sqrt(sumwdev2)
            rwmag=mt.sqrt(sumwmagdev2)


            cor=sumcross/(rw*rwmag)






print(slope)
print(cor)


