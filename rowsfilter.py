import pandas as pd

data={
    "Name":['Ram','Lucky','Vansh','Pankaj','John','Rohan','Aman'],
    "Age":[25,25,34,45,67,23,44],
    "Salary":[50000,35000,40000,25000,60000,90000,55000],
    "Performance Score":[85,89,90,95,70,80,88]
}

df=pd.DataFrame(data)

high_salary=df[df['Salary']>50000]
print("Employees with salary 50k")
print(high_salary)

#filtering rows salary>50k and age >80

filtered=df[(df['Salary']>50000) & (df['Age']>30)]
print("Employees with salary 50k and age>80")
print(filtered)

#using or
filtered_or=df[(df['Salary']>50000) | (df['Performance Score']>90)]
print("Employees with salary 50k or performance score >90")
print(filtered_or)