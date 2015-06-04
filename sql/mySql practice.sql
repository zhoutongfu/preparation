# use mysql locally
#cd /usr/local/mysql
#sudo ./bin/mysqld_safe #start mysql server


# some tips: 
#  1. don't forget to add distinct when necessary



-- select
  SELECT population FROM world
  WHERE name = 'Germany';
-- /
  SELECT name, gdp/population from world
  WHERE area > 5000000;

-- and
  SELECT name , continent
  FROM world
  WHERE area < 2000
    AND gdp > 5000000000;
-- in
  SELECT name, population FROM world
  WHERE name IN ('Denmark', 'Finland',
                 'Norway','Sweden');

-- like
  SELECT name FROM world
  WHERE name LIKE 'G%'

-- between (inclusive)
  SELECT name, area/1000 FROM world
  WHERE area BETWEEN 200000 AND 250000


-- nested: Select the code which shows the years 
-- when a Medicine award was given but no Peace or 
-- Literature award was
  SELECT DISTINCT yr FROM nobel WHERE subject='Medicine' 
  AND yr NOT IN(SELECT yr FROM nobel WHERE subject='Literature') 
  AND yr NOT IN (SELECT yr FROM nobel WHERE subject='Peace')


-- select within select
-- Show the countries in Europe with a per capita GDP 
-- greater than 'United Kingdom'
	select name from world where continent = 'Europe' 
	and gdp/population > 
	(select gdp/population from world where name = 'United Kingdom')


-- We can use the word ALL to allow >= or > or < or <=to act over a list.
-- Which countries have a GDP greater than every 
-- country in Europe? [Give the name only.] 
-- (Some countries may have NULL gdp values)
	select name from world where 
	gdp is not NULL 
	and gdp > 
	all (select gdp from world where continent = 'Europe' 
		and gdp is not NULL)


-- We can refer to values in the outer SELECT within the inner SELECT. 
-- We can name the tables so that we can tell the difference between 
-- the inner and outer versions.
-- Find the largest country (by area) in each continent, 
-- show the continent, the name and the area:
	SELECT continent, name, area FROM world x
	  WHERE area >= ALL
	    (SELECT area FROM world y
	        WHERE y.continent=x.continent
	          AND area>0); -- and area is not NULL


-- Find all countries that belongs to a continent if each country's population 
-- is below 25000000. Show name, continent and population.
	select name, continent, population from world x 
		where 25000000 > all 
		(select population from world y 
			where x.continent = y.continent)


-- Some countries have populations more than three times that of any of 
-- their neighbours (in the same continent). Give the countries and continents.
	select name, continent from world x 
		where population > all
			(select 3*population from world y 
				where x.continent = y.continent and x.name != y.name)


-- Some countries have populations more than three times 
-- that of any of their neighbours (in the same continent). 
-- Give the countries and continents.
	select name, continent from world x 
	where population/3 > 
	all(select population from world y 
		where x.continent = y.continent 
		and x.name != y.name)



-- aggregate function
-- Using SUM, Count, MAX, DISTINCT and ORDER BY.
-- Using GROUP BY and HAVING.

-- execute sequence:
-- 1.FROM
-- 2.WHERE
-- 3.GROUP BY
-- 4.HAVING
-- 5.SELECT
-- 6.ORDER BY

-- in select, each item should be either grouped or from aggregate function

-- For each continent show the continent and number of countries.
	select continent,  count(name) from world group by continent



-- For each continent show the continent 
-- and number of countries with populations of at least 10 million.
	select continent, count(name) from world 
		where population >= 10000000 
		group by continent



-- List the continents that have a total 
-- population of at least 100 million
	select continent from world 
		group by continent 
			having sum(population) > 100000000

-- join
-- Show the player, teamid and mdate and for every German goal. 
-- teamid='GER'
	SELECT player,teamid, mdate
	  FROM game JOIN goal ON (id=matchid) where teamid = 'GER'


-- show the name of all players who scored a goal against Germany.
	SELECT distinct player
	  FROM game JOIN goal ON matchid = id 
	    WHERE (team1='GER' or team2='GER') and teamid != 'GER'


-- case when ... = ... then 1 else 0 end score1
-- left outer join
-- difficult problem
	SELECT mdate,
	  team1,
	  sum(CASE WHEN team1=teamid THEN 1 ELSE 0 END) as score1,
	  team2,
	   sum(CASE WHEN team2=teamid THEN 1 ELSE 0 END) as score2
	  FROM game left outer JOIN goal ON matchid = id group by mdate, team1, team2 order by mdate, matchid, team1, team2


-- join 3 tables
-- Obtain the cast list for the film 'Alien'
-- movie, actor, casting
	select name from actor join casting 
	on actor.id=casting.actorid join movie 
	on movie.id=casting.movieid where title='Alien'


-- Obtain the cast list for 'Casablanca'. 
-- Use the id value that you obtained in the previous question
	select actor.name from casting 
		join movie on movie.id = casting.movieid 
		join actor on actor.id = casting.actorid 
	where movie.title = 'Casablanca'


-- List the film title and the leading actor 
-- for all of the films 'Julie Andrews' played in.
	SELECT distinct title,name FROM casting
	  join movie on movie.id=movieid
	  join actor on actor.id = casting.actorid
	WHERE movieid IN (
	  SELECT movieid FROM casting
	  WHERE actorid=(select id from actor where name='Julie Andrews'))
	  and ord=1



	select title, name from movie 
		join casting on movie.id = casting.movieid 
		join actor on actor.id = casting.actorid 
	where movie.id in 
		(select movieid from casting 
			join actor on actor.id = casting.actorid 
		where actor.name = 'Julie Andrews') 
	and ord = 1



-- List the films released in the year 1978 ordered 
-- by the number of actors in the cast.
	select title, count(distinct actorid) as act_num from movie 
		join casting on casting.movieid = movie.id 
		join actor on actor.id = casting.actorid 
	where movie.yr = 1978 
	group by title 
	order by count(actorid) desc



-- List all the people who have worked with 'Art Garfunkel'
	select name from actor 
		join casting on casting.actorid = actor.id 
		join movie on movie.id = casting.movieid 
	where movieid in 
		(select movieid from casting 
			join actor on casting.actorid = actor.id 
		where name = 'Art Garfunkel') 
	and name != 'Art Garfunkel'



-- Obtain a list in alphabetical order of actors 
-- who've had at least 30 starring roles
	select name 
	from actor join casting on casting.actorid=actor.id join movie on movie.id=casting.movieid 
	where ord=1 group by name having count(*)>=30



-- List all the people who have worked with 'Art Garfunkel'
	select distinct name 
	from actor join casting on casting.actorid=actor.id join movie on movie.id=casting.movieid 
	where movieid in (select movieid from movie join casting on movieid=movie.id join actor on actor.id = actorid where name='Art Garfunkel') and name !='Art Garfunkel'

-- inner join,left outer join, right outer join, ignore rows with NULL value
	SELECT teacher.name, dept.name
	 FROM teacher INNER JOIN dept
	           ON (teacher.dept=dept.id)

	SELECT teacher.name, dept.name
	 FROM teacher left outer JOIN dept
	           ON (teacher.dept=dept.id)

	SELECT teacher.name, dept.name
	 FROM teacher right outer JOIN dept
	           ON (teacher.dept=dept.id)

-- coalesce
	select name, COALESCE(mobile,'07986 444 2266') from teacher

-- Use the COALESCE function and a LEFT JOIN to print 
-- the name and department name. Use the string 'None' 
-- where there is no department.
	select teacher.name, coalesce(dept.name, 'None') from teacher 
		left join dept on teacher.dept = dept.id

-- The LEFT JOIN will include rows from the left table even when the linking value is null.



  -- CASE WHEN condition1 THEN value1 
  --      WHEN condition2 THEN value2  
  --      ELSE def_value 
  -- END


-- self join
-- Execute the self join shown and observe that b.stop gives 
-- all the places you can get to from Craiglockhart, without 
-- changing routes. Change the query so that it shows the 
-- services from Craiglockhart to London Road.
	SELECT a.company, a.num, a.stop, b.stop
	FROM route a JOIN route b ON
	  (a.company=b.company AND a.num=b.num)
	WHERE a.stop=53 and b.stop=149



-- The query shown is similar to the previous one, 
-- however by joining two copies of the stops table 
-- we can refer to stops by name rather than by number. 
-- Change the query so that the services between 'Craiglockhart' 
-- and 'London Road' are shown. 
	SELECT a.company, a.num, stopa.name, stopb.name
	FROM route a JOIN route b ON
	  (a.company=b.company AND a.num=b.num)
	  JOIN stops stopa ON (a.stop=stopa.id)
	  JOIN stops stopb ON (b.stop=stopb.id)
	WHERE stopa.name='Craiglockhart' and stopb.name='London Road'



-- Give a distinct list of the stops which may be reached 
-- from 'Craiglockhart' by taking one bus, including 'Craiglockhart' itself. 
-- Include the company and bus no. of the relevant services.
	select s2.name, r2.company, r2.num 
	from route r1 join route r2 on (r1.num=r2.num and r1.company=r2.company) 
		join stops s1 on s1.id=r1.stop 
		join stops s2 on s2.id=r2.stop 
	where s1.name='Craiglockhart'



-- Find the routes involving two buses that can go 
-- from Craiglockhart to Sighthill.
-- Show the bus no. and company for the first bus, the name of the stop for the transfer,
-- and the bus no. and company for the second bus.
	SELECT distinct r1a.num, r1a.company, s1b.name, r2b.num, r2b.company
	FROM route r1a JOIN route r1b ON (r1a.company=r1b.company AND r1a.num=r1b.num) 
			join stops s1a on s1a.id=r1a.stop 
			join stops s1b on s1b.id=r1b.stop,
		route r2a join route r2b on (r2a.company=r2b.company and r2a.num=r2b.num)
			join stops s2a on s2a.id=r2a.stop 
			join stops s2b on s2b.id=r2b.stop 
	where s1b.id=s2a.id and s1a.name='Craiglockhart' and s2b.name='Sighthill'



-- de-duplicate example
create table t1(col1 int, col2 int, col3 char(50))
insert into t1 values (1, 1, 'data value one'),
insert into t1 values (1, 1, 'data value one'),
insert into t1 values (1, 2, 'data value two');

-- identify duplicate
SELECT col1, col2, count(*)
FROM t1
GROUP BY col1, col2

set rowcount 1 -- always n-1, where n is the number of duplicates
delete from t1
where col1=1 and col2=1
HAVING count(*) > 1




-- for large set of duplicates
insert INTO holdkey
SELECT col1, col2, col3=count(*)
FROM t1
GROUP BY col1, col2
HAVING count(*) > 1


insert INTO holddups
SELECT DISTINCT t1.*
FROM t1, holdkey
WHERE t1.col1 = holdkey.col1
AND t1.col2 = holdkey.col2


-- SELECT col1, col2, count(*)
-- FROM holddups
-- GROUP BY col1, col2


DELETE t1
FROM t1, holdkey
WHERE t1.col1 = holdkey.col1
AND t1.col2 = holdkey.col2

INSERT t1 SELECT * FROM holddups





 CREATE TABLE dbo.Employee
( 
EmpID int IDENTITY(1,1) NOT NULL, 
Name varchar(55) NULL, 
Salary decimal(10, 2) NULL, 
Designation varchar(20) NULL
 ) 


  WITH TempEmp (Name,duplicateRecCount)
AS
(
SELECT Name,ROW_NUMBER() OVER(PARTITION by Name, Salary ORDER BY Name) 
AS duplicateRecCount
FROM dbo.Employee
)
--Now Delete Duplicate Records
DELETE FROM TempEmp
WHERE duplicateRecCount > 1 
