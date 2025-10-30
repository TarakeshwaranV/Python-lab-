profits = [2500,3000,3500,5000,6000,4500,6200,7000,6400,8000,7500,9500]

plt.hist(profits, bins=6, color='lightgreen', edgecolor='black')
plt.title("Profit Distribution")
plt.xlabel("Profit Range (₹)")
plt.ylabel("Frequency")
plt.show()
