# Q1='''select d.id,d.fname from director as d,movie as m,moviedirector as md 
# where exists(select * from movie where md.mid=m.id and md.did = d.id and m.year>2000)
# and not exists(select * from movie where md.mid=m.id and md.did=d.id and m.year<2000)
# order by d.id asc;'''

Q2='''select d1.fname,(select m.name from movie as m inner join moviedirector as md
on md.mid=m.id inner join director as d on d.id=md.did where d.id =d1.id 
order by m.rank desc limit 1) as name from director as d1 limit 100;'''

Q3='''select * from actor as a where (select m.id from movie inner join cast as c on c.mid = m.id 
where m.year  not in between 1990 and 2000) order by a.id desc limit 100;'''