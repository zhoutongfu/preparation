-- 2
insert into Product values ('Z', '4003', 'Printer'), ('Z', '4001', 'PC'), ('Z', '4002', 'Laptop')

-- 3
insert into PC values (22, '4444',1200, DEFAULT  ,DEFAULT , DEFAULT,1350)

-- 4
insert into PC (code, model, speed, ram, hd, price)
select min(code)+20 as code, model+1000 as model, max(speed) as speed, max(ram)*2 as ram, max(hd)*2 as hd, max(price)/1.5 as price from Laptop group by model

-- 5
delete from PC where hd=(select min(hd) from PC) or ram=(select min(ram) from PC)

-- 6
delete from Laptop
	where model in (select distinct Laptop.model from Product join Laptop on Product.model=Laptop.model 
		where maker not in (select distinct a.maker from Product a join Product b on a.maker=b.maker where a.type='Laptop' and b.type='Printer' ))
-- 7
update Product 
set Maker='Z' where maker='A' and type='Printer'
