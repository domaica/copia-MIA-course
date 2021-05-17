DELETE FROM CITIES;

SELECT * FROM CITIES;

INSERT INTO CITIES (city, state, population)
values ('Alameda', 'California', 79177),
('Mesa', 'Arizona', 496401),
('Boerne', 'Texas', 16056),
('Anaheim', 'California', 352497),
('Tucson', 'Arizona', 535677),
('Garland', 'Texas', 238002);

SELECT city FROM CITIES;

--Filter to see cities only in Arizona

SELECT city, state FROM CITIES
WHERE state = 'Arizona';

SELECT * FROM CITIES
WHERE population < 100000;

SELECT * FROM CITIES
WHERE population < 100000
and state = 'California';

