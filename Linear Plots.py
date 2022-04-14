import numpy as np
import math as mt
import pylab
import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker
from statistics import mean

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'



#####  Time array #####
#xat = np.loadtxt(r'C:\Users\Farnoush\Desktop\Data\LaCie\Sites\Wilberforce\2010\Jan\re201001.wilberforce/longdatat.dat', delimiter=',', unpack=True)
#print(xat)
# read # rows and columns from rowcol array - used for
# all files EXCEPT the time file, which has 5 columns

nrc = np.loadtxt(r'C:\Users\Farnoush\Desktop\Data\LaCie\Sites\Wilberforce\2010\Jan\re201001.wilberforce/rowcol.dat', delimiter=',', unpack=True)
#print(nrc)
# Note nrc[0] is not actually used but keep it for sanity checks.

#print(nrc[0], nrc[1])

# split up string into the desired 2-D array
# -create a new 2-D array with 5 columns and nrc[1] rows

#time_array = np.reshape(xat, (-1, 5))


# ========================================================
######  Repeat for 3 remaining arrays ######
#    - note nrc[] is good for all arrays.

# Wind magnitudes
xav = np.loadtxt(r'C:\Users\Farnoush\Desktop\Data\LaCie\Sites\Walsingham\Re2010\Months\Jan\Re201001.walsingham/longdatav.dat', delimiter=',', unpack=True)


#print(xav)

# split up string into the desired 2-D array
# -create a new 2-D array with nrc[0] rows and nrc[1] columns
# (though the program re-calculates nrc[0] for itself)
vmag_array = np.reshape(xav, (-1, int(nrc[1])))


# Wind directions
xaph = np.loadtxt(r'C:\Users\Farnoush\Desktop\Data\LaCie\Sites\Walsingham\Re2010\Months\Jan\Re201001.walsingham/longdataph.dat', delimiter=',', unpack=True)

#print(xaph)
# split up string into the desired 2-D array

vphi_array = np.reshape(xaph, (-1, int(nrc[1])))



## vertical winds
xaw = np.loadtxt(r'C:\Users\Farnoush\Desktop\Data\LaCie\Sites\Walsingham\Re2010\Months\Jan\Re201001.walsingham/longdataw.dat', delimiter=',', unpack=True)

xaw=xaw/10.0

#print(xaw)
# split up string into the desired 2-D array

w_array = np.reshape(xaw, (-1, int(nrc[1])))



# ====================================================

# sample extraction of rows and columns for vmag
# a row is data for all heights at a given time
# a column is all data for all times at a given height
# ** Note first rows and columns are index = 0 (ZERO!)


n=15
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


phi0=40.0



Wcoli = []
Wmag=[]
I = []
wmag2=0.0

ncount=0.0

i=0

while i < tlen:
            if vcol[i] >-1000.0:
                if phcol[i]>-1000.0:
                   if wcol[i]>-100.0:
                        I.append(i)
                        Wcoli.append(wcol[i])


                        #print (i,vcol[i],phcol[i],wcol[i],phi0)

                        wmag =( vcol[i]* (np.sin(teta * p / 180))) * (np.cos((phcol[i] + 180 - phi0) * p / 180))
                        Wmag.append(wmag)
            i=i+1


#plt.scatter(I,Wmag)

#plt.scatter(I,Wcoli)

fig=plt.scatter(Wmag,Wcoli)
plt.title('Scatter Plot of Vertical wind Vs. Horizontal wind')
plt.xlabel('Horizontal Wind [m/s]')
plt.ylabel('Vertical Wind [m/s]')

plt.text(10,9,'Walsingham-2010-Feb', ha='center')


######################################          Best Fit Line        ###################################################


Wmag=np.array(Wmag)
Wcoli=np.array(Wcoli)



def best_fit_slope_and_intercept(xs, ys):
    m = (((mean(xs) * mean(ys)) - mean(xs * ys)) /
         ((mean(xs) * mean(xs)) - mean(xs * xs)))

    b = mean(ys) - m * mean(xs)

    return m, b


m, b = best_fit_slope_and_intercept(Wmag,Wcoli)

print(m, b)


regression_line = [(m*x)+b for x in Wmag]

plt.plot(Wmag, regression_line,color='red',label='regression line')

correlation_matrix = np.corrcoef(Wmag,Wcoli)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2

print(r_squared)




plt.show()