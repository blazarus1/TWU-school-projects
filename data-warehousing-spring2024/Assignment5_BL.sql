-- A- Who is the highest spending customer?
SELECT p.customerNumber, c.customerName, SUM(p.amount) AS sumOfPayments
FROM customers c, payments p
WHERE c.customerNumber = p.customerNumber
GROUP BY p.customerNumber
ORDER BY SUM(p.amount) DESC
LIMIT 1;

-- B- What is the total amount of revenue in 2003?
SELECT SUM(amount)
FROM payments
WHERE YEAR(paymentDate) = 2003;

-- C- Who is the president of the company?
SELECT employeeNumber, firstName, lastName, jobTitle
FROM employees
WHERE jobTitle = 'President';

-- D- What is the description of the product that sold most in 2003?
SELECT p.productName, od.productCode, p.productDescription
FROM products p
JOIN orderdetails od ON p.productCode = od.ProductCode
JOIN orders o ON od.orderNumber = o.orderNumber
WHERE YEAR(o.orderDate) = 2003
GROUP BY p.productCode
ORDER BY SUM(od.quantityOrdered) DESC
LIMIT 1;