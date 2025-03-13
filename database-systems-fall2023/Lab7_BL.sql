SELECT productid, productname, productprice, vendorname
FROM product p, vendor v
WHERE p.vendorid = v.vendorid
ORDER BY productid;


SELECT productid, productname, productprice
FROM product p, category c
WHERE p.categoryid = c.categoryid AND categoryname = 'Camping'
ORDER BY productid;




SELECT productid, productname, productprice
FROM product
WHERE productprice = (SELECT MIN(productprice) FROM product);





SELECT productid, productname, vendorname
FROM product p, vendor v
WHERE p.vendorid = v.vendorid AND
	productprice < (SELECT AVG(productprice) FROM product);





SELECT p.productid, p.productname
FROM product p
JOIN includes i
ON i.productid = p.productid
GROUP BY productid
HAVING SUM(i.quantity) > 2;






SELECT productid, productname
FROM product p
WHERE productid IN
  (SELECT productid
   FROM includes
   GROUP BY productid
   HAVING SUM(quantity) > 2)
   ORDER BY productid;







SELECT p.productid, p.productname, p.productprice
FROM product p, includes i
WHERE i.productid = p.productid
GROUP BY productid
HAVING COUNT(i.tid) > 1
ORDER BY productid;

ALTER TABLE customer ADD (custphone CHAR(12) NOT NULL);
SELECT custphone
FROM customer;




UPDATE customer
SET custphone = '0';








ALTER TABLE customer 
DROP custphone;

SELECT *
FROM customer;






SELECT productid, productname
FROM product
WHERE productprice IS NULL;
