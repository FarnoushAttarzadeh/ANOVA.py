import numpy as np
import math as mt
import pylab
import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker
import scipy.interpolate as si
import pandas as pd
#import seaborn as sns



matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'



#####  Time array #####
#xat = np.loadtxt('e:/Data/re200805.walsingham/longdatat.dat', delimiter=',', unpack=True)
#print(xat)
# read # rows and columns from rowcol array - used for
# all files EXCEPT the time file, which has 5 columns

nrc = np.loadtxt(r'C:\Users\Farnoush\Desktop\Data\rowcol.dat', delimiter=',', unpack=True)
#print(nrc)
# Note nrc[0] is not actually used but keep it for sanity checks.

#print(nrc[0], nrc[1])

# split up string into the desired 2-D array
# -create a new 2-D array with 5 columns and nrc[1] rows

#time_array = np.reshape(xat, (-1, 5))


# ========================================================
######  Repeat for 3 remaining arrays ######
#    - note nrc[] is good for all arrays.

Site='Negrocreek'
Year='2009'
month='06'

address=r'C:\Users\Farnoush\Desktop\Data\LaCie\Sites\Negrocreek\2009\Jun\re200906.negrocreek'


# Wind magnitudes


xav = np.loadtxt('{}/longdatav.dat'.format(address), delimiter=',', unpack=True)
#print(xav)

# split up string into the desired 2-D array
# -create a new 2-D array with nrc[0] rows and nrc[1] columns
# (though the program re-calculates nrc[0] for itself)
vmag_array = np.reshape(xav, (-1, int(nrc[1])))


# Wind directions
xaph = np.loadtxt('{}/longdataph.dat'.format(address), delimiter=',', unpack=True)

#print(xaph)
# split up string into the desired 2-D array

vphi_array = np.reshape(xaph, (-1, int(nrc[1])))



## vertical winds
xaw = np.loadtxt('{}/longdataw.dat'.format(address), delimiter=',', unpack=True)

xaw=xaw/10.0

#print(xaw)
# split up string into the desired 2-D array

w_array = np.reshape(xaw, (-1, int(nrc[1])))



# ====================================================

# sample extraction of rows and columns for vmag
# a row is data for all heights at a given time
# a column is all data for all times at a given height
# ** Note first rows and columns are index = 0 (ZERO!)
n=1
COR=[]
SLOPE=[]
while  n<  int(nrc[1]):
    vcol=vmag_array[:, n]

   # print(vcol)

    wcol =w_array[:, n]

    #print((wcol))

    phcol=vphi_array[:,n]

    #print((phcol))
    tlen=len(wcol)

    #print (len(vcol),len(wcol),len(phcol))


    #print (vcol, wcol, phcol)



    teta = 1.0  # angle of  beam from vertical
    p = np.pi


    Sumw=[]
    Sumwmag=[]
    ncount=[]
    averw=[]
    avermag=[]

    phi0=0.
    Cor=[]
    Slope=[]

    while phi0 <360.0:
        Wcoli = []
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


                        #print (i,vcol[i],phcol[i],wcol[i],phi0)

                        wmag = vcol[i]* (np.sin(teta * p / 180)) * (np.cos((phcol[i] + 180 - phi0) * p / 180))
                        Wmag.append(wmag)
                        ncount=ncount+1.0

                        sumw=sumw+wcol[i]      #sum of measured w
                        sumwmag=sumwmag+wmag   #sum of modeled w (wmag)
                        wmag2 = wmag2 + wmag * wmag

                        multisum=multisum+wcol[i]*wmag


            i=i+1

        summulti=sumwmag*sumw
        sumwmag2 = sumwmag * sumwmag
        #print(ncount,n)
        averw= sumw/ncount
        avermag = sumwmag/ncount

        slope=((ncount*multisum-summulti)/(ncount*wmag2-sumwmag2))
        #print(slope)

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



        phi0=phi0+10.0
        Cor.append(cor)
        Slope.append(slope)

    COR.append(Cor)
    SLOPE.append(Slope)

    #print(Slope)
    #print(Cor)
    #print(len(Cor))
    n=n+1

#print(SLOPE)
#print(COR)

CORarray = np.reshape(COR, (-1, 36))
#print(CORarray)
print(len(CORarray))

CORARRAY=np.array(CORarray)


SLOPErshape=np.reshape(SLOPE,(-1,36))
#print(SLOPErshape)
print(len(SLOPErshape))

SLOPERESHAPE=np.array(SLOPErshape)







#############################################################        Finding the Maxes        #####################################################################


MaxCors = np.amax(CORARRAY, axis=1)

print ('Max cores are:', MaxCors)
#print("lenght of MaX Cores:",len(MaxCors))




Indcore = np.argmax(CORARRAY, axis=1)
Maxphcor = [(i) * 10 for i in Indcore]

print('phases where correlation is max are:',Maxphcor)




MaxSlopes = np.amax(SLOPERESHAPE, axis=1)

print ('Max slopes are:', MaxSlopes)
#print("lenght of MaX Slopes:",len(MaxSlopes))




Indslope = np.argmax(SLOPERESHAPE, axis=1)
Maxphslope = [(i)* 10 for i in Indslope]

print('phases where slope is max are:',Maxphslope)










########################################################    Finding slopes where the correlation is max        ####################################################

MaxSlopeCor= SLOPERESHAPE[np.arange(len(CORARRAY)), np.argmax(CORARRAY, axis=1)]

print('These are the slopes where correlations are max:',MaxSlopeCor)







#########################################################        saving and reading  results  of phies in a csv file           ############################################################




#df = pd.DataFrame([])
Maxphcorearray=np.array(Maxphcor)

df = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Phies\Negrocreek\MaxP-'+Year+'-'+Site+'.csv')
print('Maxphcorearray:',Maxphcorearray,'lenght:',len(Maxphcorearray))

df[Year+month] =Maxphcorearray


df.to_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Phies\Negrocreek\MaxP-'+Year+'-'+Site+'.csv',index=False)



print(df)

df = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Phies\Negrocreek\MaxP-'+Year+'-'+Site+'.csv')
column_labels =list( df.columns.get_values())

Phiarray=[]

for column in df:
    #print(np.array(df[column]))
    Phiarray.append(np.array(df[column]))

Phiarray=np.array(Phiarray)
PHIARRAY=np.reshape(Phiarray,(-1,26))

print(PHIARRAY)



print(Phiarray.dtype,len(PHIARRAY),column_labels )


####################################### saving and reading  slopes where the correlation is max ##########################################################



MaxSlopeCorarray=np.array(MaxSlopeCor)
MAX=float(format(np.amax(MaxSlopeCorarray), '.2f'))

dff = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-'+Year+'-'+Site+'.csv')
dff[Year+month] =MaxSlopeCorarray
dff.to_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-'+Year+'-'+Site+'.csv',index=False)


dff = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-'+Year+'-'+Site+'.csv')
column_labels =list( dff.columns.get_values())

slopearray=[]

for column in dff:
    #print(np.array(df[column]))
    slopearray.append(np.array(dff[column]))
Slopearray=np.array(slopearray)
SLOPEARRAY=np.reshape(Slopearray,(-1,26))

SLOPEARRAY=np.around(SLOPEARRAY, decimals=2)
print(SLOPEARRAY)





############################################# saving and  reading results for maximum correlation ######################################################


MaxCors=np.array(MaxCors)
MAX=float(format(np.amax(MaxCors), '.2f'))

dff = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Corrs\Negrocreek\MaxC-'+Year+'-'+Site+'.csv')
dff[Year+month] =MaxCors
dff.to_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Corrs\Negrocreek\MaxC-'+Year+'-'+Site+'.csv',index=False)


dff = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Corrs\Negrocreek\MaxC-'+Year+'-'+Site+'.csv')
column_labels =list( dff.columns.get_values())

MaxCorsarray=[]

for column in dff:
    #print(np.array(df[column]))
    MaxCorsarray.append(np.array(dff[column]))
MaxCorsarray=np.array(MaxCorsarray)
MAXCORRSARRAY=np.reshape(MaxCorsarray,(-1,26))

MAXCORRSARRAY=np.around(MAXCORRSARRAY, decimals=2)
print(MAXCORRSARRAY)




###################################################################################################################################################################
#############################################################       CORRELATION     PLOT      #####################################################################



fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)
#ax.set_title('Correlation')
plt.title('Correlation')
plt.xlabel('Angle(°)')
plt.ylabel('Altittude(km)')




scale_x = 0.1
scale_y =2

ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_x))
ax.xaxis.set_major_formatter(ticks_x)

ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_y))
ax.yaxis.set_major_formatter(ticks_y)



#plt.imshow(CORARRAY)



pylab.pcolor(CORARRAY, cmap='jet',vmin=-0.8, vmax=0.8)


ax.set_aspect('auto')

#cax = fig.add_axes([0.25, 0.1, 0.77, 0.8])
#cax.get_xaxis().set_visible(False)
#cax.get_yaxis().set_visible(False)
#cax.patch.set_alpha(0)
#cax.set_frame_on(False)
plt.colorbar(orientation='vertical')
ax.minorticks_on()



ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax.grid(which='minor', linestyle='-', linewidth='0.5', color='black')

txt= Site+' '+Year+' '+month
fig.text(.8,.01, txt, ha='center')

plt.savefig(r'C:\Users\Farnoush\Desktop\Data\LaCie\Sites\Negrocreek\2010\Nov\'C'+Year+month+Site+'.png')


#plt.show()

##############################                           SLOPE       PLOT                ###############################################################################3



fig = plt.figure(figsize=(6, 3.2))

ax = fig.add_subplot(111)

plt.title('Slope')
plt.xlabel('Angle(°)')
plt.ylabel('Altittude(km)')





scale_x = 0.1
scale_y =2

#ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_x))
ax.xaxis.set_major_formatter(ticks_x)

#ticks_y = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/scale_y))
ax.yaxis.set_major_formatter(ticks_y)
levels=np.arange (0.0,2,0.1)



cs=pylab.pcolor(SLOPERESHAPE,cmap='jet')
cs.cmap.set_over('brown')


ax.set_aspect('auto')

#cax = fig.add_axes([0.25, 0.1, 0.77, 0.8])
#cax.get_xaxis().set_visible(True)
#cax.get_yaxis().set_visible(False)
#cax.patch.set_alpha(0)
#cax.set_frame_on(False)
cb=plt.colorbar(cs,orientation='vertical')

plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['grid.alpha'] = 1
plt.rcParams['grid.color'] = "#cccccc"

ax.minorticks_on()

ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
ax.grid(which='minor', linestyle='-', linewidth='0.5', color='black')


txt= Site+' '+Year+' '+month
fig.text(.8,.01, txt, ha='center')

plt.savefig(r'C:\Users\Farnoush\Desktop\Data\LaCie\Sites\Negrocreek\2010\Nov\'S'+Year+month+Site+'.png')

plt.show()


