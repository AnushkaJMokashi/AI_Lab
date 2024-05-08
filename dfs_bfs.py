def dfs(adjacency_matrix, v, visited):
    visited.append(v)
    print(v,end=" ")
    for i in range(len(adjacency_matrix)):
        if (i not in visited) and (adjacency_matrix[v][i]):
            dfs(adjacency_matrix,i,visited)

def bfs(adjacency_matrix, visited, queue):
    if not queue:
        return
    node = queue[0]
    queue = queue[1:]
    for i in range (len(adjacency_matrix)):
        if (i not in visited) and (adjacency_matrix[node][i]):
            visited.append(i)
            queue.append(i)
    bfs(adjacency_matrix,visited,queue)

node = int(input("ENTER NUMBER OF NODES: "))
adjacency_matrix = [[0 for i in range(node)] for i in range(node)]
for i in range(node):
    for j in range(i+1,node):
        check = input(f"IS EDGE PRESENT BETWEEN {i} and {j} (y/n): ")
        if check=='y' or check=='Y':
            adjacency_matrix[i][j] = adjacency_matrix[j][i] = 1

print("\n")
print("DFS = ",end='')
visited = []
dfs(adjacency_matrix,0,visited)
print("\n")

queue = [0]
visited = [0]
bfs(adjacency_matrix,visited,queue)
print("BFS = ",end='')
[print(i,end=' ')for i in visited]