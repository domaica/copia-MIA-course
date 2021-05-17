create table premise_table (
id int primary key,
premise_name text,
county_id text
);

create table county_table (
id int primary key,
county_name text,
license_count int,
county_id text
);