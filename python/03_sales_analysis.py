import pandas as pd 
sales_data = sales_data = pd.read_csv("Superstore.csv", encoding="latin1")

sales_data["Order Date"] = pd.to_datetime(sales_data["Order Date"])
sales_data["Ship Date"] = pd.to_datetime(sales_data["Ship Date"])

# what is the company's total revenue?
total_sales = sales_data["Sales"].sum()
print("Total Sales:", total_sales)

# total profit
total_profit = sales_data["Profit"].sum()
print("Total Profit", total_profit)

# total quantity sold
total_quantity = sales_data["Quantity"].sum()
print("Total Quantity Sold:",total_quantity)

# number of Orders 
number_of_orders = sales_data["Order ID"].nunique()
print("Number of Orders:", number_of_orders)

# number of customers
number_of_customers = sales_data["Customer ID"].nunique()
print("Number of Customers:", number_of_customers)

# profit margin - Profit Margin = Profit / Sales × 100
profit_margin = (total_profit / total_sales) * 100
print("Profit Margin", profit_margin)

# Average  Order Value
#Average Order Value = Total Sales / Number of Orders
average_order_values = total_sales / number_of_orders
print("Average Order Value:",average_order_values)

# which product category genrates the most sales and profit?
category_sales = sales_data.groupby("Category")["Sales"].sum()
print(category_sales)

category_profit = sales_data.groupby("Category")["Profit"].sum()
print(category_profit)

category_performance = sales_data.groupby("Category")[
    ["Sales", "Profit"]
].sum()

print(category_performance)

#Which sub-categories are generating profit and which are destroying it?
subcategory_performance = sales_data.groupby("Sub-Category")[["Sales","Profit"]].sum()
print(subcategory_performance)

average_discount = sales_data.groupby("Sub-Category")["Discount"].mean()
print(average_discount)
average_discount = sales_data.groupby("Sub-Category")["Discount"].mean()
print(average_discount)

discount_profit = sales_data.groupby("Discount")["Profit"].agg(["sum","mean","count"])
print(discount_profit)
'''"Higher discount levels are strongly associated with lower profitability in this dataset, with several discount levels above 30% showing negative average and total profit."'''

product_profit = sales_data.groupby("Product Name")["Profit"].sum()

top_profitable_products = product_profit.sort_values(
    ascending=False
).head(10)

print(top_profitable_products)

loss_making_products = product_profit.sort_values(
    ascending=True
).head(10)

print(loss_making_products)

product_performance = sales_data.groupby("Product Name")[
    ["Sales", "Profit"]
].sum()

product_performance["Profit Margin"] = (
    product_performance["Profit"] /
    product_performance["Sales"]
) * 100

print(product_performance)

top_margin_products = product_performance.sort_values(
    "Profit Margin",
    ascending=False
).head(10)

print(top_margin_products)

lowest_margin_products = product_performance.sort_values(
    "Profit Margin"
).head(10)

print(lowest_margin_products)

sales_data["Order Year"] = sales_data["Order Date"].dt.year
yearly_performance = sales_data.groupby("Order Year")[
    ["Sales", "Profit"]
].sum()

print(yearly_performance)

yearly_performance["Sales Growth %"] = (
    yearly_performance["Sales"].pct_change() * 100
)
yearly_performance["Profit Growth %"] = (
    yearly_performance["Profit"].pct_change() * 100
)
print(yearly_performance)

#Year-Month | Sales | Profit
sales_data["Order Month"] = sales_data["Order Date"].dt.month
sales_data["Order Year Month"] = sales_data["Order Date"].dt.to_period("M")

monthly_performance = sales_data.groupby(
    "Order Year Month"
)[["Sales", "Profit"]].sum()

print(monthly_performance)