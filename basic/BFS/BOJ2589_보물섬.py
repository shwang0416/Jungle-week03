# [백준] https://www.acmicpc.net/problem/2589 보물섬

# L과 다른 L사이의 최단거리중 가장 먼 거리 찾기
# BFS로 풀기

import sys
# input
sys.stdin = open('BOJ2589.txt')
row, col = list(map(int, sys.stdin.readline().split()))
visited = [[0]*col for _ in range(row)]
board = []     #0으로 초기화 된 row ,col 모두 N까지 존재하는 이차원 리스트
cnt = 0
max_value = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(row):
    for j in range(col):
        tmp = sys.stdin.readline().strip()
        tmp = list(tmp)
        board.append(tmp)
que = []


def bfs(y, x):

    global cnt

    que.append([y,x])
    visited = [[0] * col for _ in range(row)]
    visited[y][x] = 1
    while len(que) != 0:
        y, x = que.pop(0)
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]
            if cy >= 0 and cy < row and cx >= 0 and cx < col:
                if board[cy][cx] == 'L' and visited[cy][cx] == 0:
                    que.append([cy, cx])
                    visited[cy][cx] = visited[y][x] + 1
                    cnt = max(cnt, visited[cy][cx])
    return cnt


for i in range(row):
    for j in range(col):
        if board[i][j] == 'L':
            cnt = bfs(i, j)
            max_value = max(max_value, cnt)
            cnt = 0
print(max_value-1)