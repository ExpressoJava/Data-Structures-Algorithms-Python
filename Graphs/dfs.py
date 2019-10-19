"""
           0
          / \
         1   2 
        /   / \
       3   4   5
          /
         6
"""
vertextList = ['0', '1', '2', '3', '4', '5', '6']
edgeList = [(0, 1), (0, 2), (1, 0), (1, 3), (2, 0), (2, 4),
            (2, 5), (3, 1), (4, 2), (4, 6), (5, 2), (6, 4)]
graphs = (vertextList, edgeList)


def dfs(graph, start):
    graph = vertextList, edgeList
    visitedVertex = []
    stack = [start]
    adjacenyList = [[] for vertex in vertextList]

    for edge in edgeList:
        adjacenyList[edge[0]].append(edge[1])

    while stack:
        current = stack.pop()
        for neighbor in adjacenyList[current]:
            if not neighbor in visitedVertex:
                stack.append(neighbor)
        visitedVertex.append(current)
    return visitedVertex


print(dfs(graphs, 0))
