“Analysis of Monthly Sales Performance of a Retail Store”                         
 Dataset:
Month	Sales (₹)	Profit (₹)	Customers	Advertisement Spend (₹)
Jan	12000	2500	200	1500
Feb	15000	3000	240	1700
Mar	18000	3500	300	1900
Apr	22000	5000	400	2100
May	25000	6000	420	2500
Jun	20000	4500	390	2000
Jul	27000	6200	440	2600
Aug	30000	7000	480	3000
Sep	28000	6400	460	2800
Oct	35000	8000	500	3300
Nov	32000	7500	470	3100
Dec	40000	9500	550	4000

1.Bar Graph – Monthly Sales Comparison
Code:
import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales = [12000,15000,18000,22000,25000,20000,27000,30000,28000,35000,32000,40000]

plt.bar(months, sales, color='skyblue')
plt.title("Monthly Sales Comparison")
plt.xlabel("Months")
plt.ylabel("Sales (₹)")
plt.show()
 
Why use Bar Graph:
A bar graph is best for comparing discrete categories (months) side-by-side. It clearly shows which months performed better or worse in sales.

2.) Pie Chart – Percentage Contribution of Each Month to Total Sales
import matplotlib.pyplot as plt
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales = [12000,15000,18000,22000,25000,20000,27000,30000,28000,35000,32000,40000]

plt.pie(sales, labels=months, autopct='%1.1f%%', startangle=90)
plt.title("Percentage Contribution to Annual Sales")
plt.show()
 
Why use Pie Chart:
A pie chart is ideal for showing proportional contribution of each month to the total annual sales. It’s easy to see which month dominates overall sales.

3. Histogram – Distribution of Profits
profits = [2500,3000,3500,5000,6000,4500,6200,7000,6400,8000,7500,9500]

plt.hist(profits, bins=6, color='lightgreen', edgecolor='black')
plt.title("Profit Distribution")
plt.xlabel("Profit Range (₹)")
plt.ylabel("Frequency")
plt.show()
 

Why use Histogram:
A histogram helps analyze the distribution of continuous data (like profit values) — showing how often profits fall in certain ranges

4. Line Plot – Relationship Between Advertisement Spend and Sales
ad_spend = [1500,1700,1900,2100,2500,2000,2600,3000,2800,3300,3100,4000]

plt.plot(ad_spend, sales, marker='o', linestyle='-', color='orange')
plt.title("Relationship Between Advertisement Spend and Sales")
plt.xlabel("Advertisement Spend (₹)")
plt.ylabel("Sales (₹)")
plt.show()
 
Why use Line Plot:
A line plot is perfect for showing trends or relationships between two continuous variables (how ad spend affects sales).

5. Scatter Plot – Sales vs Customers
customers = [200,240,300,400,420,390,440,480,460,500,470,550]

plt.scatter(customers, sales, color='red')
plt.title("Sales vs Number of Customers")
plt.xlabel("Customers")
plt.ylabel("Sales (₹)")
plt.show()
 
Why use Scatter Plot:
Scatter plots are best to study correlation between two numerical variables — here, as customers increase, sales also rise.
