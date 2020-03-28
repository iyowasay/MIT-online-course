# Breadth first search - BFS
class Vertex1:
    def __init__(self, n):
        self.name = n
        self.color = 'black'  # black represents unvisited
        self.distance = 9999
        self.neighbors = list()

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph1:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex1) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + '  ' + str(self.vertices[key].distance))

    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'  # red represents visited
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1


g = Graph1()
a = Vertex1('A')
g.add_vertex(a)
g.add_vertex(Vertex1('B'))

for i in range(ord('A'), ord('K')):  # the range of the characters
    g.add_vertex(Vertex1(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.bfs(a)
g.print_graph()

print('-'*32)


# Depth first search - DFS
class Vertex2:
    def __init__(self, n):
        self.name = n
        self.color = 'black'  # black represents unvisited
        self.discovery = 0
        self.finish = 0
        self.neighbors = list()

    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph2:
    vertices = {}
    time = 0

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex2) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + '  ' + str(self.vertices[key].discovery) + '  ' + str(self.vertices[key].finish))

    def _dfs(self, vert):
        global time
        vert.color = 'red'  # red represents visited
        vert.discovery = time
        time += 1
        for v in vert.neighbors:
            if self.vertices[v].color == 'black':
                self._dfs(self.vertices[v])
        vert.color = 'blue'  # blue represent finished
        vert.finish = time
        time += 1

    def dfs(self, vertex):
        global time
        time = 1
        self._dfs(vertex)


g = Graph2()
a = Vertex2('A')
g.add_vertex(a)
g.add_vertex(Vertex2('B'))

for i in range(ord('A'), ord('K')):  # the range of the characters
    g.add_vertex(Vertex2(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']

for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.dfs(a)
g.print_graph()

# order = list()
x = [1, 2, 4]
y = [5, 7, 0]
order = x + y
print(order)







