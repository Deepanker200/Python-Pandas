import pandas as pd

data={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,None,50]
}

df=pd.DataFrame(data)
print("Before Interpolation")
print(df)

print("After Interpolation")
df['Value']=df["Value"].interpolate(method="linear")
print(df)

"""
1- Time Series Data
2- Numeric Data with Trends
3- Avoid Dropping Rows
"""