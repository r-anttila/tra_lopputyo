WHITE = 0
GREY = 1
BLACK = 2


class Graph:
    def __init__(self, verts, edges, destination):
        self.verts = verts
        self.edges = edges
        self.edges.sort(key=lambda x: x[1])
        self.adj_list = self.generate_adj_list()
        self.destination = destination

    def generate_adj_list(self):
        adj_list = {}
        for edge in self.edges:
            edge_start = edge[0][0]
            edge_end = edge[0][1]

            try:
                adj_list[edge_start].append([edge_end, edge[1]])
            except KeyError:
                adj_list[edge_start] = [[edge_end, edge[1]]]

            try:
                adj_list[edge_end].append([edge_start, edge[1]])
            except KeyError:
                adj_list[edge_end] = [[edge_start, edge[1]]]
        return adj_list

    def __str__(self):
        return str(self.edges)


class DisjointSet:

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        self.parent[x] = x
        self.rank[x] = 0

    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

    def __str__(self):
        return str(self.parent)


def graph_from_file(path_to_file):
    verts = []
    edges = []

    with open(path_to_file, 'r') as file:
        lines = file.readlines()

        # Poistetaan ensimmäinen rivi, sillä sitä ei tarvita tässä implementoinnissa
        lines.pop(0).split()
        destination = int(lines.pop())

        for line in lines:
            source_dest_weight = line.split()
            source = int(source_dest_weight[0])
            dest = int(source_dest_weight[1])
            weight = int(source_dest_weight[2])

            if source not in verts:
                verts.append(source)
            if dest not in verts:
                verts.append(dest)
            edges.append([[source, dest], weight])

    return Graph(verts, edges, destination)


def kruskal(graph):
    ds = DisjointSet()
    A = []

    for vertex in graph.verts:
        ds.make_set(vertex)

    for edge in graph.edges:
        u = edge[0][0]
        v = edge[0][1]

        if ds.find(u) != ds.find(v):
            A.append([[u, v], edge[1]])
            ds.union(u, v)

    return A


def max_weight_with_bfs(graph, start):
    color = {}
    d = {}
    p = {}
    weight = {}

    for u in graph.verts:
        color[u] = WHITE
        d[u] = float("inf")
        p[u] = None
        weight[u] = 0

    d[start] = 0
    color[start] = GREY
    queue = []
    queue.append(start)

    while queue:
        u = queue.pop()
        for v in graph.adj_list[u]:
            if color[v[0]] == WHITE:
                color[v[0]] = GREY
                d[v[0]] = d[u] + 1
                p[v[0]] = u
                weight[v[0]] = v[1]
                queue.append(v[0])
        color[u] = BLACK

    return get_max_weight(start, graph.destination, d, p, weight)


def get_max_weight(start, dest, dist, pred, weight):
    u = dest
    weights = []
    if dist[dest] != float("inf"):
        while pred[u] != None:
            weights.append(weight[u])
            u = pred[u]
    return max(weights)


def run(path_to_test_file):
    graph = graph_from_file(path_to_test_file)

    graph.edges = kruskal(graph)
    graph.adj_list = graph.generate_adj_list()

    print(max_weight_with_bfs(graph, 1))


if __name__ == "__main__":
    run('./testidata/graph_large_testdata/graph_ADS2018_500.txt')
