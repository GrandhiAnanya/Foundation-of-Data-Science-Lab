import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# important features of SciPy
def objective(x):
    return x**2+10*np.sin(x)
    
result = minimize(objective,x0=0)
print("\n")
print("Optimized value using SciPy: ",result.x)

#important features of Pandas
#creating a data frame

data={
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New York','Los Angeles','Chicago'] 
}

df=pd.DataFrame(data)
print("\nDataFrame:")  
print(df)

#series
ages_series=pd.Series([25,30,35],name='Age')
print("\nSeries:")  
print(ages_series)

#reading an csv file
df.to_csv('sample.csv',index=False)
df_csv=pd.read_csv('sample.csv')
print("\nRead CSV:")  
print(df_csv)  

#reading a JSON file
df.to_json('sample.json',orient='records')
df_json=pd.read_json('sample.json',orient='records')
print("\nRead JSON:")  
print(df_json) 

#viewing the data
print("\nHead (first few rows):")  
print(df.head())  
print("\nTail (last few rows):")  
print(df.tail())  

#plotting
df.plot(kind='bar',x='Name',y='Age',rot=45)
plt.title('Age of Individuals')
plt.xlabel('Name')
plt.ylabel('Age')
plt.show()

#data cleaning
df.loc[1,'Age']=np.nan
df_cleaned=df.dropna()
print("\nData Cleaning:")  
print(df_cleaned) 

