drop table wordassociation;

create table wordassociation(
author int,
word1 varchar,
word2 varchar,
source varchar);

select * from wordassociation
where word1 = 'stone';

select * from wordassociation
where author >= 1
and author <= 10;

select * from wordassociation
where word1 = 'pie'
or word2 = 'pie';

select * from wordassociation
where source = 'BC';

select * from wordassociation
where source = 'BC'
and author >= 333
and author <= 335;



select * from wordassociation;