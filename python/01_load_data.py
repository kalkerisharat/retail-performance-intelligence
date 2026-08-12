
# print(sales_data.head())
# print(sales_data.shape)
# print(sales_data.columns)
# print(sales_data.info())
# #9,994 rows , 21 columns

# # data cleaning - currently dates are type pf string we need convert it into Pandas datetime representation 
# sales_data["Order Date"] = pd.to_datetime(
#     sales_data["Order Date"]
# )
# sales_data["Ship Date"] = pd.to_datetime(
#     sales_data["Ship Date"]
# )


# print("Number of rows:", len(sales_data))
# print("Number of columns:", len(sales_data.columns))
# print("Missing values:", sales_data.isna().sum().sum())


import pandas as pd
import mysql.connector

# 1. Load the exact CSV we used for our analysis
df = pd.read_csv("Superstore.csv", encoding="latin1")

print("CSV rows:", len(df))
print("CSV columns:", len(df.columns))


# 2. Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="superstore_db"
)

cursor = connection.cursor()

print("Connected to MySQL")


# 3. Remove the old table if it exists
cursor.execute("DROP TABLE IF EXISTS superstore")


# 4. Create the table
cursor.execute("""
CREATE TABLE superstore (
    row_id INT,
    order_id VARCHAR(30),
    order_date VARCHAR(20),
    ship_date VARCHAR(20),
    ship_mode VARCHAR(30),
    customer_id VARCHAR(30),
    customer_name VARCHAR(100),
    segment VARCHAR(30),
    country VARCHAR(50),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code INT,
    region VARCHAR(30),
    product_id VARCHAR(30),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255),
    sales DECIMAL(12,4),
    quantity INT,
    discount DECIMAL(5,2),
    profit DECIMAL(12,4)
)
""")


# 5. Insert the data
insert_query = """
INSERT INTO superstore (
    row_id,
    order_id,
    order_date,
    ship_date,
    ship_mode,
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region,
    product_id,
    category,
    sub_category,
    product_name,
    sales,
    quantity,
    discount,
    profit
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


# 6. Convert DataFrame rows into tuples
data = [
    tuple(row)
    for row in df.itertuples(index=False, name=None)
]


# 7. Insert all rows
cursor.executemany(insert_query, data)

connection.commit()

print("Rows inserted:", cursor.rowcount)


# 8. Verify the database
cursor.execute("""
SELECT
    COUNT(*),
    SUM(sales),
    SUM(profit),
    SUM(quantity)
FROM superstore
""")

result = cursor.fetchone()

print("\nMySQL verification:")
print("Rows:", result[0])
print("Sales:", result[1])
print("Profit:", result[2])
print("Quantity:", result[3])


cursor.close()
connection.close()

print("\nDone.")