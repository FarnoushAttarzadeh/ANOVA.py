import subprocess
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import csv

Site = 'Walsingham'
Year = '2010'
#output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\plots\Negrocreek\Moving Averages2\Slopes\2009'
output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Examples'


dff = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2010-Wal.csv')
column_labels = list(dff.columns.get_values())

slopearray = []

for column in dff:
    # print(np.array(df[column]))
    slopearray.append(np.array(dff[column]))
Slopearray = np.array(slopearray)

SLOPEARRAY = np.reshape(Slopearray, (-1, 26))

SLOPEARRAY = np.around(SLOPEARRAY, decimals=3)

SLOPEARRAY1 = SLOPEARRAY[1:len(SLOPEARRAY) - 1]

#print(SLOPEARRAY1,len(SLOPEARRAY1))
# print(SLOPEARRAY1[:,0])


###########################################  dff ######################################################################

del dff['Heights']

dff.drop(dff.columns[[12]],axis=1,inplace=True)

dff["LastColumn"] = np.nan

#adjusted_columns (11)
#print('dff:', dff)



##################################################        (1)       DataFrame  (Running   Mean)            #############


dfm = dff.rolling(3, axis=1, min_periods=1,closed=None).mean()
dfm.drop(dfm.columns[[0, 1,12]], axis=1, inplace=True)
#print('dfm:', dfm)

# dfm.plot();


# dfmT=dfm.T
# print(dfmT)
# dfmT.plot();


RolMean = []

for column in dfm:
    RolMean.append(np.array(dfm[column]))
RolMean = np.array(RolMean)
ROLMEAN = np.reshape(RolMean, (-1, 26))
#print('ROLEMEAN', ROLMEAN, len(ROLMEAN))



y = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13]

i = 0

while i < len(ROLMEAN):
    fig = plt.figure(1)
    #print(ROLMEAN[i])
    plt.plot(ROLMEAN[i], y, '.-', label=column_labels[i + 2])
    i = i + 1

plt.xlabel('Moving Mean')
plt.ylabel('Height')
plt.title('Height Vs.Moving average ')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0, +2, 0.25))
plt.yticks(np.arange(0, max(y) + 1, 2.5))

plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt = Site + ' ' + Year
fig.text(.8, .01, txt, ha='center')


####################################### Saving the Graph   #############################################################


def mkdir_p(mypath):
    from errno import EEXIST
    from os import makedirs, path

    try:
        makedirs(mypath)
    except OSError as exc:  # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else:
            raise


mkdir_p(output_dir)

#fig.savefig('{}/Height Vs.Moving average.png'.format(output_dir))

########################################################################################################################

##################################################          (2)     DataFrame  (Running   STD)            ##############


dfs = dff.rolling(3,min_periods=1, axis=1).std()
dfs.drop(dfs.columns[[0,1]] , axis=1, inplace=False)



# dfsT=dfs.T
# print(dfsT)


RolStd = []

for column in dfs:
    # print(np.array(df[column]))
    RolStd.append(np.array(dfs[column]))
RolStd = np.array(RolStd)
ROLSTD = np.reshape(RolStd, (-1, 26))
#print('ROLSTD:', ROLSTD, len(ROLSTD))

y = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13]

i = 0

while i < len(ROLSTD):
    fig = plt.figure(2)
    plt.plot(ROLSTD[i], y, '.-', label=column_labels[i +1])
    i = i + 1

plt.xlabel('Moving STD')
plt.ylabel('Heights')
plt.title('Height Vs.Moving STD')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0, 1, 0.1))
plt.yticks(np.arange(0, max(y) + 1, 2.5))

plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt = Site + ' ' + Year
fig.text(.8, .01, txt, ha='center')


################################################################### Saving the Graph ##################################


def mkdir_p(mypath):
    from errno import EEXIST
    from os import makedirs, path

    try:
        makedirs(mypath)
    except OSError as exc:  # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else:
            raise


# output_dir = r'C:\ Users\Farnoush\Desktop\Data\LaCie\Maxes\plots\Wilberforce\Moving Averages1\Slopes\2009'
mkdir_p(output_dir)

#fig.savefig('{}/Height Vs.Moving STD.png'.format(output_dir))

########################################################################################################################

##################################################        (3)       DataFrame  (Running   Mean both dimensions) ########
dfm.loc[len(dfm)] = 'Nan'

dfmm = dfm.rolling(3, min_periods=1, axis=0,closed=None).mean()
dfmm = dfmm.drop([0, 1], axis=0)
#print('dfmm:', dfmm)

dfmmT = dfmm.T
#print(dfmmT)
# dfmT.plot();


RolMean1 = []

for column in dfmm:
    RolMean1.append(np.array(dfmm[column]))
RolMean1 = np.array(RolMean1)
ROLMEAN1 = np.reshape(RolMean1, (-1, 25))
#print('ROLEMEAN1', ROLMEAN1, len(ROLMEAN1))

y = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,12.75]

#cmap = plt.get_cmap('color')
#prop_cycle = plt.rcParams['axes.prop_cycle']
#colors = prop_cycle.by_key()['color']

i = 0
#N=9
#color = cmap(float(i)/N)
while i < len(ROLMEAN1):
    fig = plt.figure(3)
    plt.plot(ROLMEAN1[i], y, '.-', label=column_labels[i + 2])
    i = i + 1





plt.xlabel('Moving Average of Slope (°)')
plt.ylabel('Averaged Height (km)')
plt.title('Moving Average Height Vs.Moving Average Slope')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0, +2, 0.25))
plt.yticks(np.arange(0, max(y) + 1, 2.5))

plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt = Site + ' ' + Year
fig.text(.8, .01, txt, ha='center')


################################################################### Saving the Graph ##################################


def mkdir_p(mypath):
    from errno import EEXIST
    from os import makedirs, path

    try:
        makedirs(mypath)
    except OSError as exc:  # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else:
            raise


# output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\plots\Wilberforce\Moving Averages1\Slopes\2009'
mkdir_p(output_dir)

#fig.savefig('{}/M-Average-S-Eureka-2009.png'.format(output_dir))

########################################################################################################################


##################################################        (4)       DataFrame  (Running   STD both dimensions) #########
dfs.loc[len(dfs)] = 'Nan'

dfss = dfs.rolling(3, min_periods=1, axis=0,closed=None).std()
dfss = dfss.drop([0,1], axis=0)
#print('dfss:', dfss)

dfssT = dfss.T
#print(dfssT)

RolStd1 = []

for column in dfss:
    # print(np.array(df[column]))
    RolStd1.append(np.array(dfss[column]))
RolStd1 = np.array(RolStd1)
ROLSTD1 = np.reshape(RolStd1, (-1, 25))
#print('ROLESTD1', ROLSTD1, len(ROLSTD1))

y = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,12.75]

i = 0

while i < len(ROLSTD1):
    fig = plt.figure(4)
    #print(i, ROLSTD1[i])
    plt.plot(ROLSTD1[i], y, '.-', label=column_labels[i+1 ])
    i = i + 1

plt.xlabel('Moving StD of slope (°)')
plt.ylabel('Averaged Height (km)')
plt.title(' Moving Averaged Height Vs.Moving Standard Deviation of Slope')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0, +1, 0.1))
plt.yticks(np.arange(0, max(y) + 1, 2.5))

plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt = Site + ' ' + Year
fig.text(.8, .01, txt, ha='center')


######################################################            Saving the Graph    ##################################


def mkdir_p(mypath):
    from errno import EEXIST
    from os import makedirs, path

    try:
        makedirs(mypath)
    except OSError as exc:  # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else:
            raise


 #output_dir = r'C:\ Users\Farnoush\Desktop\Data\LaCie\Maxes\plots\Wilberforce\Moving Averages2\Slopes\2010'
mkdir_p(output_dir)

fig.savefig('{}/M-STD-S-Walsingham-2010.png'.format(output_dir))

#######################################           Averages of STD         ##############################################




'''

RolStd1 = RolStd1[~np.isnan(RolStd1)]
#print(RolStd1)

PowStd=np.power(RolStd1, 2)

total=np.sum(PowStd)
count=len(PowStd)

wtotal=total/count

rwtotal=np.sqrt(wtotal)

print('Powstd:',PowStd,'len powstd:' ,len(PowStd),'count:',count,'total:',total,'wtotal:',wtotal,'rwtotal:',rwtotal)

mydict={Site+' '+Year:rwtotal}


with open(r'C:\ Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\STDs2.csv', 'a+',newline='' ) as f:
    fieldnames = ['Sites-Year','STD']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    data = [dict(zip(fieldnames, [k, v])) for k, v in mydict.items()]
    writer.writerows(data)







############################################# Standard Deviation of Standard Deviations ##############################
print('dfm:',dfm)
print('RolMean:', RolMean, len(RolMean))
print('dfmm:',dfmm)
print('RolMean1', RolMean1, len(RolMean1))



print('dff:',dff)
print('dfs:',dfs)
print('ROLSTD:', ROLSTD, len(ROLSTD))
print('dfss:',dfss)
print('ROLESTD1', ROLSTD1, len(ROLSTD1))


STDstd=[]



STDstd={Site+' '+Year:dfss.std(axis=0,skipna=True)}
Dff=pd.DataFrame(STDstd)
#Dff=Dff.drop('201012')
#Dff.to_csv(r'C:\ Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\STDstd.csv',mode='a')


print('STDstd:',STDstd,type(STDstd))
#print (np.std(dfss, axis=0))










#########################################   Seasonal Averages of STDs  #################################################



RolstdWi=RolStd1[0:4,:]
RolstdSp=RolStd1[2:6,:]
RolstdSu=RolStd1[4:8,:]
RolstdFa=RolStd1[6:10,:]



#print(RolstdWi)
#print(RolstdSp)
#print(RolstdSu)
#print(RolstdFa)

RolstdWi = RolstdWi[~np.isnan(RolstdWi)]
RolstdSp = RolstdSp[~np.isnan(RolstdSp)]
RolstdSu = RolstdSu[~np.isnan(RolstdSu)]
RolstdFa = RolstdFa[~np.isnan(RolstdFa)]


print('RolstdWi:',RolstdWi,len(RolstdWi))
print('RolstdSp:',RolstdSp,len(RolstdSp))
print('RolstdSu:',RolstdSu,len(RolstdSu))
print('RolstdFa:',RolstdFa,len(RolstdFa))





def Seasonal( Rol ):



   PowStd = np.power(Rol, 2)

   total = np.sum(PowStd)
   count = len(PowStd)

   wtotal = total / count

   rwtotal = np.sqrt(wtotal)

   print(PowStd, len(PowStd), count, total, wtotal, rwtotal)


   return(rwtotal)





Winter=Seasonal(RolstdWi)

Spring=Seasonal(RolstdSp)

Summer=Seasonal(RolstdSu)

Fall=Seasonal(RolstdFa)

print('Winter:',Winter,'Spring:',Spring,'Summer:',Summer,'Fall:',Fall)


SeasonalSTDs={Site+' '+Year:{'Winter': Winter ,'Spring': Spring ,'Summer': Summer,'Fall': Fall}}


print('SeasonalSTDs:',SeasonalSTDs)


Df=pd.DataFrame(SeasonalSTDs)

#Df.to_csv(r'C:\ Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\SeasonalSTDs.csv',mode='a')

'''

plt.show()