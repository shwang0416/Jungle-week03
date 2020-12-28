# [백준] https://www.acmicpc.net/problem/2178 미로 탐색
import sys

sys.stdin = open('test/03.txt')
N, M = list(map(int,sys.stdin.readline().split()))

board = []
visited = [[0]*M for i in range(N)] #앞이 안쪽 배열, 뒤가 바깥 배열
que = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 100000

for n in range(N):
    board.append(list(sys.stdin.readline().strip()))


def bfs(y,x):
    global result

    que.append([y,x])
    visited[y][x] = 1
    while len(que) != 0:
        y, x = que.pop(0)
        for i in range(4):

            nx = dx[i]+x
            ny = dy[i]+y
            if 0 <= nx < M and 0 <= ny < N:
                if visited[ny][nx] == 0 and board[ny][nx] == '1':
                    visited[ny][nx] = visited[y][x] + 1 #visited를 append하기전에 꼭 체크해야함
                    if nx == M-1 and ny == N-1:
                        result = min(result, visited[ny][nx])
                    que.append([ny, nx])
    return result


print(bfs(0,0))

