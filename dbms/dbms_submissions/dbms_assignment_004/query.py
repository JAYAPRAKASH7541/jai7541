Q1="select count(id) from movie where year=2002 and name like 'ha%' and rank>2;"

Q2="select max(rank) from movie where name like 'autom%' and (year=1983 or year =1994);"

Q3="select count(id) from actor where gender='M' and (fname like '%ei' or lname like 'ei%');"

Q4="select avg(rank) as average_rank_of_movies from movie where year in (1993,1995,2000) and (rank >= 4.2);"

Q5="select sum(rank) from movie where name like '%hary%' and (year between 1981 and 1984) and (rank<9);"

Q6="select min(year) from movie where rank = 5 ;"

Q7="select count(id)  from actor  where (gender='F') or fname=lname;"

Q8="select  distinct fname from actor where lname like '%ei' order by fname asc limit 100;"

Q9="select id,name as movie_title,year from movie where year in(2001,2002,2005,2006) limit 25 offset 10;"

Q10="select distinct lname from director where fname in ('Yeud','Wolf','Vicky') order by lname limit 5;"
