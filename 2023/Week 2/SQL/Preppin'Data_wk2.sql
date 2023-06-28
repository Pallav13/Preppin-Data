USE PREPPIN_DATA

/*
In the Transactions table, there is a Sort Code field which contains dashes. We need to remove these so just have a 6 digit string
Use the SWIFT Bank Code lookup table to bring in additional information about the SWIFT code and Check Digits of the receiving bank account
Add a field for the Country Code 
Hint: all these transactions take place in the UK so the Country Code should be GB
Create the IBAN as above 
Hint: watch out for trying to combine sting fields with numeric fields - check data types
Remove unnecessary field
*/

# Output

SELECT Transaction_ID, 
Concat("GB",Check_Digits,SWIFT_code,CONCAT(Left(Sort_Code,2),Right(Left(Sort_Code,5),2),Right(Sort_Code,2)), Account_Number) as "IBAN"
FROM preppin_data.transactions_2023wk2 as A
INNER JOIN preppin_data.`swift codes_2023wk2` as B
ON A.Bank = B.Bank;