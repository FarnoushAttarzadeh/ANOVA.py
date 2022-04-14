import pandas as pd
import numpy as np
import scipy as sci
from scipy.stats import f_oneway


################################################################# 2009 #################################################

dfNegro2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-2009-Negrocreek.csv')
dfNegro2009=dfNegro2009.drop(['Heights'],axis=1)
Negro2009=dfNegro2009.to_numpy()
Negro2009=Negro2009.flatten()
Negro2009= Negro2009[~np.isnan(Negro2009)]
Negro2009Len=len(Negro2009)
print(Negro2009,Negro2009Len)

dfWilber2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Wilberforce\MaxS-2009-Wilberforce.csv')
dfWilber2009=dfWilber2009.drop(['Heights'],axis=1)
Wilber2009=dfWilber2009.to_numpy()
Wilber2009=Wilber2009.flatten()
Wilber2009= Wilber2009[~np.isnan(Wilber2009)]
Wilber2009Len=len(Wilber2009)

print(Wilber2009,Wilber2009Len)


dfWal2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2009-Wal.csv')
dfWal2009=dfWal2009.drop(['Heights'],axis=1)
Wal2009=dfWal2009.to_numpy()
Wal2009=Wal2009.flatten()
Wal2009= Wal2009[~np.isnan(Wal2009)]
Wal2009Len=len(Wal2009)

print(Wal2009,Wal2009Len)



dfMcgill2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Mcgill\MaxS-2009-Mcgill.csv')
dfMcgill2009=dfMcgill2009.drop(['Heights'],axis=1)
Mcgill2009=dfMcgill2009.to_numpy()
Mcgill2009=Mcgill2009.flatten()
Mcgill2009= Mcgill2009[~np.isnan(Mcgill2009)]
Mcgill2009Len=len(Mcgill2009)

print(Mcgill2009,Mcgill2009Len)


dfHarrow2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Harrow\MaxS-2009-Harrow.csv')
dfHarrow2009=dfHarrow2009.drop(['Heights'],axis=1)
Harrow2009=dfHarrow2009.to_numpy()
Harrow2009=Harrow2009.flatten()
Harrow2009= Harrow2009[~np.isnan(Harrow2009)]
Harrow2009Len=len(Harrow2009)

print(Harrow2009,Harrow2009Len)


dfEur2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Eureka\MaxS-2009-Eur.csv')
dfEur2009=dfEur2009.drop(['Heights'],axis=1)
Eur2009=dfEur2009.to_numpy()
Eur2009=Eur2009.flatten()
Eur2009= Eur2009[~np.isnan(Eur2009)]
Eur2009Len=len(Eur2009)

print(Eur2009,Eur2009Len)


F2009 = f_oneway(Negro2009,Wilber2009,Wal2009,Mcgill2009,Harrow2009,Eur2009)
print(F2009)


###########################################       2010     #############################################################


dfNegro2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-2010-Negrocreek.csv')
dfNegro2010=dfNegro2010.drop(['Heights'],axis=1)
Negro2010=dfNegro2010.to_numpy()
Negro2010=Negro2010.flatten()
Negro2010= Negro2010[~np.isnan(Negro2010)]
Negro2010Len=len(Negro2010)
print(Negro2010,Negro2010Len)

dfWilber2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Wilberforce\MaxS-2010-Wilberforce.csv')
dfWilber2010=dfWilber2010.drop(['Heights'],axis=1)
Wilber2010=dfWilber2010.to_numpy()
Wilber2010=Wilber2010.flatten()
Wilber2010= Wilber2010[~np.isnan(Wilber2010)]
Wilber2010Len=len(Wilber2010)

print(Wilber2010,Wilber2010Len)


dfWal2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2010-Wal.csv')
dfWal2010=dfWal2010.drop(['Heights'],axis=1)
Wal2010=dfWal2010.to_numpy()
Wal2010=Wal2010.flatten()
Wal2010= Wal2010[~np.isnan(Wal2010)]
Wal2010Len=len(Wal2010)

print(Wal2010,Wal2010Len)



dfMcgill2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Mcgill\MaxS-2010-Mcgill.csv')
dfMcgill2010=dfMcgill2010.drop(['Heights'],axis=1)
Mcgill2010=dfMcgill2010.to_numpy()
Mcgill2010=Mcgill2010.flatten()
Mcgill2010= Mcgill2010[~np.isnan(Mcgill2010)]
Mcgill2010Len=len(Mcgill2010)

print(Mcgill2010,Mcgill2010Len)


dfHarrow2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Harrow\MaxS-2010-Harrow.csv')
dfHarrow2010=dfHarrow2010.drop(['Heights'],axis=1)
Harrow2010=dfHarrow2010.to_numpy()
Harrow2010=Harrow2010.flatten()
Harrow2010= Harrow2010[~np.isnan(Harrow2010)]
Harrow2010Len=len(Harrow2010)

print(Harrow2010,Harrow2010Len)


dfEur2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Eureka\MaxS-2010-Eur.csv')
dfEur2010=dfEur2010.drop(['Heights'],axis=1)
Eur2010=dfEur2010.to_numpy()
Eur2010=Eur2010.flatten()
Eur2010= Eur2010[~np.isnan(Eur2010)]
Eur2010Len=len(Eur2010)

print(Eur2010,Eur2010Len)


F2010 = f_oneway(Negro2010,Wilber2010,Wal2010,Mcgill2010,Harrow2010,Eur2010)
print(F2010)

