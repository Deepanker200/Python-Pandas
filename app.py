import pandas as pd

#read data from csv file
# df= pd.read_csv("employees.csv",encoding="utf-8")

# read data from excel file
# df= pd.read_excel("SampleSuperstore.xlsx")

# read data from json file
df=pd.read_json("sample_Data.json")

print(df)

#gcsfs: For reading cloud platform data