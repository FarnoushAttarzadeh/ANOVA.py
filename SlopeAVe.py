import sys
sys.path.append('E:\Data')
import subprocess
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mpl




Site='Wilberforce'
Year='2009'
output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\plots\Wilberforce\Averages\Slopes\2009'



dff = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Wilberforce\MaxS-2009-Wilberforce.csv')
column_labels =list( dff.columns.get_values())

slopearray=[]

for column in dff:
    #print(np.array(df[column]))
    slopearray.append(np.array(dff[column]))
Slopearray=np.array(slopearray)

SLOPEARRAY=np.reshape(Slopearray,(-1,26))

SLOPEARRAY=np.around(SLOPEARRAY, decimals=3)
#SLOPEARRAY=np.delete(SLOPEARRAY,0,0)
#print(SLOPEARRAY,len(SLOPEARRAY))
SLOPEARRAY1=SLOPEARRAY[1:len(SLOPEARRAY)-1]



###################################################### (1)                                                 ###########################################################

AVE=[]
STD=[]

j=0
while j <26:
    Ave = []
    Std=[]
    i = 0


    while i< 10:
        A = [SLOPEARRAY1[i][j], SLOPEARRAY1[i+1][j], SLOPEARRAY1[i+2][j]]
        print(A)
        A = np.array(A)

        A = A[np.logical_not(np.isnan(A))]
        ave=np.nanmean(A)
        std=np.std(A)
        Ave.append(ave)
        Std.append(std)

        #print(ave,std)
        i=i+3


    AVE.append(Ave)
    STD.append(Std)
    #print(Ave)
    j = j + 1
print(AVE, len(AVE))

AVE=np.reshape(AVE,(-1,4))
STD=np.reshape(STD,(-1,4))
STD=np.around(STD, decimals=3)
print(STD)
#print(AVE[0,1])
#df = pd.DataFrame([])
#df['errorbar'] =STD

#df.to_csv(r'C:\Users\Farnoush\Desktop\Average.csv',index=False)



y=[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13]
nsteps=5
cmap = mpl.cm.hsv
    #gist_rainbow



colors = ["blue", "yellow" , "green", "orange"]
labels=['Winter','Spring','Summer','Fall']



j=0
while j <4:

    AVEI = AVE[:, j]
    STDI=STD[:,j]
    fig = plt.figure(1)
    plt.plot(AVEI, y, '.-',label=labels[j],color=colors[j])
    #plt.errorbar(AVEI, y, xerr=STDI)
    print(STDI)
    j=j+1



plt.xlabel('Slope')
plt.ylabel('Height')
plt.title('Height Vs. The average of slope ( seasonal average ) ')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt= Site+' '+Year
fig.text(.8,.01, txt, ha='center')









def mkdir_p(mypath):


    from errno import EEXIST
    from os import makedirs,path

    try:
        makedirs(mypath)
    except OSError as exc: # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else: raise



mkdir_p(output_dir)

fig.savefig('{}/Height Vs. The average of slope.png'.format(output_dir))
















#################################################            (2)     STD on the x axis                            ####################################################





y=[0.5,1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13]
nsteps=5
cmap = mpl.cm.hsv
    #gist_rainbow



colors = ["blue", "yellow" , "green", "orange"]
labels=['Winter','Spring','Summer','Fall']



j=0
while j <4:

    AVEI = AVE[:, j]
    STDI=STD[:,j]
    fig = plt.figure(3)

    plt.plot(STDI,y,'.-',label=labels[j],color=colors[j])

    print(STDI)
    j=j+1



plt.xlabel('STD')
plt.ylabel('Height')
plt.title('Hieght  Vs. Std of slopes  (Seasonal average )')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt= Site+' '+Year
fig.text(.8,.01, txt, ha='center')







def mkdir_p(mypath):


    from errno import EEXIST
    from os import makedirs,path

    try:
        makedirs(mypath)
    except OSError as exc: # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else: raise



mkdir_p(output_dir)

fig.savefig('{}/Hieght  Vs. Std of slopes.png'.format(output_dir))












#################################################################      (3)      Average Monthly and Heightly          ############################################################################
AVE2=[]
STD2=[]
j=0


while j <4:
   Ave2 = []
   Std2=[]
   i = 0
   while i< 24:
       B = [AVE[i][j], AVE[i+1][j], AVE[i+2][j]]
       B= np.array(B)
       ave2=np.nanmean(B)
       Ave2.append(ave2)
       std2 = np.nanstd(B)
       Std2.append(std2)

       print(ave2,std2)
       i=i+3


   AVE2.append(Ave2)
   STD2.append(Std2)
   print(Ave2)
   j = j + 1
#print(AVE2, len(AVE2))

#print(B,ave2)

AVE2=np.reshape(AVE2,(-1,8))
STD2=np.reshape(STD2,(-1,8))
STD2=np.around(STD2, decimals=3)

#print(AVE2)
print(STD2)


y=[1,2.5,4,5.5,7,8.5,10,11.5]
nsteps=5
cmap = mpl.cm.hsv
    #gist_rainbow



colors = ["blue", "yellow" , "green", "orange"]
labels=['Winter','Spring','Summer','Fall','Far','Farnoush']



j=0
while j <4:
    AVE2I = AVE2[j, :]
    STD2I=STD2[j,:]

    fig = plt.figure(2)
    plt.plot(AVE2I, y, '.-',label=labels[j],color=colors[j])
    plt.errorbar(AVE2I, y,yerr=STD2I)

    j=j+1







plt.xlabel('Slope')
plt.ylabel('Average Height')
plt.title('Average Hieght Vs. Averaged slopes(Seasonal average)')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt= Site+' '+Year
fig.text(.8,.01, txt, ha='center')







def mkdir_p(mypath):


    from errno import EEXIST
    from os import makedirs,path

    try:
        makedirs(mypath)
    except OSError as exc: # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else: raise



mkdir_p(output_dir)

fig.savefig('{}/Average Hieght Vs. Averaged slopes.png'.format(output_dir))















############################################################       (4)  STD on the x axis    #########################################################################


y=[1,2.5,4,5.5,7,8.5,10,11.5]
nsteps=5
cmap = mpl.cm.hsv
    #gist_rainbow



colors = ["blue", "yellow" , "green", "orange"]
labels=['Winter','Spring','Summer','Fall','Far','Farnoush']



j=0
while j <4:
    AVE2I = AVE2[j, :]
    STD2I=STD2[j,:]

    fig = plt.figure(4)
    plt.plot(STD2I, y, '.-',label=labels[j],color=colors[j])


    j=j+1





plt.xlabel('STD')
plt.ylabel('Average Height')
plt.title(' Average Height Vs. STD of slope(Seasonal average)')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt= Site+' '+Year
fig.text(.8,.01, txt, ha='center')


def mkdir_p(mypath):


    from errno import EEXIST
    from os import makedirs,path

    try:
        makedirs(mypath)
    except OSError as exc: # Python >2.5
        if exc.errno == EEXIST and path.isdir(mypath):
            pass
        else: raise



mkdir_p(output_dir)

fig.savefig('{}/Average Height Vs. STD of slope.png'.format(output_dir))









plt.show()
















