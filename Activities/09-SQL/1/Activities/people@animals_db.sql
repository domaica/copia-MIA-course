CREATE TABLE people (
name VARCHAR(30) NOT NULL,
has_pet BOOLEAN DEFAULT false,
pet_type VARCHAR(10) NOT NULL,
pet_name VARCHAR(30),
pet_age INT);

insert into people (name, has_pet, pet_type, pet_name, pet_age)
values ('Jacob', true, 'dog', 'Misty', 10),
('Ahmed', true, 'rock', 'Rockington', 100),
('Peter', true, 'cat', 'Franklin', 2),
('Dave', true, 'dog', 'Queso, 1);

 insert into people (name, has_pet, pet_type, pet_name, pet_age)
values ('Jacinto', true, 'perro', 'Pastor', 9);

select pet_name from people;
 
select *
 from people
 where pet_type = 'dog'
 and pet_age > 5;
 
 select * from people;
 
 ALTER TABLE people ADD COLUMN ID SERIAL PRIMARY KEY;
 
 insert into people (name, has_pet, pet_type, pet_name, pet_age)
values ('Ahmed', true, 'rock', 'Rockington', 100);
 
 
  select * from people;
 
delete from people
where id = 6;

update people
set pet_type = 'donkey', pet_age = 8
where name = 'Ahmed';

-- reset primary key
select * from people
 order by id ASC;
 
 select * from people;
 
 
 
 
   select * from people;



