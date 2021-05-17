select * from film;

-- 1. What is the average cost to rent a film in the stores?
-- select avg(rental_rate) as "Average rental rate"
select round(avg(rental_rate),2) as "Average rental rate"
from film;

-- 2. What is the average rental cost of films by rating? 
-- On average, what is the cheapest rating of films to rent? Most expensive?
select rating, avg(rental_rate) as "Average rental rate"
from film
group by rating;

-- 3. How much would it cost to replace all the films in the database?
select sum(replacement_cost) as "Total replacement cost"
from film;

-- 4. How much would it cost to replace all the films in each ratings category?
select rating, sum(replacement_cost) as "Total replacement cost"
from film
group by rating
order by "Total replacement cost" desc
LIMIT 3;

-- 5. How long is the longest movie in the database? The shortest?
select min (length), max(length)
from film;
