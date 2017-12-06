from graph_tool.all import *
from social_networks.database_controller import *


class MakeGraph:
    def __init__(self, database="data", collection_name="congress_map_trimmed"):
        self.reader = ReadFromDatabase(database, collection_name)
        self.cursor = self.reader.read_raw_data()
        self.g = Graph()
        self.g.add_vertex(self.cursor.count())
        self.add_vertex_property('string', 'user_name')
        self.add_vertex_prop_val()
        self.cursor.rewind()
        self.add_graph_edges()

    def add_vertex_property(self, prop_type, prop_name):
        # add username property map
        prop = self.g.new_vertex_property(prop_type)
        self.g.vertex_properties[prop_name] = prop

    def add_vertex_prop_val(self):
        # add names to each vertex
        for v in self.g.vertices():
            self.g.vp.user_name[v] = self.cursor[self.g.vertex_index[v]]['user']
            # print(self.g.vertex_properties['user_name'][v])

    def add_graph_edges(self):
        # create all edges
        for user in self.cursor:
            # v1 is the vertex where name = cursor['user']
            v1 = find_vertex(self.g, self.g.vp.user_name, user['user'])[0]
            for mention in user['user_mentions']:
                try:
                    # v2 is the vertex where name = mention
                    v2 = find_vertex(self.g, self.g.vp.user_name, mention)[0]
                except IndexError:
                    print("Error: " + mention + " is not in the collection")
                    continue

                if self.g.vp.user_name[v1] != self.g.vp.user_name[v2]:
                    # print("adding edge between " + self.g.vp.user_name[v1] + " and " + self.g.vp.user_name[v2])
                    self.g.add_edge(v1, v2)
