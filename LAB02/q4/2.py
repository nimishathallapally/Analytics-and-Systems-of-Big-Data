from graphviz import Digraph
import os

dot = Digraph(comment="S&P 500 Hierarchy", format="png")

# Add nodes
dot.node("A", "S&P 500\n$24.37T")
dot.node("B", "Technology\n$8.137T")
dot.node("C", "Communications Equipment\n$390.8B")
dot.node("D", "Cisco Systems\n$213.7B")

# Edges
dot.edge("A", "B")
dot.edge("B", "C")
dot.edge("C", "D")

# Add other branches
dot.edge("A", "Services")
dot.edge("A", "Consumer Goods")
dot.edge("B", "Applications")
dot.edge("B", "Telecom Services")
dot.edge("B", "Internet Information Providers")
dot.edge("B", "Business Software & Services")
dot.edge("C", "Qualcomm")
dot.edge("C", "Hewlett Packard Enterprise")
dot.edge("C", "Motorola")
dot.edge("B", "Harris Corporation")
dot.edge("B", "Juniper Networks")

# Save and render
os.makedirs("output", exist_ok=True)
dot.render("output/hierarchy", view=True)
