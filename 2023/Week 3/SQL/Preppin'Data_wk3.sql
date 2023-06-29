USE PREPPIN_Data

Select A.OnlineInPerson, A.Qtr, A.Val, B.Quarterly_Target, (A.Val - B.Quarterly_Target) as "Variance_from_target"
from 
(Select OnlineInPerson, Qtr, sum(Value) as "Val"  #Input table 1
from
(SELECT *, CASE Online_or_InPerson when "1" then "Online" when "2" then "In-Person" end as "OnlineInPerson", 
Quarter(date(concat(right(left(Transaction_Date,10),4),"-",right(left(Transaction_Date,5),2), "-", left(transaction_date,2)))) as "Qtr"
FROM preppin_data.`pd 2023 wk3 input`
WHERE Transaction_Code LIKE "%DSB%") as Temp
GROUP BY OnlineInPerson, Qtr) as A

INNER JOIN 

(select *, Right(Category,1) as 'Quarter'  # Target Table
from
(SELECT t.Online_or_InPerson 
     , q.category       AS `Category`
     , CASE q.category 
       WHEN 'Q1'    THEN t.Q1 
       WHEN 'Q2'    THEN t.Q2
       WHEN 'Q3'  THEN t.Q3
       WHEN 'Q4'   THEN t.Q4
       END AS `Quarterly_Target` 
  FROM preppin_data.targets_2023wk3 t
 CROSS
  JOIN ( SELECT 'Q1'  AS category
         UNION ALL SELECT 'Q2'
         UNION ALL SELECT 'Q3'
         UNION ALL SELECT 'Q4'
       ) q
 ORDER
    BY t.Online_or_InPerson  
     , q.category='Q4'
     , q.category) as test) as B

ON A.OnlineInPerson = B.Online_or_InPerson and A.Qtr = B.Quarter
     