import matplotlib.pyplot as plt

# Sort by distance for clean bar chart
sorted_df = df_2024.sort_values(by="DistanceFromWinnerProfile")

plt.figure(figsize=(12, 6))
bars = plt.bar(sorted_df["Team"], sorted_df["DistanceFromWinnerProfile"], color='skyblue')

# Add values on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.2, round(yval, 2), ha='center', fontsize=8)

plt.title("Distance from Average Stanley Cup Winner Profile (2024 Playoff Teams)")
plt.ylabel("Total Difference from Winner Stats")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()