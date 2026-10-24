-- INVENTORY MANAGEMENT SYSTEM (simple version)
-- Tables: products and sales

-- STEP 1: CREATE THE TABLES

CREATE TABLE products (
    product_id    INT PRIMARY KEY,
    product_name  VARCHAR(50),
    category      VARCHAR(30),
    supplier      VARCHAR(50),
    price         INT,
    quantity      INT,
    reorder_level INT
);

CREATE TABLE sales (
    sale_id       INT PRIMARY KEY,
    product_id    INT,
    quantity_sold INT,
    sale_date     DATE,
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);

-- STEP 2: ADD THE DATA

INSERT INTO products VALUES (1, 'USB Cable', 'Electronics', 'TechSource', 299, 85, 20);
INSERT INTO products VALUES (2, 'Wireless Mouse', 'Electronics', 'TechSource', 699, 12, 15);
INSERT INTO products VALUES (3, 'Power Bank', 'Electronics', 'TechSource', 1299, 30, 10);
INSERT INTO products VALUES (4, 'Basmati Rice 5kg', 'Groceries', 'FreshMart', 650, 60, 25);
INSERT INTO products VALUES (5, 'Sunflower Oil 1L', 'Groceries', 'FreshMart', 160, 9, 30);
INSERT INTO products VALUES (6, 'Tea Powder 500g', 'Groceries', 'FreshMart', 280, 45, 20);
INSERT INTO products VALUES (7, 'Notebook A4', 'Stationery', 'PaperWorld', 60, 200, 60);
INSERT INTO products VALUES (8, 'Ball Pen Pack', 'Stationery', 'PaperWorld', 50, 0, 40);
INSERT INTO products VALUES (9, 'Steel Water Bottle', 'Home', 'HomeEase', 350, 40, 15);
INSERT INTO products VALUES (10, 'Lunch Box', 'Home', 'HomeEase', 450, 7, 12);

INSERT INTO sales VALUES (1, 1, 5, '2026-09-02');
INSERT INTO sales VALUES (2, 2, 3, '2026-09-05');
INSERT INTO sales VALUES (3, 4, 2, '2026-09-08');
INSERT INTO sales VALUES (4, 7, 20, '2026-09-10');
INSERT INTO sales VALUES (5, 1, 4, '2026-09-14');
INSERT INTO sales VALUES (6, 10, 6, '2026-09-18');
INSERT INTO sales VALUES (7, 3, 2, '2026-09-21');
INSERT INTO sales VALUES (8, 9, 4, '2026-09-25');
INSERT INTO sales VALUES (9, 7, 15, '2026-10-01');
INSERT INTO sales VALUES (10, 5, 8, '2026-10-04');
INSERT INTO sales VALUES (11, 2, 2, '2026-10-09');
INSERT INTO sales VALUES (12, 6, 5, '2026-10-12');

-- STEP 3: QUERIES (SELECT)

-- Q1: Show all products
SELECT * FROM products;

-- Q2: Show only Electronics products
SELECT product_name, price, quantity FROM products WHERE category = 'Electronics';

-- Q3: Show products from the most expensive to the cheapest
SELECT product_name, price FROM products ORDER BY price DESC;

-- Q4: Show low stock products (quantity is less than or equal to reorder level)
SELECT product_name, quantity, reorder_level FROM products WHERE quantity <= reorder_level;

-- Q5: Count how many products we have
SELECT COUNT(*) AS total_products FROM products;

-- Q6: Total quantity of all items in stock
SELECT SUM(quantity) AS total_items_in_stock FROM products;

-- Q7: Total value of the stock (price x quantity)
SELECT SUM(price * quantity) AS total_stock_value FROM products;

-- Q8: Number of products in each category
SELECT category, COUNT(*) AS number_of_products FROM products GROUP BY category;

-- Q9: Show each sale with the product name
SELECT sales.sale_id, products.product_name, sales.quantity_sold, sales.sale_date
FROM sales
JOIN products ON sales.product_id = products.product_id;

-- Q10: Total units sold for each product
SELECT products.product_name, SUM(sales.quantity_sold) AS units_sold
FROM sales
JOIN products ON sales.product_id = products.product_id
GROUP BY products.product_name
ORDER BY units_sold DESC;

-- Q11: Total money earned from all sales
SELECT SUM(sales.quantity_sold * products.price) AS total_sales_amount
FROM sales
JOIN products ON sales.product_id = products.product_id;

-- STEP 4: CHANGING DATA (INSERT, UPDATE, DELETE)

-- C1: Add a new product
INSERT INTO products VALUES (11, 'Desk Lamp', 'Home', 'HomeEase', 799, 25, 8);

-- C2: A customer buys 3 USB Cables. Save the sale
INSERT INTO sales VALUES (13, 1, 3, '2026-10-18');

-- C3: Reduce the USB Cable stock by 3 (it was 85)
UPDATE products SET quantity = quantity - 3 WHERE product_id = 1;

-- C4: New stock arrives: add 50 Sunflower Oil (it was 9)
UPDATE products SET quantity = quantity + 50 WHERE product_id = 5;

-- C5: Change the price of USB Cable to 320
UPDATE products SET price = 320 WHERE product_id = 1;

-- C6: Delete the Desk Lamp
DELETE FROM products WHERE product_id = 11;

-- Q12: Check the final stock after all the changes
SELECT product_id, product_name, price, quantity FROM products;
