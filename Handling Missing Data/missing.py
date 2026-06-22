import pandas as pd

data={
    "Name":['Ram',None,'Vansh','Pankaj','John','Rohan','Aman'],
    "Age":[25,None,34,45,67,23,44],
    "Salary":[50000,None,40000,25000,60000,90000,55000],
    "Performance Score":[85,None,90,95,70,80,88]
}

df=pd.DataFrame(data)
print(df.isnull()) #gives False when data is not missing and gives True when data is missing
print(df.isnull().sum())