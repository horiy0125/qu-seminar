
o = open("./input.txt")
lines = o.readlines()

N, M = list(map(int, lines[0].split()))

adjacency_list = []


for line in lines[1:]:
    from_index, to_index, capacity = list(map(int, line.split()))

    edge = [len(adjacency_list[to_index]), from_index, to_index, capacity]
    rev_edge = [len(adjacency_list[from_index]), to_index, from_index, 0]

    print(adjacency_list[0])
    print(adjacency_list[1])
    adjacency_list[to_index].append(edge)
    adjacency_list[from_index].append(rev_edge)


print(len(adjacency_list[0]))
