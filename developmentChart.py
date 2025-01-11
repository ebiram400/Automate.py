import matplotlib.pyplot as plt
import networkx as  nx

# Create a directed graph
G = nx.DiGraph()

# Define roles and their connections
roles = {
    'Idea Owner': [],
    'Product Owner': ['Idea Owner'],
    'Product Manager': ['Product Owner'],
    'R&D': ['Product Manager'],
    'Designer': ['R&D'],
    'Backend Developer': ['Designer'],
    'Frontend Developer': ['Designer'],
    'DevOps': ['Backend Developer', 'Frontend Developer'],
    'QA': ['DevOps']
}

# Add nodes and edges to the graph
for role, sub_roles in roles.items():
    G.add_node(role)
    for sub_role in sub_roles:
        G.add_edge(sub_role, role)

# Draw the graph
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', arrows=True)
plt.title('Development Cycle Roles and Responsibilities')

# Save the graph to a file
plt.savefig('./development_cycle_roles.png')
plt.show()