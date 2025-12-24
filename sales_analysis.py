import pandas as pd

df = pd.read_csv("sales_data.csv")
df.fillna(0, inplace=True)

df.drop_duplicates(inplace=True)

total_sales = df["Total_Sales"].sum()

best_product = df.groupby("Product")["Total_Sales"].sum().idxmax()

average_sales = df["Total_Sales"].mean()
max_sales = df["Total_Sales"].max()
min_sales = df["Total_Sales"].min()

print("📊 SALES ANALYSIS REPORT")
print("------------------------")
print(f"Total Sales: ₹{total_sales:,.2f}")
print(f"Best Selling Product: {best_product}")
print(f"Average Sales: ₹{average_sales:,.2f}")
print(f"Maximum Sales: ₹{max_sales:,.2f}")
print(f"Minimum Sales: ₹{min_sales:,.2f}")
