Q1="select fname,lname from actor INNER JOIN cast on id=pid where mid=12148;"

Q2="select count(mid) from cast Inner join actor on pid=id where fname='Harrison (I)' and lname='Ford';"

Q3="select distinct pid from cast Inner Join movie on id==mid where name like 'young latin girls%';"

Q4="select count(distinct pid) from cast Inner Join movie on id==mid where year between 1990 and 2000;"
'''
Count the number of movies in which actor “Harrison (I) Ford” acted
first name: “Harrison (I)”
last name: “Ford”

Get all the distinct actors ids who acted in all movie whose title starts with Young Latin Girls.


How many distinct actors have acted in any movie between 1990 and 2000 (both inclusive).
'''

