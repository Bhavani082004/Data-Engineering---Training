CREATE DATABASE retail_sales;
USE retail_sales;
CREATE TABLE stores (
    store_id INT AUTO_INCREMENT PRIMARY KEY,
    store_name VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL
);
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL
);
CREATE TABLE employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    store_id INT,
    FOREIGN KEY (store_id)
        REFERENCES stores(store_id)
);
CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    store_id INT NOT NULL,
    product_id INT NOT NULL,
    employee_id INT,
    quantity INT NOT NULL,
    sale_date DATE NOT NULL,
    FOREIGN KEY (store_id)
        REFERENCES stores(store_id),
    FOREIGN KEY (product_id)
        REFERENCES products(product_id),
    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id)
);
INSERT INTO stores (store_name, location)
VALUES
    ('Chennai Central', 'Chennai'),
    ('Bangalore Main', 'Bangalore'),
    ('Hyderabad Branch', 'Hyderabad');
INSERT INTO products (product_name, category, price)
VALUES
    ('Laptop', 'Electronics', 50000.00),
    ('Headphones', 'Electronics', 1500.00),
    ('Office Chair', 'Furniture', 4500.00),
    ('Keyboard', 'Accessories', 800.00);  
INSERT INTO employees (employee_name, store_id)
VALUES
    ('Arun', 1),
    ('Priya', 1),
    ('Rahul', 2),
    ('Meena', 3); 
INSERT INTO sales
    (store_id, product_id, employee_id, quantity, sale_date)
VALUES
    (1, 1, 1, 2, '2026-10-01'),
    (1, 2, 2, 5, '2026-10-01'),
    (2, 1, 3, 1, '2026-10-01'),
    (2, 3, 3, 3, '2026-10-02'),
    (3, 4, 4, 10, '2026-10-02'),
    (1, 3, 1, 2, '2026-10-02');  
SELECT * FROM stores;

SELECT * FROM products;

SELECT * FROM employees;

SELECT * FROM sales;  

INSERT INTO products
    (product_name, category, price)
VALUES
    ('Mouse', 'Accessories', 600.00);  
	
SELECT *FROM products;

SELECT *FROM products
WHERE category = 'Electronics';

UPDATE products
SET price = 650.00
WHERE product_id = 3;

SET SQL_SAFE_UPDATES = 0;

DELETE FROM products
WHERE product_name = 'Mouse';

SET SQL_SAFE_UPDATES = 1;

SELECT
    s.sale_id,
    st.store_name,
    p.product_name,
    s.quantity,
    p.price,
    s.quantity * p.price AS total_amount,
    s.sale_date
FROM sales AS s
JOIN stores AS st
    ON s.store_id = st.store_id
JOIN products AS p
    ON s.product_id = p.product_id;
     
DELIMITER //

CREATE PROCEDURE DailyStoreSales(
    IN p_store_id INT,
    IN p_sale_date DATE
)
BEGIN
    SELECT
        st.store_name,
        s.sale_date,
        SUM(s.quantity * p.price) AS daily_sales
    FROM sales AS s
    JOIN products AS p
        ON s.product_id = p.product_id
    JOIN stores AS st
        ON s.store_id = st.store_id
    WHERE s.store_id = p_store_id
      AND s.sale_date = p_sale_date
    GROUP BY
        st.store_name,
        s.sale_date;
END //

DELIMITER ; 

SELECT SUM(s.quantity * p.price) AS daily_sales
FROM sales s
JOIN products p ON s.product_id = p.product_id;

CALL DailyStoreSales(1, '2026-10-01');

CALL DailyStoreSales(2, '2026-10-02');

SELECT
    p.product_name,
    SUM(s.quantity) AS total_quantity_sold,
    SUM(s.quantity * p.price) AS total_revenue
FROM products AS p
LEFT JOIN sales AS s
    ON p.product_id = s.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY total_quantity_sold ASC;
CREATE INDEX idx_product_name
ON products(product_name);
CREATE INDEX idx_store_location
ON stores(location);
CREATE INDEX idx_sales_store_date
ON sales(store_id, sale_date);
SHOW INDEX FROM products;

SHOW INDEX FROM stores;

SHOW INDEX FROM sales;



  