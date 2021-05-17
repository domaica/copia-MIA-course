select * from inventory;

select * from film;


select title,
(select count(inventory.film_id)
from inventory
where film.film_id = inventory.film_id)
as "number of copies"
from film;

-- CREATE VIEW
create view title_count as
select title,
(select count(inventory.film_id)
from inventory
where film.film_id = inventory.film_id)
as "number of copies"
from film;






SELECT title, "number of copies"
