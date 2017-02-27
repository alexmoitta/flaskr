import random, copy
#data = open("/Users/alex/GitHub/coursera-algorithms-analysis/progAssignement4/workdir/teste_pequeno.txt","r")
base_dir = "/Users/alex/GitHub/coursera-algorithms-analysis/progAssignement4/workdir/"
#name_file = "_f370cd8b4d3482c940e4a57f489a200b_kargerMinCut.txt"
name_file = "teste_pequeno.txt"
full_name_file = base_dir + name_file
data = open(full_name_file,"r")
G = {}
for line in data:
    if line != "\n":
        lst = [int(s) for s in line.split()]
        G[lst[0]] = lst[1:]

def choose_random_key(G):
    v1 = random.choice(list(G.keys()))
    v2 = random.choice(list(G[v1]))
    return v1, v2

def karger(G):
    length = []
    while len(G) > 2:
        v1, v2 = choose_random_key(G)
        G[v1].extend(G[v2])
        for x in G[v2]:
            G[x].remove(v2)
            G[x].append(v1)
        while v1 in G[v1]:
            G[v1].remove(v1)
        del G[v2]
    for key in G.keys():
        length.append(len(G[key]))
    return length[0]

def operation(n):
    i = 0
    count = 10000
    while i < n:
        data = copy.deepcopy(G)
        min_cut = karger(data)
        if min_cut < count:
            count = min_cut
        i = i + 1
    return count


print(operation(100))