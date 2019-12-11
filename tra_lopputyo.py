
class Graph:
    def __init__(self, verts, edges, destination):
        self.verts = verts
        self.edges = edges
        self.edges.sort(key=lambda x: x[1])
        self.destination = destination

    def __str__(self):
        return str(self.edges)


class SetElement:
    def __init__(self, content, rank, size):
        self.content = content
        self.parent = self
        self.rank = rank
        self.size = size

    def __str__(self):
        return str([self.content, self.parent.content])


class DisjointSet:

    def __init__(self):
        self.sets = []

    def make_set(self, x):
        if x not in self.sets:
            self.sets.append(SetElement(x, 0, 1))

    def find(self, x):
        root = x

        while root.parent.content != root.content:
            root = root.parent

        while x.parent != root:
            parent = x.parent
            x.parent = root
            x = parent

        return root

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return
        elif x_root.rank < y_root.rank:
            x_root, y_root = y_root, x_root

        y_root.parent = x_root
        if x_root.rank == y_root.rank:
            x_root.rank = x_root.rank + 1

    def __str__(self):
        return str(self.sets)


def graph_from_file(path_to_file):
    verts = []
    edges = []

    with open(path_to_file, 'r') as file:
        lines = file.readlines()
        no_verts_and_edges = lines.pop(0).split()
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
            edges.append(
                [[SetElement(source, 0, 1), SetElement(dest, 0, 1)], weight])
            edges.append(
                [[SetElement(dest, 0, 1), SetElement(source, 0, 1)], weight])

    return Graph(verts, edges, destination)


def kruskal(graph):
    ds = DisjointSet()
    A = []

    for vertex in graph.verts:
        ds.make_set(vertex)

    for item in ds.sets:
        print(item)

    for edge in graph.edges:
        u = edge[0][0]
        v = edge[0][1]

        if ds.find(u) != ds.find(v):
            A = A + [[u, v]]
            ds.union(u, v)

    for item in ds.sets:
        print(item)

    return A


if __name__ == "__main__":
    graph = graph_from_file(
        './testidata/graph_testdata/graph_ADS2018_10_1.txt')

    for item in kruskal(graph):
        print(item[0], item[1])
