import pandas as pd
import numpy as np

# Input the data
path1 = "C:\\Users\\HP\\Desktop\\Preppin Data\\Preppi Data 2023\\Week 2\\Transactions.csv"
path2 = "C:\\Users\\HP\\Desktop\\Preppin Data\\Preppi Data 2023\\Week 2\\Swift Codes.csv"

df1 = pd.read_csv(path1)

df2 = pd.read_csv(path2)


# In the Transactions table, there is a Sort Code field which contains dashes. We need to remove these so just have a 6 digit string (hint)
df1["Sort Code"] = df1['Sort Code'].str.replace("-","")

# Use the SWIFT Bank Code lookup table to bring in additional information about the SWIFT code and Check Digits of the receiving bank account (hint)
join_df = pd.merge(df1,df2, how="inner", on=['Bank', 'Bank'])

# Add a field for the Country Code (hint)
# Hint: all these transactions take place in the UK so the Country Code should be GB
join_df['Country Code'] = 'GB'

# Create the IBAN as above (hint)
# Hint: watch out for trying to combine sting fields with numeric fields - check data types
join_df['IBAN'] = join_df['Country Code'].astype(str) + join_df['Check Digits'].astype(str) + join_df['SWIFT code'].astype(str) + join_df['Sort Code'].astype(str) + join_df['Account Number'].astype(str)

# Remove unnecessary fields (hint)
output = join_df[['Transaction ID', 'IBAN']]
print(output)
# Output the data

output.to_csv("C:\\Users\\HP\\Desktop\\Preppin Data\\Preppi Data 2023\\Week 2\\py_output.csv", index=False)
