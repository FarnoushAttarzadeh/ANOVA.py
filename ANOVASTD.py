import pandas as pd
import numpy as np
import scipy as sci
from scipy.stats import f_oneway


###############################    ANOVA for STDs  2009   over heights           #######################################

dfNegro2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-2009-Negrocreek.csv')
dfNegro2009=dfNegro2009.drop(['Heights'],axis=1)
Negro2009Std=np.array(dfNegro2009.std(axis = 1, skipna = True))
print(Negro2009Std)



dfWilber2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Wilberforce\MaxS-2009-Wilberforce.csv')
dfWilber2009=dfWilber2009.drop(['Heights'],axis=1)
Wilber2009Std=np.array(dfWilber2009.std(axis = 1, skipna = True))
print(Wilber2009Std)

dfWal2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2009-Wal.csv')
dfWal2009=dfWal2009.drop(['Heights'],axis=1)
Wal2009Std=np.array(dfWal2009.std(axis = 1, skipna = True))
print(Wal2009Std)


dfMcgill2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Mcgill\MaxS-2009-Mcgill.csv')
dfMcgill2009=dfMcgill2009.drop(['Heights'],axis=1)
Mcgill2009Std=np.array(dfMcgill2009.std(axis = 1, skipna = True))
print(Mcgill2009Std)

dfHarrow2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Harrow\MaxS-2009-Harrow.csv')
dfHarrow2009=dfHarrow2009.drop(['Heights'],axis=1)
Harrow2009Std=np.array(dfHarrow2009.std(axis = 1, skipna = True))
print(Harrow2009Std)

dfEur2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Eureka\MaxS-2009-Eur.csv')
dfEur2009=dfEur2009.drop(['Heights'],axis=1)
Eur2009Std=np.array(dfEur2009.std(axis = 1, skipna = True))
print(Eur2009Std)

FStd2009H = f_oneway(Negro2009Std,Wilber2009Std,Wal2009Std,Mcgill2009Std,Harrow2009Std,Eur2009Std)
print(FStd2009H)


#################################               ANOVA for STD 2010   over heights                  #####################



dfNegro2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-2010-Negrocreek.csv')
dfNegro2010=dfNegro2010.drop(['Heights'],axis=1)
Negro2010Std=np.array(dfNegro2010.std(axis = 1, skipna = True))
print(Negro2010Std)



dfWilber2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Wilberforce\MaxS-2010-Wilberforce.csv')
dfWilber2010=dfWilber2010.drop(['Heights'],axis=1)
Wilber2010Std=np.array(dfWilber2010.std(axis = 1, skipna = True))
print(Wilber2010Std)

dfWal2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2010-Wal.csv')
dfWal2010=dfWal2010.drop(['Heights'],axis=1)
Wal2010Std=np.array(dfWal2010.std(axis = 1, skipna = True))
print(Wal2010Std)


dfMcgill2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Mcgill\MaxS-2010-Mcgill.csv')
dfMcgill2010=dfMcgill2010.drop(['Heights'],axis=1)
Mcgill2010Std=np.array(dfMcgill2010.std(axis = 1, skipna = True))
print(Mcgill2010Std)

dfHarrow2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Harrow\MaxS-2010-Harrow.csv')
dfHarrow2010=dfHarrow2010.drop(['Heights'],axis=1)
Harrow2010Std=np.array(dfHarrow2010.std(axis = 1, skipna = True))
print(Harrow2010Std)

dfEur2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Eureka\MaxS-2010-Eur.csv')
dfEur2010=dfEur2010.drop(['Heights'],axis=1)
Eur2010Std=np.array(dfEur2010.std(axis = 1, skipna = True))
print(Eur2010Std)

FStd2010H = f_oneway(Negro2010Std,Wilber2010Std,Wal2010Std,Mcgill2010Std,Harrow2010Std,Eur2010Std)
print(FStd2010H)


#########################    ANOVA for STD over months 2009               ##############################################


dfNegro2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-2009-Negrocreek.csv')
dfNegro2009=dfNegro2009.drop(['Heights'],axis=1)
Negro2009Std=np.array(dfNegro2009.std(axis = 0, skipna = True))
Negro2009Std= Negro2009Std[~np.isnan(Negro2009Std)]
print(Negro2009Std)



dfWilber2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Wilberforce\MaxS-2009-Wilberforce.csv')
dfWilber2009=dfWilber2009.drop(['Heights'],axis=1)
Wilber2009Std=np.array(dfWilber2009.std(axis = 0, skipna = True))
Wilber2009Std= Wilber2009Std[~np.isnan(Wilber2009Std)]
print(Wilber2009Std)

dfWal2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2009-Wal.csv')
dfWal2009=dfWal2009.drop(['Heights'],axis=1)
Wal2009Std=np.array(dfWal2009.std(axis = 0, skipna = True))
Wal2009Std= Wal2009Std[~np.isnan(Wal2009Std)]
print(Wal2009Std)


dfMcgill2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Mcgill\MaxS-2009-Mcgill.csv')
dfMcgill2009=dfMcgill2009.drop(['Heights'],axis=1)
Mcgill2009Std=np.array(dfMcgill2009.std(axis = 0, skipna = True))
Mcgill2009Std= Mcgill2009Std[~np.isnan(Mcgill2009Std)]
print(Mcgill2009Std)


dfHarrow2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Harrow\MaxS-2009-Harrow.csv')
dfHarrow2009=dfHarrow2009.drop(['Heights'],axis=1)
Harrow2009Std=np.array(dfHarrow2009.std(axis = 0, skipna = True))
Harrow2009Std= Harrow2009Std[~np.isnan(Harrow2009Std)]
print(Harrow2009Std)

dfEur2009 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Eureka\MaxS-2009-Eur.csv')
dfEur2009=dfEur2009.drop(['Heights'],axis=1)
Eur2009Std=np.array(dfEur2009.std(axis = 0, skipna = True))
Eur2009Std= Eur2009Std[~np.isnan(Eur2009Std)]
print(Eur2009Std)

FStd2009M = f_oneway(Negro2009Std,Wilber2009Std,Wal2009Std,Mcgill2009Std,Harrow2009Std,Eur2009Std)
print(FStd2009M)

#################################               ANOVA for STD 2010   over heights                  #####################



dfNegro2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Negrocreek\MaxS-2010-Negrocreek.csv')
dfNegro2010=dfNegro2010.drop(['Heights'],axis=1)
Negro2010Std=np.array(dfNegro2010.std(axis = 0, skipna = True))
Negro2010Std= Negro2010Std[~np.isnan(Negro2010Std)]
print(Negro2010Std)



dfWilber2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Wilberforce\MaxS-2010-Wilberforce.csv')
dfWilber2010=dfWilber2010.drop(['Heights'],axis=1)
Wilber2010Std=np.array(dfWilber2010.std(axis = 0, skipna = True))
Wilber2010Std= Wilber2010Std[~np.isnan(Wilber2010Std)]
print(Wilber2010Std)

dfWal2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Walsingham\MaxS-2010-Wal.csv')
dfWal2010=dfWal2010.drop(['Heights'],axis=1)
Wal2010Std=np.array(dfWal2010.std(axis = 0, skipna = True))
Wal2010Std= Wal2010Std[~np.isnan(Wal2010Std)]
print(Wal2010Std)


dfMcgill2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Mcgill\MaxS-2010-Mcgill.csv')
dfMcgill2010=dfMcgill2010.drop(['Heights'],axis=1)
Mcgill2010Std=np.array(dfMcgill2010.std(axis = 0, skipna = True))
Mcgill2010Std= Mcgill2010Std[~np.isnan(Mcgill2010Std)]
print(Mcgill2010Std)

dfHarrow2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Harrow\MaxS-2010-Harrow.csv')
dfHarrow2010=dfHarrow2010.drop(['Heights'],axis=1)
Harrow2010Std=np.array(dfHarrow2010.std(axis = 0, skipna = True))
Harrow2010Std= Harrow2010Std[~np.isnan(Harrow2010Std)]
print(Harrow2010Std)

dfEur2010 = pd.read_csv(r'C:\Users\Farnoush\Desktop\Data\LaCie\Maxes\Slopes\Eureka\MaxS-2010-Eur.csv')
dfEur2010=dfEur2010.drop(['Heights'],axis=1)
Eur2010Std=np.array(dfEur2010.std(axis = 0, skipna = True))
Eur2010Std= Eur2010Std[~np.isnan(Eur2010Std)]
print(Eur2010Std)

FStd2010M = f_oneway(Negro2010Std,Wilber2010Std,Wal2010Std,Mcgill2010Std,Harrow2010Std,Eur2010Std)
print(FStd2010M)