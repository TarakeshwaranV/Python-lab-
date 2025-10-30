import matplotlib.pyplot as plt
months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
sales = [12000,15000,18000,22000,25000,20000,27000,30000,28000,35000,32000,40000]

plt.pie(sales, labels=months, autopct='%1.1f%%', startangle=90)
plt.title("Percentage Contribution to Annual Sales")
plt.show()
