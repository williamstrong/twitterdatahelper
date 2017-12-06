from graph_tool.all import *
from social_networks.analysis.make_graph import MakeGraph

maker = MakeGraph()
g = maker.g

# attempt at weighting the graph
# pos = sfdp_layout(g)
pos = arf_layout(g)

tree_map = min_spanning_tree(g)
print(tree_map)
vert_list = find_edge(g, tree_map, 1)
print(vert_list)

vprops = {'anchor': 0, 'pen_width': 0.2}
eprops = {'pen_width': 0.4}
graph_draw(g, pos=pos, vertex_font_size=8,
           vprops=vprops, eprops=eprops,
           output_size=(1000, 1000), output="graphs/graph.png")
