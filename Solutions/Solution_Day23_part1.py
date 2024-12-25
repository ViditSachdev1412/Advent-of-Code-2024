def read_input(file_path):
    with open(file_path, 'r') as file:
        connections = [line.strip() for line in file.readlines()]
    return connections

def parse_input(connections):
    network = {}
    for connection in connections:
        comp1, comp2 = connection.split('-')
        if comp1 not in network:
            network[comp1] = set()
        if comp2 not in network:
            network[comp2] = set()
        network[comp1].add(comp2)
        network[comp2].add(comp1)
    return network

def find_triangles(network):
    triangles = set()
    for comp1 in network:
        for comp2 in network[comp1]:  
            if comp1 < comp2:
                for comp3 in network[comp2]:
                    if comp3 in network[comp1] and comp2 < comp3:
                        triangles.add(tuple(sorted([comp1, comp2, comp3])))
    return triangles

def filter_triangles_with_t(triangles):
    filtered_triangles = [triangle for triangle in triangles if any(comp.startswith('t') for comp in triangle)]
    return filtered_triangles

file_path = 'Datasets/dataset_day23.txt'
connections = read_input(file_path)
network = parse_input(connections)

triangles = find_triangles(network)

triangles_with_t = filter_triangles_with_t(triangles)

for triangle in triangles_with_t:
    print(triangle)

print("Number of triangles with at least one 't':", len(triangles_with_t))