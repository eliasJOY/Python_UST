import pandas as pd
import numpy as np

fSeries = pd.Series(list("abcdefgh"))
print(fSeries)

country = pd.Series(np.array(['Luxenburg','Ireland','Singapore','Norway','Qatar','UAE']),
                 index=['a','b','c','d','e','f'])

print(country)

# collection of series : creating a dataframe using collection of series(dict)

GDP={'rich':pd.Series(np.array(['Luxenburg','Ireland','Singapore','Norway','Qatar','UAE'])),
 'GDP':pd.Series(np.array([1422,1342,1321,1221,1111,999]))}

df=pd.DataFrame(GDP)
print(df.head())
