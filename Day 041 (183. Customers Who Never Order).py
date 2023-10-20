# Write your MySQL query statement below

SELECT name as Customers
FROM Customers c
INNER JOIN Orders o
ON c.id = o.customerId




## BEST ANSWER
## Require more work on sql to perform better

# Write your MySQL query statement below
SELECT Customers.name AS Customers 
FROM Customers 
WHERE Customers.id NOT IN (SELECT DISTINCT customerId FROM Orders)