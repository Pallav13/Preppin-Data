import pandas as pd
import numpy as np

# Input the data
path1 = "C:\\Users\\HP\\Desktop\\Preppin'Data\\2023\\Week 3\\PD 2023 Wk 1 Input.csv"

df1 = pd.read_csv(path1)

path2 = "C:\\Users\\HP\\Desktop\\Preppin'Data\\2023\\Week 3\\Targets.csv"

df2 = pd. read_csv(path2)


# For the transactions file:

# Filter the transactions to just look at DSB (help)
# These will be transactions that contain DSB in the Transaction Code field
df1['Bank'] = df1['Transaction Code'].str.split(pat= "-", expand=True)[0]
df1 = df1.loc[df1['Bank'] == 'DSB']

# Rename the values in the Online or In-person field, Online of the 1 values and In-Person for the 2 values
df1['Transaction Type'] = np.where(df1['Online or In-Person'] == 1, 'Online', 'In-Person')

# Change the date to be the quarter (help)
X = pd.to_datetime(df1['Transaction Date'], format="%d/%m/%Y %H:%M:%S")
df1['Quarter'] = pd.to_numeric(X.dt.quarter)

# Sum the transaction values for each quarter and for each Type of Transaction (Online or In-Person) (help)
transactions = df1.groupby(['Quarter', 'Transaction Type'], as_index=False)['Value'].sum()

# For the targets file:
# Pivot the quarterly targets so we have a row for each Type of Transaction and each Quarter (help)
#  Rename the fields
targets = pd.melt(df2, id_vars=['Online or In-Person'], value_vars=['Q1', 'Q2', 'Q3', 'Q4'], var_name= 'Quarter', value_name='Quarterly Targets')

# Remove the 'Q' from the quarter field and make the data type numeric (help)

targets['Quarter'] = pd.to_numeric( targets['Quarter'].str.replace("Q", ""))


# Join the two datasets together (help)
# You may need more than one join clause!
# Remove unnecessary fields
joined = pd.merge(transactions, targets, how='inner', left_on=['Quarter', 'Transaction Type'], right_on=['Quarter', 'Online or In-Person'] )

# Calculate the Variance to Target for each row (help)
joined['Variance from Target'] = joined['Value'] - joined['Quarterly Targets']


# Output the data
joined.to_csv("C:\\Users\\HP\\Desktop\\Preppin'Data\\2023\\Week 3\\Python\\Output.csv", index=False)

print("data prepped!")