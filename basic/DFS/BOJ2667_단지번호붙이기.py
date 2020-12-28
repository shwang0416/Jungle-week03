# [백준] https://www.acmicpc.net/problem/2667 단지번호 붙이기
# DFS, BFS 둘 다 가능할 듯??
import sys

sys.stdin = open('BOJ2667.txt')
N = int(input())
board = []
visited =[[False]*N for i in range(N)]
ans = []

for i in range(N):
    board.append(list(input()))
cnt = 0

def dfs(x,y):
    global cnt

    if x >= 0 and y >= 0 and x < N and y < N and visited[y][x] == False:
        visited[y][x] = True
        tmp = board[y][x]
        if tmp == '1':
            cnt += 1
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x+1, y)
        return cnt


for i in range(N):
    for j in range(N):
        cnt = 0
        result = dfs(i,j)
        if result and result > 0:
            ans.append(result)
list.sort(ans)
l = len(ans)
print(l)
for a in ans:
    print(a)