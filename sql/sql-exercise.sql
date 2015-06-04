-- 13

-- 14
select distinct maker, type 
from Product 
where maker in 
	(select maker 
		from Product 
		group by maker 
		having count(distinct type)=1 and count(*) > 1)

-- 15
select hd 
from PC 
	group by hd 
	having count(*) > 1

-- 16
Select distinct pc1.model, pc2.model, pc1.speed, pc1.ram 
from PC pc1, PC pc2 
where pc1.speed=pc2.speed 
	and pc1.ram=pc2.ram 
	and pc1.model > pc2.model

Select distinct pc1.model, pc2.model, pc1.speed, pc1.ram 
from PC pc1 join PC pc2 on
	pc1.ram=pc2.ram
	and pc1.speed=pc2.speed
	and pc1.model > pc2.model

-- 17
Select distinct type,Product.model,speed 
from Product join Laptop on Product.model=Laptop.model 
where type='Laptop' 
	and speed < all(select speed from PC)

-- 18
Select distinct maker, price 
from Product join Printer on Product.model=Printer.model 
where price=(select MIN(price) from Printer where color='y') 
									and color='y'
-- 19
Select maker, avg(screen) from Laptop left join Product on Laptop.model=Product.model group by maker

-- 20 
select maker, count(distinct model) as Count_Model from Product where type='PC' group by maker having count(distinct model) >= 3

-- 21
Select maker, MAX(price) from Product join PC on PC.model=Product.model group by maker

-- 22
Select speed, avg(price) from PC where speed > 600 group by speed

-- intersect, except: http://www.sql-tutorial.ru/en/book_intersect_except.html
-- 23
select maker from Product join PC on PC.model=Product.model 
	where type='PC' and speed >= 750
intersect
select maker from Product join Laptop on Laptop.model=Product.model 
	where type='Laptop' and speed >= 750

-- 24
Select model from
(
select model, price from PC
union
select model, price from Laptop
union
select model, price from Printer
) X
where X.price= (select max(Y.price) from (
select  price from PC
union
select  price from Laptop
union
select  price from Printer
) Y )
-- why the below does not work?
-- where X.price >= all 
-- 	(select price from PC 
-- 		union
-- 	select price from Printer
-- 		union 
-- 	select price from Laptop)
-- group by model;

-- 25

select distinct maker from (select distinct a.maker as maker, a.model as model 
	from Product a join Product b on a.maker=b.maker where a.type='PC' and b.type='Printer') x
	join PC on PC.model=x.model
	where ram=(select min(ram) from PC) and speed=(select max(speed) from PC where ram=(select min(ram) from PC))

-- 26 union all does not remove duplicates while union did
select avg(price) from (select price from PC join Product on PC.model=Product.model where maker='A'
union all
select price from Laptop join Product on Laptop.model=Product.model where maker='A') x


-- 27
Select maker, avg(hd) 
from PC join Product on Product.model=PC.model 
where maker in 
	(select distinct a.maker from Product a join Product b on a.maker=b.maker where a.type='Printer' and b.type='PC')
group by maker


-- 28
Select avg(hd) 
from PC join Product on Product.model=PC.model 
where maker in 
	(select distinct a.maker from Product a join Product b on a.maker=b.maker where a.type='Printer' and b.type='PC')

-- 29

