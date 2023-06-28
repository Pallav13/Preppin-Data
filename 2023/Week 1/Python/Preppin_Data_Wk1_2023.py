import pandas as pd
import numpy as np
# Input the data (help)
path = "C:\\Users\\HP\\Desktop\\Preppin Data\\Preppi Data 2023\\Week 1\\Wk1InputSQL.csv"

df = pd.read_csv(path)

# Split the Transaction Code to extract the letters at the start of the transaction code. These identify the bank who processes the transaction (help)
# Rename the new field with the Bank code 'Bank'. 
df['Bank'] =  df['Transaction_Code'].str.split("-", expand=True)[0]

# Rename the values in the Online or In-person field, Online of the 1 values and In-Person for the 2 values. 
df['Online_or_In-Person'] = np.where(df['Online_or_In-Person'] == 1, 'Online', 'In-Person')

# Change the date to be the day of the week (help)
dWeek = pd.to_datetime(df['Transaction_Date'], format="%d-%m-%Y %H:%M")
# df['Day_of_Week'] = calender.day_name(dWeek)
df['Day_of_Week'] = dWeek.dt.day_name()
# Different levels of detail are required in the outputs. You will need to sum up the values of the transactions in three ways (help):
# 1. Total Values of Transactions by each bank
output1 = df.groupby('Bank', as_index=False)['Value'].sum()
# 2. Total Values by Bank, Day of the Week and Type of Transaction (Online or In-Person)
output2 = df.groupby(['Bank', 'Online_or_In-Person', 'Day_of_Week'], as_index=False)['Value'].sum()  
# 3. Total Values by Bank and Customer Code
output3 = df.groupby(['Bank', 'Customer Code'], as_index=False)['Value'].sum()
# Output each data file (help)

output1.to_csv("C:\\Users\\HP\\Desktop\\Preppin Data\\Preppi Data 2023\\Week 1\\py_output1.csv", index=False)
output2.to_csv("C:\\Users\\HP\\Desktop\\Preppin Data\\Preppi Data 2023\\Week 1\\py_output2.csv", index=False)
output3.to_csv("C:\\Users\\HP\\Desktop\\Preppin Data\\Preppi Data 2023\\Week 1\\py_output3.csv", index=False)
print('Data Prepped!')