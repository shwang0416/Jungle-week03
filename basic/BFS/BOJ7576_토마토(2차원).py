# [백준] https://www.acmicpc.net/problem/7576 토마토(2차원)
# BFS '최소 날짜'
import sys
import collections

sys.stdin = open('basic/BOJ7576.txt')

M, N = list(map(int, sys.stdin.readline().split()))
box = []
que = collections.deque([])
visited = [[0] * M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
day = 0
m = 0
idx = []

for i in range(N):
    tmp = list(sys.stdin.readline().split())
    for j in range(M):
        if '-1' == tmp[j]:
            visited[i][j] = -1
        elif '1' == tmp[j]:
            que.append([i, j])
            visited[i][j] = 1
    box.append(tmp)


def bfs():
    global m
    while len(que) != 0:
        y, x = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < N and 0 <= nx < M:
                if visited[ny][nx] == 0 and box[ny][nx] == '0':
                    box[ny][nx] = 1
                    visited[ny][nx] = visited[y][x] + 1
                    m = m if m > visited[ny][nx] else visited[ny][nx]
                    que.append([ny, nx])

    for n in range(N):
        if 0 in visited[n]:
            return -1
    else:
        return m-1


for n in range(N):
    if '0' in box[n]:
        print(bfs())
        exit(0)
else:
    print(0)
