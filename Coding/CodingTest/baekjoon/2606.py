n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]


def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)


for i in range(m):
    x, y = map(int, input().split())

    graph[x].append(y)
    graph[y].append(x)


visited = [False]*(n+1)

dfs(graph, 1, visited)

print(graph)
print(visited.count(True)-1)
