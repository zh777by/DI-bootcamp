-- ex_xp+

create table students (
    id int primary key,
    first_name varchar(255),
    last_name varchar(255),
    birth_date date
);

drop table students
select * from students

insert into students (id, first_name, last_name, birth_date)
values
    (1, 'Marc', 'Benichou', '1998-11-02'),
    (2, 'Yoan', 'Cohen', '2010-12-03'),
    (3, 'Lea', 'Benichou', '1987-07-27'),
    (4, 'Amelia', 'Dux', '1996-04-07'),
    (5, 'David', 'Grez', '2003-06-14'),
    (6, 'Omer', 'Simpson', '1980-10-03');
	
insert into students (id, first_name, last_name, birth_date) values (7, 'Evgenii', 'Byalo', '1977-07-06')

select first_name, last_name from students
select * from students where id = 2
select first_name, last_name from students where last_name = 'Benichou' and first_name = 'Marc'
select first_name, last_name from students where last_name = 'Benichou' or first_name = 'Marc'
select * from students where first_name like '%a%'
select * from students where first_name like 'a%'
select * from students where first_name like '%a'
select * from students where first_name like '_a%a'
select * from students where id in (1, 3)


-- ex_g
select * from students
order by last_name
limit 4

select * from students
order by birth_date desc
limit 1;












