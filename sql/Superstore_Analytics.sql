-- SUPERSTORE SALES ANALYTICS - SQL PROJECT
-- Database: superstore_db | Table: superstore

USE superstore_db;

-- 1. Overall KPIs
SELECT SUM(sales) AS total_sales, SUM(profit) AS total_profit,
       SUM(quantity) AS total_quantity,
       COUNT(DISTINCT order_id) AS total_orders,
       COUNT(DISTINCT customer_id) AS total_customers,
       ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin,
       ROUND(SUM(sales) / COUNT(DISTINCT order_id), 2) AS average_order_value
FROM superstore;

-- 2. Category performance
SELECT category, SUM(sales) AS total_sales, SUM(profit) AS total_profit
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

-- 3. Sub-category profit
SELECT sub_category, SUM(profit) AS total_profit
FROM superstore
GROUP BY sub_category
ORDER BY total_profit DESC;

-- 4. Sub-category sales, profit and margin
SELECT sub_category, SUM(sales) AS total_sales, SUM(profit) AS total_profit,
       ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin
FROM superstore
GROUP BY sub_category
ORDER BY total_profit DESC;

-- 5. Discount analysis
SELECT discount, SUM(sales) AS total_sales, SUM(profit) AS total_profit,
       AVG(profit) AS average_profit
FROM superstore
GROUP BY discount
ORDER BY discount;

-- 6. Discount analysis with order count
SELECT discount, SUM(sales) AS total_sales, SUM(profit) AS total_profit,
       AVG(profit) AS average_profit,
       COUNT(DISTINCT order_id) AS total_orders
FROM superstore
GROUP BY discount
ORDER BY discount;

-- 7. Top 10 products by profit
SELECT product_name, SUM(profit) AS total_profit
FROM superstore
GROUP BY product_name
ORDER BY total_profit DESC
LIMIT 10;

-- 8. Bottom 10 products by profit
SELECT product_name, SUM(profit) AS total_profit
FROM superstore
GROUP BY product_name
ORDER BY total_profit ASC
LIMIT 10;

-- 9. Yearly performance
SELECT YEAR(STR_TO_DATE(order_date, '%m/%d/%Y')) AS order_year,
       SUM(sales) AS total_sales, SUM(profit) AS total_profit
FROM superstore
GROUP BY YEAR(STR_TO_DATE(order_date, '%m/%d/%Y'))
ORDER BY order_year;

-- 10. Monthly performance
SELECT DATE_FORMAT(STR_TO_DATE(order_date, '%m/%d/%Y'), '%Y-%m') AS order_month,
       SUM(sales) AS total_sales, SUM(profit) AS total_profit
FROM superstore
GROUP BY DATE_FORMAT(STR_TO_DATE(order_date, '%m/%d/%Y'), '%Y-%m')
ORDER BY order_month;

-- 11. Regional performance
SELECT region, SUM(sales) AS total_sales, SUM(profit) AS total_profit
FROM superstore
GROUP BY region
ORDER BY total_sales DESC;

-- 12. Segment performance
SELECT segment, SUM(sales) AS total_sales, SUM(profit) AS total_profit
FROM superstore
GROUP BY segment
ORDER BY total_sales DESC;

-- 13. Segment performance with margin
SELECT segment, SUM(sales) AS total_sales, SUM(profit) AS total_profit,
       ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin
FROM superstore
GROUP BY segment
ORDER BY profit_margin DESC;

-- 14. Shipping performance
SELECT ship_mode, SUM(sales) AS total_sales, SUM(profit) AS total_profit,
       COUNT(DISTINCT order_id) AS total_orders
FROM superstore
GROUP BY ship_mode
ORDER BY total_orders DESC;

-- 15. Shipping performance with margin
SELECT ship_mode, SUM(sales) AS total_sales, SUM(profit) AS total_profit,
       COUNT(DISTINCT order_id) AS total_orders,
       ROUND(SUM(profit) / SUM(sales) * 100, 2) AS profit_margin
FROM superstore
GROUP BY ship_mode
ORDER BY profit_margin DESC;

-- 16. Top 10 customers by profit
SELECT customer_name, SUM(sales) AS total_sales, SUM(profit) AS total_profit
FROM superstore
GROUP BY customer_name
ORDER BY total_profit DESC
LIMIT 10;

-- 17. Bottom 10 customers by profit
SELECT customer_name, SUM(sales) AS total_sales, SUM(profit) AS total_profit
FROM superstore
GROUP BY customer_name
ORDER BY total_profit ASC
LIMIT 10;

-- 18. Data quality: missing values
SELECT COUNT(*) AS total_rows,
       COUNT(order_id) AS order_id_present,
       COUNT(customer_id) AS customer_id_present,
       COUNT(sales) AS sales_present,
       COUNT(profit) AS profit_present
FROM superstore;

-- 19. Data quality: negative sales
SELECT COUNT(*) AS negative_sales
FROM superstore
WHERE sales < 0;

-- 20. Data quality: invalid quantity
SELECT COUNT(*) AS invalid_quantity
FROM superstore
WHERE quantity <= 0;

-- 21. Data quality: invalid discount
SELECT COUNT(*) AS invalid_discount
FROM superstore
WHERE discount < 0 OR discount > 1;

-- 22. Final validation
SELECT COUNT(*) AS total_rows,
       SUM(sales) AS total_sales,
       SUM(profit) AS total_profit,
       SUM(quantity) AS total_quantity
FROM superstore;
