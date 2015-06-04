# Employees Earning More Than Their Managers
select x.Name from Employee x join Employee y on y.Id = x.ManagerId where x.Salary > y.Salary;

# Duplicate Emails
select Email from Person group by Email having count(*) > 1;
select distinct a.Email from Person a join Person b on a.Email = b.Email where a.Id <> b.Id

# Combine Two Tables 
select a.FirstName, a.LastName, b.City, b.State from Person a left outer join Address b on a.PersonId = b.PersonId;

# Customers Who Never Order
select a.Name from Customers a left outer join Orders b on a.Id = b.CustomerId where b.Id is NULL;
select Name from Customers where Id not in (select CustomerId from Orders);

# Second Highest Salary 
select MAX(Salary) from Employee where Salary < (select Salary from Employee order by Salary desc limit 1);

# 