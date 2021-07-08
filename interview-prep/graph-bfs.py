def bfs(graph, startnode):
    seen, queue = set([startnode]), [startnode]
    while queue:
        vertex = queue[0]
        queue.pop(0)
        print(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)

gdict = { "a" : set(["b","c"]),
         "b" : set(["a", "d"]),
         "c" : set(["a", "d"]),
         "d" : set(["e"]),
         "e" : set(["a"])
         }

bfs(gdict, "a")
