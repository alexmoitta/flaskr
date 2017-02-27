import random
#import csv
#import string
#from string import Formatter
import re


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

def remove_edge_by_node_names(edges, old_node_name_0, old_node_name_1, new_node_name):
    edges_size = len(edges)
    new_edges = []
    for i in range(0,edges_size,1):

        if edges[i][0] == old_node_name_0 and edges[i][1] == old_node_name_1:
            print "Edge " + str(edges[i][0]) + " " + str(edges[i][1]) + " will not be replicated\n"
            continue

        if edges[i][0] == old_node_name_1 and edges[i][1] == old_node_name_0:
            print "Edge " + str(edges[i][0]) + " " + str(edges[i][1]) + " will not be replicated\n"
            continue

        if edges[i][0] == old_node_name_0:
            print "Edge " + str(edges[i][0]) + " " + str(edges[i][1]) + " will not be replicated\n"
            print "a new item will be created, instead."
            #I have to create a new item
            new_edges.append((new_node_name,edges[i][1]))
            continue

        if edges[i][1] == old_node_name_0:
            print "Edge " + str(edges[i][0]) + " " + str(edges[i][1]) + " will not be replicated\n"
            print "a new item will be created, instead."
            #I have to create a new item
            new_edges.append((edges[i][0],new_node_name))
            continue

        if edges[i][0] == old_node_name_1:
            print "Edge " + str(edges[i][0]) + " " + str(edges[i][1]) + " will not be replicated\n"
            print "a new item will be created, instead."
            #I have to create a new item
            new_edges.append((new_node_name,edges[i][1]))
            continue

        if edges[i][1] == old_node_name_1:
            print "Edge " + str(edges[i][0]) + " " + str(edges[i][1]) + " will not be replicated\n"
            print "a new item will be created, instead."
            #I have to create a new item
            new_edges.append((edges[i][0],new_node_name))
            continue

        #replicate the current element as is, because it doesnt have any relation with the nodes merged
        new_edges.append((edges[i][0],edges[i][1]))

    return new_edges



def pick_random_edge(edges):
    random.seed()
    print "Maximum is: " + str (len(edges)-1)
    return random.randint(0,len(edges)-1)

#this code assumes that the list is ordered
def deduplicate(edges):
    new_edges = []

    edges.sort() #the list MUST be sorted

    if len(edges) == 1:
        return edges #same value
    else:

        edge_size = len(edges)
        pivot_value_0 = edges[0][0]
        pivot_value_1 = edges[0][1]
        new_edges.append(edges[0])
        x = 1 #first element will be the pivot. So we start comparing the second one
        while x < edge_size:
            current_value_0 = edges[x][0]
            current_value_1 = edges[x][1]
            if pivot_value_0 == current_value_0 and pivot_value_1 == current_value_1:
                print "this item already exists. Ignore it. Don't replicate"
            else:
                #change values in pivot value
                pivot_value_0 = current_value_0
                pivot_value_1 = current_value_1
                new_edges.append(edges[x])
            x += 1

    return new_edges


def merge_nodes(graph_network,edges,random_edge):
    old_name_0 = edges[random_edge][0]
    old_name_1 = edges[random_edge][1]
    if old_name_0 < old_name_1:
        new_node_name = old_name_0 + old_name_1
    else:
        new_node_name = old_name_1 + old_name_0
    print "New node name: " + new_node_name

    #cleaning edges
    edges = remove_edge_by_node_names(edges, old_name_0, old_name_1, new_node_name)
#    edges = deduplicate(edges)


    #cleaning graph
#    del graph_network[old_name_0]
#    del graph_network[old_name_1]
    return edges

def create_edges_by_line(node_list,edges):
    size_node_list = len(node_list)
    if size_node_list < 2:
        return
    else:
        origin_edge = node_list[0]
        x = 1
        while x < size_node_list:
            edges.append((str(origin_edge),str(node_list[x])))
            x += 1
    return


def load_graph_edges():
    edges = []
    workdirectory = "/Users/alex/GitHub/coursera-algorithms-analysis/progAssignement4/workdir"
    name_of_file = "teste_pequeno.txt"
    #name_of_file = "_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt"
    graph_file = workdirectory + "/" + name_of_file
    #outputnameofile = workdirectory + "/" + "outputorderednumbers"

    filepointer = open (graph_file,mode='r')
    print filepointer
    lines = filepointer.readlines()

    for line in lines:
        if line != "\n":
#            string_parsed = formatter.parse(line)
#            node_list = [int(s) for s in line.split() if s.isdigit()]
            node_list = [str(s) for s in line.split() if s.isalnum()]
            create_edges_by_line(node_list,edges)


    filepointer.close()
    return edges




graph_network = {"1" : ["2", "3"],
                 "2" : ["1","3"],
                 "3" : ["1","2"]}



#edges = []
#edges.append(("3","1"))
#edges.append(("3","2"))
#edges.append(("1","2"))
#edges.append(("1","3"))
#edges.append(("2","1"))
#edges.append(("2","3"))

edges = []

edges = load_graph_edges()

orig_edges = list(edges)

print "edges: before merge"
for i in range(0,len(edges),1):
    print edges[i]

while len(edges) > 6:
    random_edge = pick_random_edge(edges)
    print "Edge id randomly selected: " + str(random_edge)
    print "Those nodes will be merged: " + edges[random_edge][0] + " " + edges[random_edge][1]

    edges = merge_nodes(graph_network,edges,random_edge)

    print "edges: after merge"
    for i in range(0,len(edges),1):
        print edges[i]


print "Terminou"













