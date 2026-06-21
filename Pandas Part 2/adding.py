#adding columns

import pandas as pd

data={
    "Name":['Ram','Lucky','Vansh','Pankaj','John','Rohan','Aman'],
    "Age":[25,25,34,45,67,23,44],
    "Salary":[50000,35000,40000,25000,60000,90000,55000],
    "Performance Score":[85,89,90,95,70,80,88]
}

df=pd.DataFrame(data)
print(df)

#square brackets df["Column_Name"]=some_Data
df["Bonus"]=df["Salary"]*0.1
print("After..........")
print(df)

#using insert
df.insert(0,"Emp ID",[101,102,103,104,105,106,107])
print("Inserting......")
print(df)
# print(df.to_csv("part2.csv",index=False))