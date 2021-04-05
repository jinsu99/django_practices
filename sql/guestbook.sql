-- scheme
desc guestbook; 

-- insert
insert into guestbook values(null, '동해물', '1234', '안녕하세요', now());

-- select
select 	no, 
		name, 
		message, date_format(reg_date, '%Y-%m-%d %p %h:%i:%s') as reg_date 
	from guestbook 
    order by reg_date desc;
select * from guestbook;

-- delete
delete from guestbook where no = 4 and password='1231';


