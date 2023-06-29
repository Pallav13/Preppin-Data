USE Preppin_data;

select * from targets;

select X.Quarter, X.Transaction_Type, X.Value, T1.QuarterlyTargets, X.Value - T1.QuarterlyTargets as "Variance_from_Target"from
(select test.Quarter, test.Transaction_Type, sum(test.Value) as "Value" from
(select *
from 
(select *, 
case
when pd2023_wk1_input.Online_or_In_Person = 1 then 'Online'
else 'In-Person'
end as "Transaction_Type",
substring_index(Transaction_Code, "-",1) as 'Bank',
quarter(str_to_date(Transaction_Date,"%d-%m-%Y %T")) as 'Quarter'
from pd2023_wk1_input

) as trans
WHERE Bank = 'DSB') test
group by test.Quarter, test.Transaction_Type) as X
inner join 
(select targets.Online_or_In_Person, 1 as 'Quarter', Q1 as 'QuarterlyTargets'
from targets
union all
select targets.Online_or_In_Person, 2 as 'Quarter', Q2 as 'QuarterlyTargets'
from targets
union all
select targets.Online_or_In_Person, 3 as 'Quarter', Q3 as 'QuarterlyTargets'
from targets
union all
select targets.Online_or_In_Person, 4 as 'Quarter', Q4 as 'QuarterlyTargets'
from targets) as T1

ON X.Transaction_Type = T1.Online_or_In_Person AND X.Quarter = T1.Quarter
;