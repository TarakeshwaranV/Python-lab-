ad_spend = [1500,1700,1900,2100,2500,2000,2600,3000,2800,3300,3100,4000]

plt.plot(ad_spend, sales, marker='o', linestyle='-', color='orange')
plt.title("Relationship Between Advertisement Spend and Sales")
plt.xlabel("Advertisement Spend (₹)")
plt.ylabel("Sales (₹)")
plt.show()
