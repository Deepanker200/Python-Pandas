import pandas as pd

data={
    "Name":['Ram','Lucky','Vansh','Pankaj','John','Rohan','Aman'],
    "Age":[25,25,34,45,67,23,44],
    "Salary":[50000,35000,40000,25000,60000,90000,55000],
    "Performance Score":[85,89,90,95,70,80,88]
}


df=pd.DataFrame(data)
print("Sample DataFrame")
print(df)
print("Names (Single column return series)")
name=df["Name"]
print(name)

#selecting multiple columns
subset=df[["Name","Salary"]]
print("Subset with Name and Salary")
print(subset)