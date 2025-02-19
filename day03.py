def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A')+i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited) #graph에서 i,j칸이 참이면 j행을 탐색한다, 근데 j행이 한번도 방문한 적이 없으면 감

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

visited = [0] * len(graph) #len(graph) = 5
dfs(graph, 0, visited)