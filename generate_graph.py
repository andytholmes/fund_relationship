import networkx as nx
import matplotlib.pyplot as plt

# Example data
funds = {
    "Fund A": {"nav": 100, "strategy": "Equity"},
    "Fund B": {"nav": 150, "strategy": "Fixed Income"},
    "Fund C": {"nav": 200, "strategy": "Mixed"},
}

investments = [
    {"from": "Fund A", "to": "Fund B", "amount": 50},
    {"from": "Fund B", "to": "Fund C", "amount": 70},
    {"from": "Fund C", "to": "Fund A", "amount": 30},
]

# Create a graph
G = nx.DiGraph()

# Add nodes with NAV and strategy attributes
for fund, data in funds.items():
    G.add_node(fund, nav=data["nav"], strategy=data["strategy"])

# Add edges with investment amounts
for investment in investments:
    G.add_edge(
        investment["from"],
        investment["to"],
        amount=investment["amount"],
    )

# Generate positions for the graph
pos = nx.spring_layout(G, seed=42)

# Draw nodes with sizes based on NAV
node_sizes = [data["nav"] * 10 for _, data in G.nodes(data=True)]
node_colors = [hash(data["strategy"]) % 256 for _, data in G.nodes(data=True)]  # Encode strategy as colors

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, cmap=plt.cm.Set3, alpha=0.8)

# Draw edges with widths based on investment amount
edge_widths = [data["amount"] / 10 for _, _, data in G.edges(data=True)]
nx.draw_networkx_edges(G, pos, width=edge_widths, alpha=0.6, edge_color="gray")

# Add labels
nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")
edge_labels = {
    (u, v): f"${data['amount']}"
    for u, v, data in G.edges(data=True)
}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Add a legend for strategies
strategy_legend = {data["strategy"] for _, data in G.nodes(data=True)}
for i, strategy in enumerate(strategy_legend):
    plt.scatter([], [], color=plt.cm.Set3(i / len(strategy_legend)), label=strategy, s=100)
plt.legend(title="Strategy", loc="upper left", bbox_to_anchor=(1, 1))

# Display the graph
plt.title("Fund Investment and Strategies")
plt.show()
