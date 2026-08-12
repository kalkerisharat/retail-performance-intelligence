
  📊 Retail Performance Intelligence

>   End-to-end Business Intelligence & Analytics pipeline using Python, MySQL, SQL, Power BI and DAX  

![Dashboard Preview](screenshots/dashboard.png)

   Overview

  Retail Performance Intelligence   is an end-to-end data analytics project that transforms raw retail transaction data into actionable business insights.

The project combines   Python for data validation and analysis, MySQL for structured data storage, SQL for business analysis, and Power BI + DAX for interactive business intelligence reporting.  

Rather than focusing only on revenue, the project analyzes the relationship between:

- Sales
- Profitability
- Discounts
- Products
- Customers
- Regions
- Segments
- Shipping
- Time

The objective is to identify   what drives revenue, what drives profit, and where the business is losing money.  

---

   🎯 Business Questions

The analysis was designed around practical business questions:

- What are the company's overall sales and profitability?
- Which categories and sub-categories drive profit?
- Which products generate the highest and lowest profit?
- Which regions perform best?
- Which customer segments are most profitable?
- How does discounting affect profitability?
- Which shipping modes perform best?
- Which customers generate the most and least profit?
- How do sales and profit change over time?
- Are there data-quality issues that could affect analysis?

---

## 🏗️ End-to-End Architecture

```mermaid
flowchart TD
    A[Raw Transaction Data] --> B[Python + Pandas]
    B --> C[MySQL]
    C --> D[SQL Business Analysis]
    D --> E[Power BI + DAX]
    E --> F[Business Insights]

    B --> B1[Load & Validate]
    B --> B2[Exploratory Analysis]

    C --> C1[Structured Storage]
    C --> C2[Data Validation]

    D --> D1[KPI Analysis]
    D --> D2[Profitability Analysis]
    D --> D3[Customer & Product Analysis]

    E --> E1[Interactive Dashboard]
    E --> E2[KPI Measures]
    E --> E3[Interactive Filters]

  🛠️ Technology Stack

| Technology       | Role                                              |
| ---------------- | ------------------------------------------------- |
|   Python         | Data loading, validation and exploratory analysis |
|   Pandas         | Data manipulation and analysis                    |
|   MySQL          | Structured relational data storage                |
|   SQL            | Business analysis and aggregations                |
|   Power BI       | Interactive dashboard and visualization           |
|   DAX            | KPI and analytical measures                       |
|   Git & GitHub   | Version control and project documentation         |

---

  📁 Project Structure

   text
retail-performance-intelligence/
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
   

> File names may vary depending on the final project structure.

---

  📌 Dataset

The project uses a retail Superstore transaction dataset containing   9,994 records and 21 attributes  .

The dataset includes information about:

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
  Customer Segments
  Shipping Modes
  Order Dates

    Dataset validation

   text
Rows:              9,994
Columns:              21
Missing values:        0
   

---

  🐍 1. Python Analysis

Python was used as the initial analytical and validation layer.

    Key tasks

  Loaded transactional data using Pandas
  Validated dataset dimensions
  Checked missing values
  Validated numerical fields
  Analyzed sales and profitability
  Investigated discount behavior
  Identified top and bottom products
  Analyzed yearly and monthly performance
  Cross-checked results before loading data into MySQL

    Python → MySQL validation

   text
Rows:       9,994
Sales:      2,297,200.8603
Profit:       286,397.0217
Quantity:      37,873
   

---

  🗄️ 2. MySQL Data Layer

The validated dataset was loaded into MySQL for structured querying and business analysis.

   text
Database: superstore_db
Table:    superstore
   

The MySQL layer was independently validated against the source dataset using:

  Row counts
  Sales totals
  Profit totals
  Quantity totals
  Missing-value checks
  Invalid-value checks

---

  🔎 3. SQL Business Analysis

SQL was used to convert business questions into measurable analytical queries.

    Analysis areas

  Overall KPIs
  Category performance
  Sub-category profitability
  Discount analysis
  Product profitability
  Yearly performance
  Monthly performance
  Regional performance
  Customer segment performance
  Shipping performance
  Customer profitability
  Data-quality validation

    SQL techniques

   text
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
   

The complete SQL analysis is available in:

   text
sql/Superstore_Analytics.sql
   

---

  📊 4. Power BI Dashboard

Power BI acts as the final business intelligence layer.

The dashboard connects to the   MySQL database   using   Import connectivity  .

    Dashboard KPIs

  Total Sales
  Total Profit
  Total Orders
  Total Customers
  Profit Margin

    Analytical Visuals

  Sales & Profit Trend
  Sales & Profit by Category
  Profit by Sub-Category
  Regional Sales & Profit
  Sales by Customer Segment
  Profit Margin by Segment
  Profit by Discount Level
  Sales & Profit by Shipping Mode
  Top 10 Products by Profit
  Bottom 10 Products by Profit

    Interactive Filters

  Year
  Region
  Customer Segment

---

  🧮 DAX Measures

The dashboard uses DAX measures rather than hard-coded values.

   DAX
Total Sales =
SUM('superstore_db superstore'[sales])
   

   DAX
Total Profit =
SUM('superstore_db superstore'[profit])
   

   DAX
Total Quantity =
SUM('superstore_db superstore'[quantity])
   

   DAX
Total Orders =
DISTINCTCOUNT('superstore_db superstore'[order_id])
   

   DAX
Total Customers =
DISTINCTCOUNT('superstore_db superstore'[customer_id])
   

   DAX
Profit Margin =
DIVIDE([Total Profit], [Total Sales])
   

   DAX
Average Order Value =
DIVIDE([Total Sales], [Total Orders])
   

---

  📈 Key Business Results

| KPI                     |      Result |
| ----------------------- | ----------: |
|   Total Sales           |   $2.297M   |
|   Total Profit          |   $286.4K   |
|   Total Orders          |     5,009   |
|   Total Customers       |       793   |
|   Total Quantity        |    37,873   |
|   Profit Margin         |    12.47%   |
|   Average Order Value   |   $458.61   |

---

  💡 Key Business Insights

    🥇 Technology leads overall performance

Technology generated the highest total sales and profit among the three major categories.

This makes Technology the strongest overall category based on both revenue and absolute profitability.

---

    📦 Product profitability varies significantly

The highest-profit product was:

  Canon imageCLASS 2200 Advanced Copier  

   text
Profit ≈ $25.2K
   

The largest loss-making product was:

  Cubify CubeX 3D Printer Double Head Print  

   text
Loss ≈ $8.9K
   

This highlights the importance of evaluating products using   profitability rather than sales alone  .

---

    💸 Discounts are strongly associated with weaker profitability

Several higher-discount levels produced negative total profit.

Examples:

   text
0% discount   → +$321K profit
20% discount  → +$90K profit
30% discount  → -$10K loss
40% discount  → -$23K loss
70% discount  → -$40K loss
80% discount  → -$31K loss
   

The analysis suggests that aggressive discounting can significantly reduce profitability.

>   Business implication:   Discount strategies should be evaluated against profit and margin, not revenue alone.

---

    🌎 West is the strongest region

The   West   region generated the highest total sales and total profit.

This makes it the strongest region in terms of absolute financial contribution.

---

    👥 Largest segment ≠ most profitable segment

The   Consumer   segment generated the highest absolute sales and profit.

However:

   text
Home Office → Highest Profit Margin
   

This demonstrates why both   absolute profit   and   profit margin   should be considered when evaluating customer segments.

---

    🚚 Shipping volume ≠ profitability efficiency

Standard Class generated the highest:

  Sales
  Profit
  Number of orders

However,   First Class achieved the highest profit margin   among the shipping modes analyzed.

This highlights the difference between   volume   and   profitability efficiency  .

---

    👤 Customer profitability requires more than revenue

The most profitable customer was:

  Tamara Chand  

   text
Profit ≈ $8.98K
   

The largest loss-making customer was:

  Cindy Stewart  

   text
Loss ≈ $6.63K
   

Some customers generated substantial sales while still producing losses.

> Revenue alone does not indicate customer value.

---

  🔍 Data Quality Validation

The dataset was validated throughout the pipeline.

| Validation           |    Result |
| -------------------- | --------: |
| Total rows           |   9,994   |
| Missing Order IDs    |       0   |
| Missing Customer IDs |       0   |
| Missing Sales        |       0   |
| Missing Profit       |       0   |
| Negative Sales       |       0   |
| Invalid Quantity     |       0   |
| Invalid Discount     |       0   |

Python and MySQL aggregate results were cross-checked before building the Power BI dashboard.

---

  🎯 Business Takeaways

The analysis highlights several areas that could support business decision-making:

    1. Protect margins

High-discount transactions should be monitored because several discount levels are associated with negative profitability.

    2. Investigate loss-making products

Products generating recurring losses should be reviewed for:

  Pricing
  Discounts
  Cost structure
  Demand
  Product strategy

    3. Evaluate customers by profitability

High-revenue customers are not necessarily high-profit customers.

    4. Look beyond total sales

Regional, segment and shipping analysis demonstrates why   profit margin   is an important complement to revenue.

---

  🚀 Future Improvements

Potential extensions include:

  Customer Lifetime Value analysis
  RFM customer segmentation
  Sales forecasting
  Profitability prediction
  Advanced DAX time intelligence
  Automated Power BI refresh
  Geographic profitability analysis
  Executive KPI alerts
  Automated data pipeline

---

  📚 Skills Demonstrated

This project demonstrates practical experience with:

  Data Analytics  

  Exploratory Data Analysis
  Data Validation
  KPI Development
  Business Analysis
  Data Storytelling

  SQL & Databases  

  MySQL
  Aggregations
  GROUP BY
  DISTINCT analysis
  Date functions
  Data-quality validation

  Business Intelligence  

  Power BI
  DAX
  Interactive dashboards
  KPI cards
  Slicers
  Drill-down analysis
  Business-focused visualization

  Programming  

  Python
  Pandas

  Development Workflow  

  Git
  GitHub
  End-to-end analytics pipeline

---

  🔮 Future Direction

The current project establishes the foundation for a broader retail intelligence platform.

Future iterations could introduce:

   text
Historical Data
      ↓
Automated Pipeline
      ↓
Data Warehouse
      ↓
Advanced Analytics
      ↓
Forecasting
      ↓
Predictive Insights
      ↓
Executive Decision Support
   

---

  👨‍💻 Author

   Sharat Kalkeri

Computer Science & Engineering

  Focus Areas  

 Data Analytics  ·  SQL  ·  Python  ·  Power BI  ·  Business Intelligence  ·  Cloud Technology 

---

   ⭐ Project Summary

   text
9,994        Transactions analyzed
$2.297M      Total Sales
$286.4K      Total Profit
5,009        Orders
793          Customers
12.47%       Profit Margin
   

>   From raw retail transactions to business decisions — powered by Python, SQL, MySQL, Power BI and DAX.  

 the one I'd use for the GitHub repository.   It is considerably more recruiter-oriented: the first screen immediately communicates   what you built, the architecture, the tools, the business problem, and measurable outcomes  , instead of making the recruiter read through a long project description first.
