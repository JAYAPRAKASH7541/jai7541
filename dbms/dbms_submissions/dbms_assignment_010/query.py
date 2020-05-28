Q1='''select p.player_id,p.team_id,p.jersey_no,p.name,p.date_of_birth,
p.age from player as p inner join matchcaptain as mc
on p.player_id=mc.captain where captain not in 
(select player_id from goaldetails) order by match_no;

'''
Q2='''
select t.team_id,count(m.match_no) from matchteamdetails as m 
inner join team as t on t.team_id=m.team_id group by t.team_id; 
'''
Q3='''
select team_id,(count(goal_id)*1.0/
(select count(player_id) from player group by team_id)) as avg_goal_score
from goaldetails
group by team_id;
'''
Q4='''
select captain ,count(match_no) from matchcaptain group by captain;
'''
Q5='''
select count(distinct mc.captain) as no_players 
from match as m inner join matchcaptain as mc 
on mc.captain=m.player_of_match where m.match_no=mc.match_no;
'''
Q6='''
select distinct p.player_id as no_players from player as p
inner join matchcaptain as mc on p.player_id=mc.captain 
where captain not in (select player_of_match from match);
'''
Q7='''
select strftime('%m',play_date) as month,count(match_no) as no_of_matches 
from match group by month order by no_of_matches desc ;
'''

Q8='''
select p.jersey_no,count(mc.captain) as no_captains from player as p
inner join matchcaptain as mc on mc.captain=p.player_id group by p.jersey_no 
order by 
no_captains desc,p.jersey_no desc;
'''

Q9='''
select player_id,avg(audience) as avg_audience from match as m inner join
matchteamdetails as mtd on m.match_no=mtd.match_no inner join player
as p on p.team_id=mtd.team_id
group by p.player_id order by avg_audience desc,player_id desc;
'''

Q10='''select team_id,avg(age) from player group by team_id;'''

Q11='''
select avg(p.age) as avg_age_of_captains from player 
as p inner join matchcaptain
as mc on mc.captain=p.player_id;
'''

Q12='''
select strftime('%m',date_of_birth) as month ,count(player_id) as no_of_players
from player group by month
order by no_of_players desc,month desc;
'''
Q13='''
select 
'''
'''
# Task 13
Find the captain id and the number of matches he/she has won(no_of_wins). 
Your Query should return captain and no_of_wins in the descending order of no_of_wins.

# Sample Output Format
captain|no_of_wins
160140|5
160163|4
160322|4
160539|4
160062|3
.........

'''

 
 






