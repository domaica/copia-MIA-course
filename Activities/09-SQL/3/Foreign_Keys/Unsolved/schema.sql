-- 1. Create a Customer table
create table customer (
cust_id serial primary key,
	first_name varchar,
	last_name varchar
);

select * from customer;

-- drop table customer;

-- 2. Populate that table
-- 'Bob Smith', 'Jane Davidson', 'Jimmy Bell', and 'Stephanie Duke'

INSERT INTO customer VALUES
(1,'Bob','Smith'),
(2,'Jane','Davidson'),
(3,'Jimmy','Bell'),
(4,'Stephanie','Duke')
;

-- 3. View Table

-- 4.. Create Customer Email table
create table customer_email (
cust_id serial primary key,
	cust_email varchar
);

select * from customer_email;


-- 5. Populate the second table
-- 'bobsmith@email.com', 'jdavids@email.com', 'jimmyb@email.com', 'sd@email.com'
INSERT INTO customer_email VALUES
(1,'bobsmith@email.com'),
(2,'jdavids@email.com'),
(3,'jimmyb@email.com'),
(4,'sd@email.com')
;



-- 6. View Table



-- 7. Creater Customer Phone Number table
create table customer_phone (
cust_id serial primary key,
	cust_phone varchar
);

select * from customer_phone;


-- 8. Populate Third Table
-- '435-344-2245', '332-776-4678', '221-634-7753', '445-663-5799'
INSERT INTO customer_phone VALUES
(1,'435-344-2245'),
(2,'332-776-4678'),
(3,'221-634-7753'),
(4,'445-663-5799')
;
-- 9. View Table
