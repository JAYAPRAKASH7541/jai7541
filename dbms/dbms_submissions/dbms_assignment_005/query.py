Q1="select pid as actor_id,count(mid) as no_of_movies  from cast group by (pid);"

Q2="select year,count(id) from movie group by year order by year;"

Q3="select year,avg(rank) as avg_rank from movie group by year  having count(id)>10 order by year desc;"

Q4="select year,max(rank) as max_rank from movie group by year order by year asc;"

Q5="select rank,count(id) as no_of_movies from movie where name like 'a%' group by rank;"

