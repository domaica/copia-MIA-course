DROP TABLE IF EXISTS firepower;

-- Create new table to import data
CREATE TABLE firepower (
	country VARCHAR,
	ISO3 VARCHAR,
	rank INT,
	TotalPopulation INT,
	ManpowerAvailable INT,
	TotalMilitaryPersonnel INT,
	ActivePersonnel INT,
	ReservePersonnel INT,
	TotalAircraftStrength INT,
	FighterAircraft INT,
	AttackAircraft INT,
	TotalHelicopterStrength INT,
	AttackHelicopters INT
);

-- Import data from GlobalFirePower.csv
-- View the table to ensure all data has been imported correctly
delete from firepower
where ReservePersonnel = 0;


select * from firepower
where FighterAircraft = 1

UPDATE firepower 
SET TotalAircraftStrength = TotalAircraftStrength + 1
WHERE iso3 <> 'SRL';

SELECT AVG(column_name)
FROM table_name
WHERE condition;


SELECT * FROM firepower;