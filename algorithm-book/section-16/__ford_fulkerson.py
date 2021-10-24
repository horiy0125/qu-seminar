
o = open("./input.txt")
lines = o.readlines()

N, M = list(map(int, lines[0].split()))

adjacency_list = []
for _ in range(N):
    adjacency_list.append([])


for line in lines[1:]:
    from_index, to_index, capacity = list(map(int, line.split()))

    edge = [len(adjacency_list[to_index]), from_index, to_index, capacity]
    rev_edge = [len(adjacency_list[from_index]), to_index, from_index, 0]

    adjacency_list[to_index].append(edge)
    adjacency_list[from_index].append(rev_edge)


def ford_fulkerson():
    result = 0

    while True:
        flow = check_minimum_capacity()
        if flow == 0:
            return result
        else:
            result += flow


def check_minimum_capacity():
    return 0


def run_flow(apex_index: int, edge_index: int, quantity: int):
    rev_edge_index, from_index, to_index, capacity = list(
        map(int, adjacency_list[apex_index][edge_index]))

    adjacency_list[from_index][edge_index][3] = capacity - quantity
    adjacency_list[to_index][rev_edge_index][3] = adjacency_list[to_index][rev_edge_index][3] + quantity
