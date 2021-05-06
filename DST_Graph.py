
class GraphNode():
    # Vertex of a graph G(V, E)
    def __init__(self, v_key):
        self.vertex_id = v_key
        self.Adj = {}           # {Other vertex_id: Weight of the Other vertex_id}
        pass

    def AddAdj(self, other_key, edg_weight):
        self.Adj[other_key] = edg_weight

    def GetAdjWeight(self, v_key):
        return self.Adj[v_key]

    def GetVID(self):
        return self.vertex_id

    def GetAdjIDs(self):
        return self.Adj.keys()

    def __str__(self):
        return str(self.vertex_id) + ' connected to: ' + str([x.vertex_id for x in self.Adj])


class Graph():
    def __init__(self):
        # self.VertexDict = v_key_lst
        self.VertexDict = {}
        pass

    def AddNode(self, v_key):
        self.VertexDict[v_key] = GraphNode(v_key)

    def AddEdge(self, v_key_1, v_key_2, weight):
        if v_key_1 not in self.VertexDict:
            self.AddNode(v_key_1)
        if v_key_2 not in self.VertexDict:
            self.AddNode(v_key_2)
        if v_key_1 not in self.VertexDict:
            V = GraphNode(v_key_1)
            if v_key_2 not in V.GetAdjIDs():
                V.AddAdj(v_key_2, weight)
            self.VertexDict[v_key_1] = V

    def AdjustGraph(self, v_key, other_v_lst):
        V = GraphNode(v_key)
        [V.AddAdj(other_v[0], other_v[1]) for other_v in other_v_lst]               # other_v = [other_v_key, other_v_weight]
        self.VertexDict[v_key] = V

    def GetNode(self, v_key):
        return self.VertexDict[v_key]

    def GetWeight(self, v_key, v_key_other):
        return self.VertexDict[v_key].GetAdjWeight(v_key_other)

    def GetGraphIDs(self):
        return self.VertexDict.keys()

    def Visualize(self):
        """
        TODO: 可视化为邻接矩阵
        :return:
        """
        pass
