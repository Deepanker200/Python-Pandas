#step-1 sample data frame

import pandas as pd

data={
    "Name":['Ram','Lucky','Vansh','Pankaj','John','Rohan','Aman'],
    "Age":[25,25,34,45,67,23,44],
    "Salary":[50000,35000,40000,25000,60000,90000,55000],
    "Performance Score":[85,89,90,95,70,80,88]
}

df=pd.DataFrame(data)
print("Sample Dataframe")
print(df)
print("Descriptive Stastics")
print(df.describe())