CREATE TABLE films (
	film_id serial primary key,
title VARCHAR,
description VARCHAR,
release_year INT,
language_id INT,
original_language_id INT,
rental_duration INT,
rental_rate float(2),
lenght INT,
replacement_cost float(2),
rating VARCHAR,
last_update SQL,
special_features VARCHAR,
fulltext VARCHAR);

select * from films;


-- 1. What is the average cost to rent a film in the stores?


-- 2. What is the average rental cost of films by rating? On average, what is the cheapest rating of films to rent? Most expensive?


-- 3. How much would it cost to replace all the films in the database?


-- 4. How much would it cost to replace all the films in each ratings category?


-- 5. How long is the longest movie in the database? The shortest?
