from graph_tool.all import *
from social_networks.analysis.make_graph import MakeGraph


def homophily (g, prop):
    repub = 0
    dem = 0
    count = 0
    hcount = 0
    # Get distribution of vertices based on property
    for v in g.vertices():
        if prop[v] == 'Republican':
            repub += 1
        else:
            dem += 1

    rprob = repub/g.num_vertices()
    dprob = dem/g.num_vertices()
    print('probability for republican vertex: {}'.format(rprob))
    print('probability for democratic vertex: {}'.format(dprob))

    # Get average for graph (2 * rprob * dprob)
    avg = (2 * rprob * dprob)

    # For each edge, determine the prop value of each vertex
    for edge in g.get_edges():
        # If not same, add 1 to counter
        if prop[edge[0]] != prop[edge[1]]:
            #print("source: {},{} Target: {},{}".format(g.vp.name[edge[0]], prop[edge[0]], g.vp.name[edge[1]], prop[edge[1]]))
            count += 1
        else:
            hcount +=1
    print('total heterogeneous edges = {} | Total homo edges = {} | Total edges = {}'.format(count, hcount, len(g.get_edges())))

    # If counter/total_edges less than average, homophily is exhibited
    print("Homophily Info: Average({}) | Actual({})".format(avg, count/len(g.get_edges())))

#make the graph
maker = MakeGraph()
g = maker.g

#print graph information
print("In degree: {0} | Out degree: {1} | Total degree: {2}".format(vertex_average(g, deg="in")[0], vertex_average(g, deg="out")[0], vertex_average(g, deg="total")[0]))
homophily(g, g.vp.years)
print("num vertices:{}".format(g.num_vertices()))
print("global clustering (coefficient,std deviation) {}".format(global_clustering(g)))

#graph formatting
vprops = {'anchor': 0, 'pen_width': 0.2, 'font_size': 8, 'size': 10}
eprops = {'pen_width': 0.4, 'color': [255,255,255, 0.5]}
color = g.vp.color

#draw nested model graph
state = minimize_nested_blockmodel_dl(g)
draw_hierarchy(state,
               bg_color=[0, 0, 0, 1],
               vertex_fill_color=color,
               vertex_color=color,
               output="graphs/nested_model_test.png",
               size=5)


pos = sfdp_layout(g, groups=g.vp.cluster)

#draw clustering graph
graph_draw(g, pos=pos,
            vprops=vprops, eprops=eprops,
            output_size=(500, 500),
            vertex_fill_color=color,
            vertex_color=color,
            bg_color=[0, 0, 0, 1],
            output="graphs/clustering_test.png")


#minimum spanning tree settings
tree_map = min_spanning_tree(g)
u = GraphView(g, efilt=tree_map)
pos = arf_layout(g)

#draw min spanning tree
graph_draw(u, pos=pos,
            vprops=vprops, eprops=eprops,
            output_size=(500, 500),
            vertex_fill_color=color,
            vertex_color=color,
            bg_color=[0, 0, 0, 1],
            output="graphs/min_spanning_tree_test.png")