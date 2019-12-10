
class Graph:
    def __init__(self, verts, adj, destination):
        self.verts = verts
        self.adj = adj
        self.destination = destination
        


def graph_from_file(path_to_file):
    verts = []

    with open(path_to_file, 'r') as file:
        lines = file.readlines()
        no_verts_and_edges = lines.pop(0).split()
        no_verts = int(no_verts_and_edges[0])
        no_edges = int(no_verts_and_edges[1])
        destination = int(lines.pop())

        for line in lines:
            source_and_dest = line.split()
            source = int(source_and_dest[0])
            dest = int(source_and_dest[1])

            if source not in verts:
                verts.append(source)
            if dest not in verts:
                verts.append(dest)

        adj = [None]*len(verts)

        for line in lines:
            source_dest_weight = line.split()
            source = int(source_dest_weight[0])
            dest = int(source_dest_weight[1])
            weight = int(source_dest_weight[2])

            if adj[source-1] != None:
                adj[source-1].append((dest, weight))
            else:
                adj[source-1] = [(dest, weight)]

            if adj[dest-1] != None:
                adj[dest-1].append((source, weight))
            else:
                adj[dest-1] = [(source, weight)]

    return Graph(verts, adj, destination)

def dijkstra(graph):
    start = graph.verts[0]
    start_index = start - 1

    dist = [None]*len(graph.verts)

    for i in range(len(dist)):
        dist[i] = [float("inf")]
        dist[i].append([start])
    
    dist[start_index][0] = 0
    
    queue = [i for i in range(len(graph.verts))]
    seen = set()

    while len(queue) > 0:
        min_height = float("inf")
        min_index = None

        for n in queue:
            if dist[n][0] < min_height and n + 1 not in seen:
                min_height = dist[n][0]
                min_index = n
                min_vert = n + 1

        queue.remove(min_index)
        seen.add(min_vert)

        if graph.destination in seen:
            print("Found")

        for (vert, weight) in graph.adj[min_index]:
            vert_index = vert - 1
 
            if min_height < dist[vert_index][0]:
                dist[vert_index][0] = min_height
                dist[vert_index][1] = list(dist[min_index][1])
                dist[vert_index][1].append(vert)

    print(dist)

if __name__ == "__main__":
    graph = graph_from_file('./testidata/graph_testdata/graph_ADS2018_10_1.txt')
    dijkstra(graph)