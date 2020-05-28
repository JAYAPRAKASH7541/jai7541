Q1="select * from Movie order by rank Desc limit 10;"

Q2="select * from Movie order by rank Desc limit 10 offset 10;"

Q3="select name from Movie where year > 2004;"

Q4="select name from Movie where rank < 1.1;"

Q5="select * from Movie where year in (2004,2005,2006);"

Q6="select name,year from Movie where name like 'harry%';"

Q7="select * from actor where fname=='Christin' and lname !='Watson';"

Q8="select * from actor where fname=='Woody' and lname =='Watson';"

Q9="select name from movie where year ==1990 and rank==5;"

Q10="select * from actor where fname ='Christin' and lname ='Watson';"

Q11="select name from movie where year between 2003 and 2005;"

Q12="select Distinct year from movie "

Q13="select * from actor where (fname ='Christin' or lname ='Watson') and (gender = 'M') order by fname limit 10 ;"

