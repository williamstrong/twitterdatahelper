from graph_tool.all import *
from twitter_data.database_controller import *

reader = ReadFromDatabase("data", "congress_map_trimmed")
cursor = reader.read_raw_data()

g = Graph()
g.add_vertex(cursor.count())

#testing
# for user in cursor:
#     print(user)
# cursor.rewind()

#add username property map
name_prop = g.new_vertex_property("string")
g.vertex_properties['name'] = name_prop

#add names to each vertex
for v in g.vertices():
    g.vp.name[v] = cursor[g.vertex_index[v]]['user']
    #print(g.vertex_properties['name'][v])

cursor.rewind()

#create all edges
for user in cursor:
    #v1 is the vertex where name = cursor['user']
    v1 = find_vertex(g, g.vp.name, user['user'])[0]
    for mention in user['user_mentions']:
        try:
            # v2 is the vertex where name = mention
            v2 = find_vertex(g, g.vp.name, mention)[0]
        except IndexError:
            print("Error: " + mention + " is not in the collection")
            continue

        if g.vp.name[v1] != g.vp.name[v2]:
            print("adding edge between " + g.vp.name[v1] + " and " + g.vp.name[v2])
            edge = g.add_edge(v1, v2)

#attempt at weighting the graph
pos = sfdp_layout(g)

graph_draw(g, pos=pos, vertex_text=g.vertex_index, vertex_font_size=12,
            output_size=(1000, 1000), output="new-graph.png")



