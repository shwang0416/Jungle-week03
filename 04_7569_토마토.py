# [백준] https://www.acmicpc.net/problem/7569 토마토(3차원)
# BFS '최소 날짜'

import sys
import collections

sys.stdin = open('test/04.txt')

M, N, H = list(map(int, sys.stdin.readline().split()))
box = []
que = collections.deque([])
visited = [[[0] * M for _ in range(N)] for _ in range(H)]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]
dh = [-1, 1, 0, 0, 0, 0]
m = 0

for k in range(H):
    temp =[]
    for i in range(N):
        tmp = list(sys.stdin.readline().split())
        for j in range(M):
            if '-1' == tmp[j]:
                visited[k][i][j] = -1
            elif '1' == tmp[j]:
                que.append([k, i, j])
                visited[k][i][j] = 1
        temp.append(tmp)
    box.append(temp)


def bfs():
    global m
    while len(que) != 0:
        h, y, x = que.popleft()

        for i in range(6):
            nh = h + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < N and 0 <= nx < M and 0 <= nh < H:
                if visited[nh][ny][nx] == 0 and box[nh][ny][nx] == '0':
                    box[nh][ny][nx] = 1
                    visited[nh][ny][nx] = visited[h][y][x] + 1
                    m = m if m > visited[nh][ny][nx] else visited[nh][ny][nx]
                    que.append([nh, ny, nx])


    for h in range(H):
        for n in range(N):
            if 0 in visited[h][n]:
                return -1
    else:
        return m-1


for h in range(H):
    for n in range(N):
        if '0' in box[h][n]:
            print(bfs())
            exit(0)
else:
    print(0)