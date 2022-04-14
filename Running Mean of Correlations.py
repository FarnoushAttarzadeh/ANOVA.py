#import subprocess
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl
import csv




Site='Eureka'
Year='2009'
output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Examples'
#output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\plots\Negrocreek\Moving Averages2\Corrs\2010'


dff = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Corrs\Eureka\MaxC-2009-Eur.csv')

column_labels = list(dff.columns.get_values())



correarray=[]
for column in dff:

    correarray.append(np.array(dff[column]))

Correarray=np.array(correarray)
CORREARRAY=np.reshape(Correarray,(-1,26))

CORREARRAY=np.around(CORREARRAY, decimals=4)


CORREARRAY1=CORREARRAY[1:len(CORREARRAY)-1]




##########################################  dff ########################################################################

del dff['Heights']

dff.drop(dff.columns[[12]],axis=1,inplace=True)

dff["LastColumn"] = np.nan

#adjusted_columns (11)
#print('dff:', dff)





##################################################        (1)       DataFrame  (Running   Mean)            #############





dfm = dff.rolling(3, axis=1, min_periods=1).mean()
dfm.drop(dfm.columns[[0, 1]], axis=1, inplace=True)
print(dfm)

# dfm.plot();


#dfmT = dfm.T
#print(dfmT)
# dfmT.plot();


RolMean = []

for column in dfm:
    RolMean.append(np.array(dfm[column]))
RolMean = np.array(RolMean)
ROLMEAN = np.reshape(RolMean, (-1, 26))
print(ROLMEAN, len(ROLMEAN))

y = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13]

i = 0

while i < len(ROLMEAN):
    fig = plt.figure(1)
    plt.plot(ROLMEAN[i], y, '.-', label=column_labels[i + 2])
    i = i + 1

plt.xlabel('Moving Mean')
plt.ylabel('Height')
plt.title('Height Vs.Moving average ')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0,1,0.1 ))
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


dfs = dff.rolling(3, axis=1, min_periods=1).std()
dfs.drop(dfs.columns[[0, 1]], axis=1, inplace=True)
print(dfs)

#dfsT = dfs.T
#print(dfsT)

RolStd = []

for column in dfs:
    # print(np.array(df[column]))
    RolStd.append(np.array(dfs[column]))
RolStd = np.array(RolStd)
ROLSTD = np.reshape(RolStd, (-1, 26))
print(ROLSTD, len(ROLSTD))

y = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13]

i = 0

while i < len(ROLSTD):
    fig = plt.figure(2)
    plt.plot(ROLSTD[i], y, '.-', label=column_labels[i + 2])
    i = i + 1

plt.xlabel('Moving STD')
plt.ylabel('Heights')
plt.title('Height Vs.Moving STD')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0,0.5,0.05 ))
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


# output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\plots\Wilberforce\Moving Averages\Slopes\2009'
mkdir_p(output_dir)

#fig.savefig('{}/Height Vs.Moving STD.png'.format(output_dir))







########################################################################################################################




################################       (3)       DataFrame  (Running   Mean both dimensions)  ##########################


dfmm = dfm.rolling(3, min_periods=1, axis=0).mean()
dfmm = dfmm.drop([0, 1], axis=0)
print(dfmm)

#dfmmT = dfmm.T
#print(dfmmT)
# dfmT.plot();


RolMean1 = []

for column in dfmm:
    RolMean1.append(np.array(dfmm[column]))
RolMean1 = np.array(RolMean1)
ROLMEAN1 = np.reshape(RolMean1, (-1, 24))
print(ROLMEAN1, len(ROLMEAN1))

y = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5]

i = 0

while i < len(ROLMEAN1):
    fig = plt.figure(3)
    plt.plot(ROLMEAN1[i], y, '.-', label=column_labels[i + 2])
    i = i + 1

plt.xlabel('Moving Average of Correlation')
plt.ylabel('Averaged Height (km)')
plt.title('Moving Averaged Height Vs.Moving averaged correlation')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0,1,0.1 ))
plt.yticks(np.arange(0, max(y) + 1, 2.5))

plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt = Site + ' ' + Year
fig.text(.8, .01, txt, ha='center')





##########################################    Saving the Graph         #################################################


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


output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Examples'
mkdir_p(output_dir)

#fig.savefig('{}/M-Averages-C-Eureka-2009.png'.format(output_dir))




########################################################################################################################


################################       (4)       DataFrame  (Running   STD both dimensions)   ##########################


dfss = dfs.rolling(3, min_periods=1, axis=0).std()
dfss = dfss.drop([0, 1], axis=0)
print(dfss)

#dfssT = dfss.T
#print(dfssT)

RolStd1 = []

for column in dfss:
    # print(np.array(df[column]))
    RolStd1.append(np.array(dfss[column]))
RolStd1 = np.array(RolStd1)
ROLSTD1 = np.reshape(RolStd1, (-1, 24))
print(ROLSTD1, len(ROLSTD1))

y = [1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5]
i = 0

while i < len(ROLSTD1):
    fig = plt.figure(4)
    plt.plot(ROLSTD1[i], y, '.-', label=column_labels[i + 2])
    i = i + 1

plt.xlabel('Moving StD of Correlation')
plt.ylabel('Averaged Height (km)')
plt.title('Moving Averaged Height Vs.Moving Standard Deviation of Correlation')
plt.xlim(left=0)
plt.ylim(bottom=0)

plt.xticks(np.arange(0,0.5,0.05 ))
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


# output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\plots\Wilberforce\Moving Averages\Slopes\2009'
mkdir_p(output_dir)

fig.savefig('{}/M-STD-C-Eureka-2009.png'.format(output_dir))





#######################################           Averages of STD         ##############################################






RolStd1 = RolStd1[~np.isnan(RolStd1)]
#print(RolStd1)

PowStd=np.power(RolStd1, 2)

total=np.sum(PowStd)
count=len(PowStd)

wtotal=total/count

rwtotal=np.sqrt(wtotal)

print('Powstd:',PowStd,'len powstd:' ,len(PowStd),'count:',count,'total:',total,'wtotal:',wtotal,'rwtotal:',rwtotal)

mydict={Site+' '+Year:rwtotal}


with open(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Corrs\STDs2.csv', 'a+',newline='' ) as f:
    fieldnames = ['Sites-Year','STD']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    data = [dict(zip(fieldnames, [k, v])) for k, v in mydict.items()]
    writer.writerows(data)







#######################################    Standard Deviation of Standard Deviations    ################################
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
#Dff.to_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Corrs\STDstd.csv',mode='a')


print('STDstd:',STDstd,type(STDstd))
#print (np.std(dfss, axis=0))







plt.show()

