DROP TABLE programming_languages;

CREATE TABLE programming_languages(
	id SERIAL PRIMARY KEY,
	language VARCHAR(20) not null,
	rating INT	
);

INSERT INTO programming_languages (language, rating)
VALUES ('HTML', 95),
		('JS', 99),
		('JQuery', 98),
		('MySQL', 70),
		('MySQL', 70);
		
select id, language, rating from programming_languages
where language = 'MySQL';

delete from programming_languages where id = 5

update programming_languages
set language 

select * from programming_languages; 

