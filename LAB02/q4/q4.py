import plotly.express as px
import pandas as pd
import os

# Fixed hierarchical data
data = {
    "Category": [
        "S&P 500", "Technology", "Services", "Consumer Goods",
        "Applications", "Communications Equipment", "Telecom Services",
        "Internet Information Providers", "Business Software & Services",
        "Cisco Systems", "Qualcomm", "Hewlett Packard Enterprise",
        "Motorola", "Harris Corporation", "Juniper Networks"
    ],
    "Parent": [
        "", "S&P 500", "S&P 500", "S&P 500",
        "Technology", "Technology", "Technology",
        "Technology", "Technology",
        "Communications Equipment", "Communications Equipment", "Communications Equipment",
        "Telecom Services", "Internet Information Providers", "Business Software & Services"
    ],
    # Only leaves need values
    "Value": [
        None, None, None, None,   # parent nodes
        None, None, None, None, None,   # mid-level nodes
        213.7, 150, 120, 80, 60, 50  # leaf values (fake numbers for demo except Cisco)
    ]
}

df = pd.DataFrame(data)

# Build TreeMap
fig = px.treemap(
    df,
    path=['Parent', 'Category'],
    values='Value',
    title="Hierarchical Treemap of S&P 500 Example",
    color='Value',
    color_continuous_scale='Blues'
)

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

# Save and show
fig.write_image("output/treemap.png")
fig.show()
print("Treemap saved to output/treemap.png")
