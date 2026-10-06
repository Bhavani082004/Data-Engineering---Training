CREATE DATABASE shop_db;
USE shop_db;


CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL
);


INSERT INTO products (product_name, category, price, stock_quantity) VALUES
('Smartphone', 'Electronics', 15000.00, 25),
('Laptop', 'Electronics', 55000.00, 8),
('Running Shoes', 'Footwear', 2500.00, 15),
('T-Shirt', 'Clothing', 800.00, 50),
('Coffee Maker', 'Home Appliances', 3500.00, 5),
('Backpack', 'Accessories', 1200.00, 0);


SELECT * FROM products;


SELECT product_name, price FROM products;


INSERT INTO products (product_name, category, price, stock_quantity) 
VALUES ('Wireless Mouse', 'Electronics', 999.00, 20);


UPDATE products 
SET price = 2800.00 
WHERE product_id = 3;


UPDATE products 
SET price = price * 1.10 
WHERE category = 'Electronics';


UPDATE products 
SET stock_quantity = stock_quantity - 1 
WHERE product_id = 1;


UPDATE products 
SET category = 'Apparel' 
WHERE product_id = 4;


SELECT * FROM products 
WHERE price > 1000;


SELECT * FROM products 
WHERE stock_quantity < 10;


SELECT * FROM products 
WHERE category = 'Electronics';
SELECT * FROM products 
ORDER BY price DESC;


DELETE FROM products 
WHERE product_id = 5;


DELETE FROM products 
WHERE stock_quantity = 0;


SELECT * FROM products;