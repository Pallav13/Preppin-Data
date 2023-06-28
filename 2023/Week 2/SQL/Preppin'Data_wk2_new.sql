USE Preppin_data;

select * from transactions;

select * from swiftcodes;

SELECT t.TransactionID,
CONCAT("GB",s.CheckDigits,s.SWIFTcode,Replace(SortCode, "-", ""), t.AccountNumber ) as "IBAN"
from transactions t
inner join swiftcodes s
ON t.Bank = s.Bank;