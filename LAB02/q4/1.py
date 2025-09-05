import plotly.express as px
import pandas as pd
import os

# Hierarchical data with values
data = dict(
    ids=[
        "S&P 500", 
        "Technology", "Services", "Consumer Goods",
        "Applications", "Communications Equipment", "Telecom Services",
        "Internet Information Providers", "Business Software & Services",
        "Cisco Systems", "Qualcomm", "Hewlett Packard Enterprise",
        "Motorola", "Harris Corporation", "Juniper Networks"
    ],
    parents=[
        "", 
        "S&P 500", "S&P 500", "S&P 500",
        "Technology", "Technology", "Technology",
        "Technology", "Technology",
        "Communications Equipment", "Communications Equipment", "Communications Equipment",
        "Telecom Services", "Internet Information Providers", "Business Software & Services"
    ],
    values=[
        24370, 8137, 5000, 5000,   # top level (dummy sums except S&P/Tech real)
        1000, 390.8, 1200, 900, 1100,   # mid-level
        213.7, 100, 77, 60, 50, 40     # leaf nodes
    ]
)

# Build sunburst (hierarchical chart)
fig = px.sunburst(
    data,
    ids="ids",
    parents="parents",
    values="values",
    title="Hierarchical Tree of S&P 500 Example"
)

# Save
os.makedirs("output", exist_ok=True)
fig.write_image("output/hierarchy.png")

# fig.show()
