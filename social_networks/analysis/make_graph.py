from graph_tool.all import *
from social_networks.database_controller import *


class MakeGraph:
    def __init__(self, database="data", collection_name="current_congress_with_data"):
        self.reader = ReadFromDatabase(database, collection_name)
        self.cursor = self.reader.read_raw_data()
        self.g = Graph()
        self.g.add_vertex(self.cursor.count())
        self.add_vertex_property('string', 'name')
        self.add_vertex_prop_val('name')
        self.cursor.rewind()
        self.add_vertex_property('string', 'user')
        self.add_vertex_prop_val('user')
        self.cursor.rewind()
        self.add_vertex_property('string', 'party')
        self.add_vertex_prop_val('party')
        self.cursor.rewind()
        self.add_vertex_property('vector<double>', 'color')
        self.add_vertex_prop_val('color')
        self.cursor.rewind()
        self.add_vertex_property('int32_t', 'cluster')
        self.add_vertex_prop_val('cluster')
        self.cursor.rewind()
        self.add_vertex_property('string', 'district')
        self.add_vertex_prop_val('district')
        self.cursor.rewind()
        self.add_vertex_property('string', 'state')
        self.add_vertex_prop_val('state')
        self.cursor.rewind()
        self.add_vertex_property('string', 'years')
        self.add_vertex_prop_val('years')
        self.cursor.rewind()
        self.add_graph_edges()

    def add_vertex_property(self, prop_type, prop_name):
        # add username property map
        prop = self.g.new_vertex_property(prop_type)
        self.g.vertex_properties[prop_name] = prop

    def add_vertex_prop_val(self, prop_value):
        # add names to each vertex
        for v in self.g.vertices():
            if prop_value == 'color':
                if self.cursor[self.g.vertex_index[v]]['party'] == 'Republican':
                    self.g.vertex_properties[prop_value][v] = (1, 0, 0, 1)
                else:
                    self.g.vertex_properties[prop_value][v] = (0, 0, 1, 1)
            elif prop_value == 'cluster':
                if self.cursor[self.g.vertex_index[v]]['party'] == 'Republican':
                    self.g.vertex_properties[prop_value][v] = 1
                else:
                    self.g.vertex_properties[prop_value][v] = 0
            else:
                self.g.vertex_properties[prop_value][v] = self.cursor[self.g.vertex_index[v]][prop_value]
            # print(self.g.vertex_properties['name'][v])

    def add_graph_edges(self):
        # create all edges
        for user in self.cursor:
            # v1 is the vertex where name = cursor['name']
            v1 = find_vertex(self.g, self.g.vp.user, user['user'])[0]
            for mention in user['user_mentions']:
                try:
                    # v2 is the vertex where name = mention
                    v2 = find_vertex(self.g, self.g.vp.user, mention)[0]
                except IndexError:
                    #print("Error: " + mention + " is not in the collection")
                    continue

                if self.g.vp.user[v1] != self.g.vp.user[v2]:
                    #print("adding edge between " + self.g.vp.user[v1] + " and " + self.g.vp.user[v2])
                    self.g.add_edge(v1, v2)
