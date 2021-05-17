  
DROP TABLE IF EXISTS toys;
DROP TABLE IF EXISTS games;

CREATE TABLE toys (
    toy_id SERIAL,
    type VARCHAR,
    name VARCHAR
);

CREATE TABLE games (
    game_id SERIAL,
    type VARCHAR,
    name VARCHAR
);

INSERT INTO toys (type, name)
VALUES
('sports', 'baseball'),
('adventure', 'staff'),
('sports', 'tennis ball'),
('fun', 'doll');

INSERT INTO games (type, name)
VALUES
('sports', 'tag'),
('adventure', 'Kings Quest'),
('sports', 'tennis'),
('fun', 'Make believe');


select * from games;


-- Two separte queries for toys and games
SELECT toy_id AS id, type
FROM toys;

SELECT game_id AS id, type
FROM games;

-- Union of toys and game types
SELECT toy_id AS id, type
FROM toys

UNION

SELECT game_id AS id, type
FROM games;

-- Include duplicate rows
SELECT toy_id AS id, type
FROM toys

UNION ALL

SELECT game_id AS id, type
FROM games;













-- Question 1

SELECT COUNT(*)
FROM city
UNION
SELECT COUNT(*)
FROM country;


-- Question 2

SELECT customer_id
FROM customer
WHERE address_id IN
(
  SELECT address_id
  FROM address
  WHERE city_id IN
  (
    SELECT city_id
    FROM city
    WHERE city = 'London'
  )
)
UNION ALL
SELECT id
FROM customer_list
WHERE city = 'London';


