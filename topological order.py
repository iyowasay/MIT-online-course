from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # topological sort using the concept of DFS
    def topologicalSortUtil(self, v, visited, stack):
        visited[v] = True

        # print(self.graph)
        # print(visited)
        for i in self.graph[v]:
            if visited[i] is False:
                self.topologicalSortUtil(i, visited, stack)
                print(stack)

        stack.insert(0, v)

    def topologicalSort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if visited[i] is False:
                self.topologicalSortUtil(i, visited, stack)

        print(stack)

    # topological sort using in-degree of vertices
    def topologicalSort2(self):

        in_degree = [0] * self.V
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)
        cnt = 0
        top_order = []
        while queue:

            u = queue.pop(0)
            top_order.append(u)
            # Iterate through all neighbouring nodes
            # of dequeued node u and decrease their in-degree
            # by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                if in_degree[i] == 0:
                    queue.append(i)

            cnt += 1
        # Check if there was a cycle
        if cnt != self.V:
            print("There exists a cycle in the graph")
        else:
            print(top_order)


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topologicalSort()
g.topologicalSort2()



