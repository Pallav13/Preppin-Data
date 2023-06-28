CREATE DATABASE Preppin_Data

USE Preppin_Data

SELECT * from pd2023_wk1_input;


# OUTPUT 1
with CTE as (select *,substring_index(Transaction_Code, "-", 1) as "Bank", 
CASE 
When Online_or_In_Person = 1 then 'Online'
Else 'In-Person' end as "Transaction Type",
DAYNAME(str_to_date(Transaction_Date, "%d-%m-%Y %T")) as "Day_of_Week"
from pd2023_wk1_input)
SELECT Bank, sum(CTE.Value) as "Value"
from CTE
GROUP BY BANK;


# OUTPUT 2

WITH CTE as (SELECT *, substring_index(Transaction_Code, "-", 1) as "Bank",
CASE
WHEN Online_or_In_Person = 1 then "Online"
else "In-Person"
end as "Transaction_Type",
dayname(str_to_date(Transaction_Date, "%d-%m-%Y %T")) as "Day_of_Week"
from pd2023_wk1_input)
SELECT BANK, Online_or_In_Person, Day_of_Week, sum(Value) as "Value"
from CTE
GROUP BY BANK, Online_or_In_Person, Day_of_Week;


# Output 3
WITH CTE as (SELECT *, substring_index(Transaction_Code, "-", 1) as "Bank",
CASE
WHEN Online_or_In_Person = 1 then "Online"
else "In-Person"
end as "Transaction_Type",
dayname(str_to_date(Transaction_Date, "%d-%m-%Y %T")) as "Day_of_Week"
from pd2023_wk1_input)
SELECT Bank, Customer_Code, sum(value) as "Value"
from CTE
group by Bank, Customer_Code