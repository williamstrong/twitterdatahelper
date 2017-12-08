from graph_tool.all import *
from social_networks.analysis.make_graph import MakeGraph

maker = MakeGraph()
g = maker.g

# attempt at weighting the graph
# pos = sfdp_layout(g)
pos = arf_layout(g)

tree_map = min_spanning_tree(g)
#print(tree_map)
vert_list = find_edge(g, tree_map, 1)
#print(vert_list)


print("In degree: {0} | Out degree: {1} | Total degree: {2}".format(vertex_average(g, deg="in")[0], vertex_average(g, deg="out")[0], vertex_average(g, deg="total")[0]))

vprops = {'anchor': 0, 'pen_width': 0.2, 'font_size': 8}
eprops = {'pen_width': 0.4}
color = g.vp.color
state = minimize_nested_blockmodel_dl(g)
draw_hierarchy(state,
               bg_color=[0, 0, 0, 1],
               vertex_fill_color=color,
               vertex_color=color,
               output="graphs/nested_model.png",
               size=5)

# graph_draw(g, pos=pos,
#             vprops=vprops, eprops=eprops,
#             output_size=(1000, 1000),
#             bg_color=[1.0, 2.0, 3.0, 4.0],
#             output="graphs/test.png")
