import pandas as pd
import numpy as np
import scipy as sci
from scipy.stats import f_oneway


###############################    ANOVA for STDs  for Walsingham    over heights           #######################################

dfWal2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2009-Wal.csv')
dfWal2009=dfWal2009.drop(['Heights'],axis=1)
Wal2009Std=np.array(dfWal2009.std(axis = 1, skipna = True))
print(Wal2009Std)

dfWal2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2010-Wal.csv')
dfWal2010=dfWal2010.drop(['Heights'],axis=1)
Wal2010Std=np.array(dfWal2010.std(axis = 1, skipna = True))
print(Wal2010Std)

dfWal2011 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2011-Wal.csv')
dfWal2011=dfWal2011.drop(['Heights'],axis=1)
Wal2011Std=np.array(dfWal2011.std(axis = 1, skipna = True))
print(Wal2011Std)

dfWal2012 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2012-Wal.csv')
dfWal2012=dfWal2012.drop(['Heights'],axis=1)
Wal2012Std=np.array(dfWal2012.std(axis = 1, skipna = True))
print(Wal2012Std,len(Wal2012Std,))


FWal2009 = f_oneway(Wal2009Std,Wal2010Std,Wal2011Std,Wal2012Std)
print(FWal2009)