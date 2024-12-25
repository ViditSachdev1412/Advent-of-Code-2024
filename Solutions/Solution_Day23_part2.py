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

def bron_kerbosch(R, P, X, network, cliques):
    if not P and not X:
        cliques.append(R)
    while P:
        v = P.pop()
        bron_kerbosch(R.union([v]), P.intersection(network[v]), X.intersection(network[v]), network, cliques)
        X.add(v)

def find_largest_clique(network):
    nodes = set(network.keys())
    cliques = []
    bron_kerbosch(set(), nodes, set(), network, cliques)
    max_clique = max(cliques, key=len)
    return max_clique

def generate_password(clique):
    return ",".join(sorted(clique))

file_path = 'Datasets/dataset_day23.txt'
connections = read_input(file_path)
network = parse_input(connections)
largest_clique = find_largest_clique(network)
password = generate_password(largest_clique)
print("Password to get into the LAN party:", password)