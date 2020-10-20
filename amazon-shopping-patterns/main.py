import itertools, math
from collections import defaultdict

def minimum(products_nodes, products_edges, edges):
    ans = math.inf
    graph = defaultdict(lambda:set())
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])

    for A,B in edges:     #O(N)
        cur = 0
        cs = graph[A] & graph[B]   #O(M)
        for C in cs:    #O(M)
            if C != A and C != B:
                ans = min(ans, (len(graph[A])-2) + (len(graph[B])-2) + (len(graph[C])-2))

    return ans

products_nodes = 6
products_edges = 6
edges = [[1,2],[2,4],[2,5],[3,5],[4,5],[5,6]]
print("minimum is: ", minimum(products_nodes, products_edges, edges))
