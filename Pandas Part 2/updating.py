#updating columns

import pandas as pd

data={
    "Name":['Ram','Lucky','Vansh','Pankaj','John','Rohan','Aman'],
    "Age":[25,25,34,45,67,23,44],
    "Salary":[50000,35000,40000,25000,60000,90000,55000],
    "Performance Score":[85,89,90,95,70,80,88]
}

df=pd.DataFrame(data)
# print(df)

#. loc[]
# df.loc[row_index,"Column Name"]=new_value
# df.loc[0,'Salary']=55000

#increasing salary of all by 5%
df['Salary']=df['Salary']*1.05
print(df)