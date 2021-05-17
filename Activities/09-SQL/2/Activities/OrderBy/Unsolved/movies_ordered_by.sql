select * from actor;

-- select timezone((last_update)) from actor;

select count(first_name)
from actor;

-- select count of actors first names in descending order
select first_name, count(first_name) AS "nombres"
from actor
group by first_name
ORDER by "nombres" DESC;


select * from film;

-- select avg duration of movies by rating
select rating, round(avg(rental_duration),2) as "Avg duration"
from film
group by rating
ORDER by "Avg duration" DESC;


-- select top ten replace cost of movies by length of the movie
select length, round(avg(replacement_cost),2) as "Avg replacement cost"
from film
group by length
ORDER by "Avg replacement cost" DESC
limit 10;

-- select the count of countries
select * from city;
select * from country;

select country.country, count(country.country) AS "country count"
from city
join country on city.country_id = country.country_id
group by country.country
order by "country count" desc;

-- select country, count(country)
-- from country
-- where country_id in
-- (select country_id 
-- from city
-- where country_id);



