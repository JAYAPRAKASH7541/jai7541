Q1="select avg(age) from player;"

Q2='''select match_no,play_date from match
	where audience>50000 order by match_no asc;'''

Q3='''select team_id,count(win_lose) as l from MatchTeamDetails 
	group by team_id,win_lose having win_lose == 'W'
	order by l desc,team_id asc;'''

Q4=''' select match_no,play_date from match where stop1_sec > 
	(select avg(stop1_sec) from match) 
	order by match_no desc;'''

Q5='''select mc.match_no,t.name,p.name from team as t inner join matchcaptain as mc on t.team_id=mc.team_id inner join player as p on p.team_id=mc.team_id where mc.captain = p.player_id order by mc.match_no asc ,t.name asc;'''

Q6='''select m.match_no,p.name,p.jersey_no from match as m inner join player as p on m.player_of_match=p.player_id order by m.match_no asc;''' 

Q7=''' select t.name,avg(p.age) as s from team as t inner join player as p 
	on p.team_id=t.team_id group by(t.team_id) having s>26 order by
	t.name asc;'''
	
Q8='''select p.name,p.jersey_no,p.age,count(goal_id) as c from player as p
	inner join goaldetails as gd on p.player_id=gd.player_id
	group by (p.player_id) having (p.age) <=27 
	order by c desc ,
	p.name asc;'''
	
	  

Q9='''select team_id,(count(goal_id)*100.0)/(select count(goal_id) from goaldetails) from goaldetails group by team_id;'''



Q10 = '''SELECT AVG(c) FROM (SELECT COUNT(goal_id) AS c FROM GoalDetails 
GROUP BY team_id);'''



Q11='''select player_id,name,date_of_birth from player as p where not exists 
(select p.player_id from goaldetails as gd where p.player_id=gd.player_id) order by p.player_id asc;'''

Q12='''
'''        