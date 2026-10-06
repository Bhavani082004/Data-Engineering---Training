CREATE DATABASE sql_practice_pack;
USE sql_practice_pack;
CREATE TABLE menu_items (
 item_id INT PRIMARY KEY,
 item_name VARCHAR(100),
 category VARCHAR(50),
 price DECIMAL(10,2),
 available_qty INT
);
INSERT INTO menu_items VALUES
(1, 'Chicken Biryani', 'Main Course', 320, 25),
(2, 'Paneer Tikka', 'Starter', 240, 15),
(3, 'Masala Dosa', 'Breakfast', 120, 30),
(4, 'Veg Burger', 'Fast Food', 180, 10),
(5, 'Cold Coffee', 'Beverage', 150, 20),
(6, 'Chicken Burger', 'Fast Food', 220, 8),
(7, 'Idli', 'Breakfast', 80, 40),
(8, 'Fresh Lime', 'Beverage', 90, 0);
SELECT * FROM menu_items;
SELECT item_name, price
FROM menu_items;
INSERT INTO menu_items
VALUES (9, 'Chocolate Shake', 'Beverage', 180, 12);
UPDATE menu_items
SET price = 350
WHERE item_id = 1;
UPDATE menu_items
SET price = price * 1.10
WHERE item_id IN (4,6);
update menu_items
SET available_qty = available_qty -2
where item_id = 4;
delete from menu_items
where item_id = 8;
SELECT *
FROM menu_items
WHERE price > 200;
SELECT *
FROM menu_items
WHERE price BETWEEN 100 AND 250;
SELECT *
FROM menu_items
WHERE category = 'Breakfast';
SELECT *
FROM menu_items
WHERE category IN ('Breakfast', 'Beverage');
SELECT *
FROM menu_items
WHERE item_name LIKE '%Chicken%';
SELECT *
FROM menu_items
ORDER BY price DESC;
SELECT *
FROM menu_items
ORDER BY price DESC
LIMIT 3;
SELECT *
FROM menu_items
WHERE available_qty < 15;



