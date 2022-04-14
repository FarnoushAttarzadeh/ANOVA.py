import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import matplotlib as mpl


Site='Eureka'
Year='2009'
output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Examples'


dff = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Eureka\MaxS-2009-Eur.csv')
column_labels =list( dff.columns.get_values())

slopearray=[]

for column in dff:
    #print(np.array(df[column]))
    slopearray.append(np.array(dff[column]))
Slopearray=np.array(slopearray)
SLOPEARRAY=np.reshape(Slopearray,(-1,23))

SLOPEARRAY=np.around(SLOPEARRAY, decimals=2)
#print(CORREARRAY)



#######################################
# ########################                Running Mean           ###########################################################

def runningmean(value, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(value, weights, 'valid')
    return smas


B=[]
Run=[]
run = []
j=1




while j < len(SLOPEARRAY):


    run = runningmean(SLOPEARRAY[j],9)

    Run.append(run)

    j = j + 1

print(Run)
B=np.arange(2,len(run)/2+2,0.5)
print(B)

nsteps =13
K=np.arange(0,12,3)
cmap = mpl.cm.gist_rainbow

for k in K:
    #while i < len(CORREARRAY):
    fig = plt.figure(1)
    plt.plot(Run[k], B, '.-', label='2009'+str(k),color=cmap(k / float(nsteps)))
    plt.plot(Run[k+1], B, '+-', label='2009'+str(k+1),color=cmap(k / float(nsteps)))
    plt.plot(Run[k+2], B, '^-', label='2009'+str(k+2),color=cmap(k / float(nsteps)))

    k = k + 1





y = [ 1.5,2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5,9,9.5,10,10.5,11]


plt.xlabel('Value of slopes (°)')
plt.ylabel('Averaged height (km)')
plt.title('Moving average of slopes for different heights and months')
plt.xlim(left=0)
plt.yticks(np.arange(0, max(y)+1))
plt.grid(b=None, which='both', axis='both')
plt.minorticks_on()
plt.legend()

txt= Site+' '+Year
fig.text(.8,.01, txt, ha='center')




plt.show()


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


 #output_dir = r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\plots\Wilberforce\Moving Averages2\Slopes\2010'
mkdir_p(output_dir)

fig.savefig('{}/Seas-S-Eureka-2009.png'.format(output_dir))
