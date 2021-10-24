class Edge:
    def __init__(self, rev: int, from_index: int, to_index: int, cap: int):
        self.rev = rev
        self.from_index = from_index
        self.to_index = to_index
        self.cap = cap


class Graph:
    def __init__(self, size: int):
        self.size = size
        self.adjacency_list = []

        for _ in range(size):
            self.adjacency_list.append([])

    def add_edge(self, from_index: int, to_index: int, capacity: int):
        from_apex = self.adjacency_list[from_index]
        to_apex = self.adjacency_list[to_index]

        edge = Edge(len(to_apex), from_index, to_index, capacity)
        rev_edge = Edge(len(from_apex), to_index, from_index, 0)

        self.adjacency_list[from_index].append(edge)
        self.adjacency_list[to_index].append(rev_edge)

    def run_flow(self, apex_index: int, edge_index: int):
        self.adjacency_list[apex_index][apex_index]
    #    self.adjacency_list[edge.from_index][edge.]
    #     rev_edge = self.adjacency_list[edge.to_index][edge.rev]


o = open("./input.txt")
lines = o.readlines()

N, M = list(map(int, lines[0].split()))

graph = Graph(N)

for line in lines[1:]:
    from_index, to_index, capacity = list(map(int, line.split()))
    graph.add_edge(from_index, to_index, capacity)
