import pandas as pd
sales_data = sales_data = pd.read_csv("Superstore.csv", encoding="latin1")
# data cleaning - currently dates are type pf string we need convert it into Pandas datetime representation 
sales_data["Order Date"] = pd.to_datetime(sales_data["Order Date"])
sales_data["Ship Date"] = pd.to_datetime(sales_data["Ship Date"])
print(sales_data.isna().sum())

print(sales_data.duplicated().sum())
print(sales_data["Order ID"].duplicated().sum())
print(sales_data["Product ID"].duplicated().sum())

print("Negative Sales:")
print((sales_data["Sales"] < 0).sum())

print("Non-positive Quantity:")
print((sales_data["Quantity"] <= 0).sum())

print("Invalid Discount:")
print(((sales_data["Discount"] < 0) | (sales_data["Discount"] > 1)).sum())