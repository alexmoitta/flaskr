import random

#Karger min cut algorithm

#load the text file for each node and adjaceny
#create a dict with a list of items for each adjacency
#   for each node deleting
#       look for the id of the node in other nodes
#       replace the old node name by the merged name
#create a dict or tuple of edges (what will it be the key? I need a key able to be randomized)
#I shall try to test random first


def remove_edge_by_node_name(edges, node_name):
    edges_size = len(edges)
    new_edges = []
    for i in range(0,edges_size,1):
        if edges[i][0] == node_name or edges[i][1] == node_name:
            print "Edge " + str(edges[i][0]) + " " + str(edges[i][1]) + " will note be replicated\n"
        else:
            new_edges.append(edges[i])
    return new_edges

def remove_edge_by_node_names(edges, old_node_name_0, old_node_name_1):
    edges_size = len(edges)
    new_edges = []
    for i in range(0,edges_size,1):
        if edges[i][0] == old_node_name_0 or edges[i][1] == old_node_name_0:
            print "Edge " + str(edges[i][0]) + " " + str(edges[i][1]) + " will note be replicated\n"
        else:
            if edges[i][0] == old_node_name_1 or edges[i][1] == old_node_name_1:
                print "Edge " + str(edges[i][0]) + " " + str(edges[i][1]) + " will note be replicated\n"
            else:
                new_edges.append(edges[i])

    return new_edges



def pick_random_edge(edges):
    return random.randint(0,len(edges)-1)


def merge_nodes(graph_network,edges,random_edge):
    old_name_0 = edges[random_edge][0]
    old_name_1 = edges[random_edge][1]
    if old_name_0 < old_name_1:
        new_node_name = old_name_0 + old_name_1
    else:
        new_node_name = old_name_1 + old_name_0
    print "New node name: " + new_node_name


    #cleaning edges
    edges = remove_edge_by_node_names(edges, old_name_0, old_name_1)


    #cleaning graph
    del graph_network[old_name_0]
    del graph_network[old_name_1]





random.seed()

graph_network = {"1" : ["2", "3"],
                 "2" : ["1","3"],
                 "3" : ["1","2"]}



edges = []
edges.append(("1","2"))
edges.append(("1","3"))
edges.append(("2","1"))
edges.append(("2","3"))
edges.append(("3","1"))
edges.append(("3","2"))


print "graph: before merge"
print graph_network

print "edges: before merge"
for i in range(0,len(edges),1):
    print edges[i]


random_edge = pick_random_edge(edges)
print "Edge id randomly selected: " + str(random_edge)
print "Those nodes will be merged: " + edges[random_edge][0] + " " + edges[random_edge][1]


merge_nodes(graph_network,edges,random_edge)


print "graph: after merge"
for i in range(0,len(graph_network),1):
    print graph_network[1]

print "edges: after merge"
for i in range(0,len(edges),1):
    print edges[i]


print "after deletion node 3"

print edges[3][1]
edges = remove_edge_by_node_name(edges,"3")

for i in range(0,len(edges),1):
    print edges[i]














