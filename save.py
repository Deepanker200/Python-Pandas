import pandas as pd

data={
    "Name":['Ram','Shyam','Ghanshyam'],
    "Age":[10,20,30],
    "City":['Nagpur','Mumbai','Delhi']
}

df=pd.DataFrame(data)
# print(df)

# For showing without index
# print(df.to_string(index=False))


# For saving a file in csv
# df.to_csv("output.csv",index=False)

# For saving a file in excel
# Install: pip install openpyxl
df.to_excel("output.xlsx",index=False)

# For saving a file in json
df.to_json("output.json",index=False)