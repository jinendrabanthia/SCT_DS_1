import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Data
data = {
    "Country": [
        "India", "China", "United States", "Indonesia", "Pakistan",
        "Nigeria", "Brazil", "Bangladesh", "Russian Federation", "Ethiopia"
    ],
    "Population (Thousands)": [
        1450935.79, 1408975.00, 340110.99, 283487.93, 251269.16,
        232679.48, 211998.57, 173562.36, 143533.85, 132059.77
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert to millions for better readability
df["Population (Millions)"] = df["Population (Thousands)"] / 1000

# Set seaborn style for modern look
sns.set_theme(style="whitegrid")

# Create the bar chart
plt.figure(figsize=(12, 6))
barplot = sns.barplot(
    x="Population (Millions)", 
    y="Country", 
    data=df, 
    palette="viridis",
    hue="Country",
    legend=False
)

# Add titles and labels
plt.title("Top 10 Most Populous Countries in 2024", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("Population (Millions)", fontsize=12)
plt.ylabel("Country", fontsize=12)

# Add data labels on the bars
for p in barplot.patches:
    width = p.get_width()
    plt.text(
        width + 20, # Offset slightly
        p.get_y() + p.get_height() / 2,
        f"{width:,.0f}M",
        ha="left", 
        va="center",
        fontsize=10
    )

# Adjust layout
plt.tight_layout()

# Save the plot
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "population_bar_chart.png")
plt.savefig(output_path, dpi=300, bbox_inches="tight")
print(f"Plot saved successfully to {output_path}")
