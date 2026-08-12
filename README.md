![alt text](<screenshot/Screenshot 2026-08-12 181031.png>)
  📊 Superstore Sales Analytics

>   End-to-end Business Intelligence & Data Analytics Project using Python, MySQL, SQL, Power BI, and DAX  

An end-to-end sales analytics project that transforms raw Superstore transactional data into actionable business insights through   Python-based data analysis, MySQL data storage, SQL analytics, and an interactive Power BI dashboard  .

The project focuses on understanding   sales performance, profitability, customer behavior, regional performance, discount impact, product performance, and operational trends  .

---

   🚀 Project Overview

Businesses generate large volumes of transactional data, but raw data alone does not provide actionable information.

This project builds a complete analytics workflow:

   
                    RAW DATA
                       │
                       ▼
              ┌─────────────────┐
              │ Python + Pandas │
              │ Data Validation │
              │ Exploratory     │
              │ Analysis        │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │     MySQL       │
              │ Data Storage    │
              │ & Transformation│
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │      SQL        │
              │ Business        │
              │ Analysis        │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Power BI + DAX  │
              │ Interactive BI  │
              │ Dashboard       │
              └────────┬────────┘
                       │
                       ▼
               BUSINESS INSIGHTS

🎯 Business Objectives

The project answers key business questions such as:

How much revenue and profit does the business generate?
Which categories and sub-categories drive profitability?
Which products generate the highest and lowest profits?
Which regions perform best?
Which customer segments are most valuable?
How does discounting affect profitability?
Which shipping modes are most profitable?
Which customers generate the highest profit?
How have sales and profit changed over time?
Are there data-quality issues that could affect decision-making?

| Technology       | Purpose                                         |
| ---------------- | ----------------------------------------------- |
|   Python         | Data loading, validation & exploratory analysis |
|   Pandas         | Data manipulation and analysis                  |
|   MySQL          | Relational data storage                         |
|   SQL            | Business analysis and aggregation               |
|   Power BI       | Interactive dashboard and visualization         |
|   DAX            | KPI calculations and analytical measures        |
|   Git & GitHub   | Version control and project documentation       |

superstore-sales-analytics/
│
├── python/
│   ├── 01_load_data.py
│   ├── 02_data_cleaning.py
│   └── 03_sales_analysis.py
│
├── sql/
│   └── Superstore_Analytics.sql
│
├── powerbi/
│   └── Superstore_Sales_Analytics.pbix
│
├── screenshots/
│   └── dashboard.png
│
├── README.md
└── .gitignore

📌 Dataset

The project uses the Superstore sales dataset, containing transactional information related to:

Orders
Customers
Products
Categories
Sub-Categories
Sales
Quantity
Discounts
Profit
Regions
Segments
Shipping modes
Order dates


Dataset dimensions

Rows:       9,994
Columns:       21

🐍 Phase 1 — Python Data Analysis

Python was used as the initial analytical layer.

Key tasks
Loaded the raw CSV dataset using Pandas
Validated dataset dimensions
Checked missing values
Verified numerical fields
Analyzed sales and profitability
Investigated discount behavior
Identified top and bottom performing products
Analyzed yearly and monthly trends
Validated analytical results before loading the data into MySQL

Data validation
Rows:             9,994
Columns:             21
Missing values:       0

Python analysis established the initial business findings and provided a reference point for validating the SQL and Power BI results.

🗄️ Phase 2 — MySQL Data Pipeline

The validated dataset was loaded into MySQL for structured analysis.

Database
Database: superstore_db
Table:    superstore

The Python-to-MySQL pipeline was validated using row counts and aggregate metrics.

Validation
Rows:       9,994
Sales:      2,297,200.8603
Profit:       286,397.0217
Quantity:      37,873

This ensured that the data loaded into MySQL matched the source dataset.

🔎 Phase 3 — SQL Business Analysis

SQL was used to answer business questions directly from the MySQL database.

Analysis performed
Overall business KPIs
Category performance
Sub-category profitability
Discount analysis
Top 10 products
Bottom 10 products
Yearly performance
Monthly performance
Regional performance
Customer segment performance
Shipping performance
Top customers
Bottom customers
Data-quality validation
SQL concepts used
SELECT
WHERE
GROUP BY
ORDER BY
LIMIT
SUM()
AVG()
COUNT()
COUNT(DISTINCT)
ROUND()
YEAR()
STR_TO_DATE()
DATE_FORMAT()
📊 Phase 4 — Power BI Dashboard

The final analytical layer was built using Power BI.

The dashboard connects directly to the MySQL database using the Import connectivity mode.

Key KPI Measures
Total Sales = SUM('superstore_db superstore'[sales])

Total Profit = SUM('superstore_db superstore'[profit])

Total Quantity = SUM('superstore_db superstore'[quantity])

Total Orders =
DISTINCTCOUNT('superstore_db superstore'[order_id])

Total Customers =
DISTINCTCOUNT('superstore_db superstore'[customer_id])

Profit Margin =
DIVIDE([Total Profit], [Total Sales])

Average Order Value =
DIVIDE([Total Sales], [Total Orders])
📈 Dashboard Features

The Power BI dashboard includes:

KPI Overview
Total Sales
Total Profit
Total Orders
Total Customers
Profit Margin
Performance Analysis
Sales & Profit Trend
Sales & Profit by Category
Profit by Sub-Category
Regional Sales & Profit
Sales by Customer Segment
Profit Margin by Segment
Profit by Discount Level
Sales & Profit by Shipping Mode
Product Analysis
Top 10 Products by Profit
Bottom 10 Products by Profit
Interactive Filters
Year
Region
Customer Segment
💡 Key Business Insights
1. Overall Performance

The business generated:

KPI	Value
Total Sales	$2.297M
Total Profit	$286.4K
Total Orders	5,009
Total Customers	793
Profit Margin	12.47%
Total Quantity	37,873
2. Category Performance

Technology generated the highest total sales and profit among the three major categories.

Technology
    ↓
Highest Sales
    ↓
Highest Profit

This makes Technology the strongest overall category in the dataset.

3. Sub-Category Profitability

The strongest profit contributors included:

Copiers
Phones
Accessories
Paper
Binders

However, several sub-categories generated losses.

The largest loss was recorded by:

Tables → -$17.7K

This demonstrates why analyzing profit rather than sales alone is important.

4. Discount Impact

Discount analysis revealed a strong relationship between higher discount levels and weaker profitability.

Examples:

0% discount  → +$321K profit
20% discount → +$90K profit
30% discount → -$10K loss
40% discount → -$23K loss
70% discount → -$40K loss
80% discount → -$31K loss

Higher discount levels are associated with significantly weaker profitability in this dataset.

This analysis shows why discount strategies should be evaluated against margin rather than revenue alone.

5. Regional Performance

The West region generated the highest:

Sales
Total Profit

However, regional performance also shows that higher sales do not automatically translate into proportionally higher profitability.

6. Customer Segment

The Consumer segment generated the highest absolute Sales and Profit.

However:

Home Office → Highest Profit Margin

This demonstrates the difference between:

Largest segment

and

Most profitable segment relative to sales

7. Shipping Performance

Standard Class generated the highest:

Sales
Profit
Number of Orders

However, First Class achieved the highest profit margin among the shipping modes analyzed.

Again:

Highest volume ≠ highest profitability efficiency.

8. Product Profitability

The highest-profit product was:

Canon imageCLASS 2200 Advanced Copier
Profit ≈ $25.2K

The largest loss-making product was:

Cubify CubeX 3D Printer Double Head Print
Loss ≈ $8.9K

This highlights products that may deserve further investigation around:

Pricing
Discounting
Cost structure
Demand
Product strategy
9. Customer Profitability

The most profitable customer was:

Tamara Chand
Profit ≈ $8.98K

The largest loss-making customer was:

Cindy Stewart
Loss ≈ $6.63K

Interestingly, some customers generated substantial sales while still producing losses.

This reinforces the importance of analyzing:

Revenue + Profit

rather than revenue alone.

🔍 Data Quality Validation

Before building the final dashboard, the dataset was validated at multiple stages.

Validation results
Total Rows             9,994
Missing Order IDs          0
Missing Customer IDs       0
Missing Sales              0
Missing Profit             0
Negative Sales             0
Invalid Quantity           0
Invalid Discount           0

The Python, MySQL, and Power BI layers were cross-validated using aggregate metrics to ensure consistency.

🔄 End-to-End Data Flow

The final architecture demonstrates how multiple analytics technologies can work together:

                 ┌─────────────────┐
                 │  Superstore CSV │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Python / Pandas │
                 │                 │
                 │ • Load          │
                 │ • Validate      │
                 │ • Analyze       │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │      MySQL      │
                 │                 │
                 │ • Store         │
                 │ • Query         │
                 │ • Aggregate     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │     Power BI    │
                 │                 │
                 │ • DAX           │
                 │ • Visualization │
                 │ • Interaction  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Business        │
                 │ Insights        │
                 └─────────────────┘
📸 Dashboard Preview

Add your final Power BI dashboard screenshot here:

![Superstore Sales Analytics Dashboard](screenshot\Screenshot 2026-08-12 181031.png)

🧠 What I Learned

This project helped develop practical experience in:

Data cleaning and validation
Exploratory data analysis
Business KPI development
SQL aggregation and analytical queries
Relational database workflows
Data validation across multiple tools
Power BI dashboard development
DAX measure creation
Business-oriented data storytelling
Translating business questions into analytical queries

More importantly, the project demonstrates an end-to-end analytics workflow rather than isolated tool usage.

🚀 Future Improvements

Potential extensions include:

Customer lifetime value analysis
Customer segmentation
RFM analysis
Forecasting future sales
Profitability prediction
Automated Power BI refresh
Additional geographic analysis
Advanced DAX time-intelligence measures
Executive-level KPI alerts
Automated data pipeline


👨‍💻 Author

Sharat Kalkeri

Computer Science & Engineering

Interested in:

Data Analytics
Business Intelligence
SQL
Python
Power BI
Cloud & Technology

⭐ Project Highlights
9,994+        Transactions analyzed
$2.297M       Total Sales
$286.4K       Total Profit
5,009         Orders
793           Customers
12.47%        Profit Margin

From raw transactional data to business decisions — using Python, SQL, MySQL, Power BI and DAX.
