select * from address;

select * from customer;

select * from city;
-- question 1
select city_id, city from city
where city = 'Qalyub'
OR city = 'Qinhuangdao'
OR city = 'Qomsheh'
OR city = 'Quilmes';

select city_id, city from city
where city in ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes');
-- question 2  ---
select district from address
where city_id IN
(
select city_id from city
where city = 'Qalyub'
OR city = 'Qinhuangdao'
OR city = 'Qomsheh'
OR city = 'Quilmes'	
);


select district 
from address
where city_id IN 
(
select city_id from city
where city in ('Qalyub', 'Qinhuangdao', 'Qomsheh', 'Quilmes')
);

-- Bonus Using subqueries, find the first and last names 
-- of customers who reside in cities that begin with the letter Q.

select * from customer;

select city_id from city
where city 
like 'Q%';

select first_name, last_name 
from customer cus
where address_id IN
(
select address_id 
from address a
where city_id IN 
(
select city_id from city
where city 
like 'Q%')
);


