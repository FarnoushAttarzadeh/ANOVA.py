import pandas as pd
import numpy as np
import scipy as sci
from scipy import stats

dfNegro2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-2009-Negrocreek.csv')
dfNegro2009=dfNegro2009.drop(['Heights'],axis=1)
Negro2009=dfNegro2009.to_numpy()
Negro2009=Negro2009.flatten()
Negro2009= Negro2009[~np.isnan(Negro2009)]
Negro2009=Negro2009.flatten()
Negro2009=Negro2009.tolist()
Negro2009Len=len(Negro2009)
#print(Negro2009,Negro2009Len)

dfWilber2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Wilberforce\MaxS-2009-Wilberforce.csv')
dfWilber2009=dfWilber2009.drop(['Heights'],axis=1)
Wilber2009=dfWilber2009.to_numpy()
Wilber2009=Wilber2009.flatten()
Wilber2009= Wilber2009[~np.isnan(Wilber2009)]
Wilber2009=Wilber2009.flatten()
Wilber2009=Wilber2009.tolist()
Wilber2009Len=len(Wilber2009)
print(Wilber2009Len)


t_testWilNeg= stats.ttest_ind(Wilber2009,Negro2009)
print(t_testWilNeg)






dfWal2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2009-Wal.csv')
dfWal2009=dfWal2009.drop(['Heights'],axis=1)
Wal2009=dfWal2009.to_numpy()
Wal2009=Wal2009.flatten()
Wal2009= Wal2009[~np.isnan(Wal2009)]
Wal2009=Wal2009.flatten()
Wal2009=Wal2009.tolist()
Wal2009Len=len(Wal2009)

#print(Wal2009,Wal2009Len)


dfHarrow2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Harrow\MaxS-2009-Harrow.csv')
dfHarrow2009=dfHarrow2009.drop(['Heights'],axis=1)
Harrow2009=dfHarrow2009.to_numpy()
Harrow2009=Harrow2009.flatten()
Harrow2009= Harrow2009[~np.isnan(Harrow2009)]
Harrow2009=Harrow2009.flatten()
Harrow2009=Harrow2009.tolist()
Harrow2009Len=len(Harrow2009)

#print(Harrow2009,Harrow2009Len)


t_testWalHar= stats.ttest_ind(Harrow2009,Wal2009)
print(t_testWalHar)





NegWil=Wilber2009+Negro2009
HarWil=Harrow2009+Negro2009


t_test= stats.ttest_ind(HarWil,NegWil)
print(t_test)



##########################################           2010                        #####################################


dfNegro2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-2010-Negrocreek.csv')
dfNegro2010=dfNegro2010.drop(['Heights'],axis=1)
Negro2010=dfNegro2010.to_numpy()
Negro2010=Negro2010.flatten()
Negro2010= Negro2010[~np.isnan(Negro2010)]
Negro2010=Negro2010.tolist()
Negro2010Len=len(Negro2010)
#print(Negro2010,Negro2010Len)






dfWilber2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Wilberforce\MaxS-2010-Wilberforce.csv')
dfWilber2010=dfWilber2010.drop(['Heights'],axis=1)
Wilber2010=dfWilber2010.to_numpy()
Wilber2010=Wilber2010.flatten()
Wilber2010= Wilber2010[~np.isnan(Wilber2010)]
Wilber2010=Wilber2010.tolist()
Wilber2010Len=len(Wilber2010)

#print(Wilber2010,Wilber2010Len)










dfWal2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2010-Wal.csv')
dfWal2010=dfWal2010.drop(['Heights'],axis=1)
Wal2010=dfWal2010.to_numpy()
Wal2010=Wal2010.flatten()
Wal2010= Wal2010[~np.isnan(Wal2010)]
Wal2010Len=len(Wal2010)








dfHarrow2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Harrow\MaxS-2010-Harrow.csv')
dfHarrow2010=dfHarrow2010.drop(['Heights'],axis=1)
Harrow2010=dfHarrow2010.to_numpy()
Harrow2010=Harrow2010.flatten()
Harrow2010= Harrow2010[~np.isnan(Harrow2010)]
Harrow2010=Harrow2010.tolist()
Harrow2010Len=len(Harrow2010)



NegWil2=Wilber2010+Negro2010
HarWil2=Harrow2010+Negro2010


t_test2= stats.ttest_ind(HarWil2,NegWil2)
print(t_test2)





