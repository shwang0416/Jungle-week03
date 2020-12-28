# [백준] https://www.acmicpc.net/problem/1260 DFS와 BFS
import sys

# input
sys.stdin = open('test/01.txt')
N, M, V = list(map(int, sys.stdin.readline().split()))
N += 1  # N은 1부터 시작하므로
visited = [False]*N
arr = [[0]*N for _ in range(N)]     #0으로 초기화 된 row ,col 모두 N까지 존재하는 이차원 리스트
que = []
for i in range(M):
    x, y=list(map(int, sys.stdin.readline().split()))
    arr[x][y] = 1
    arr[y][x] = 1


# ------------------------------------------------- DFS
def dfs(v):

    visited[v] = True
    print(v, end=' ')
    for i in range(N):
        if arr[v][i] == 1 and not visited[i]:
            dfs(i)

dfs(V)
print()
# ------------------------------------------------- BFS


def bfs(V):
    visited = [False] * N
    visited[V] = True
    que.append(V)

    while len(que) != 0:
        b = que.pop(0)
        print(b, end=' ')
        for j in range(N):
            if arr[b][j] == 1 and not visited[j]:
                que.append(j)
                visited[j] = True
bfs(1)