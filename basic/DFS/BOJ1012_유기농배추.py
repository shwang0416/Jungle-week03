# [백준] https://www.acmicpc.net/problem/1012 유기농배추
# 단지번호 붙이기와 같은 문제
import sys
sys.setrecursionlimit(100000)
sys.stdin = open('BOJ1012.txt')

T = int(sys.stdin.readline().strip())   #testcase


def dfs(y, x):
    # 좌표가 범위 안이고 방문한 적 없다면
    if 0 <= y < N and 0 <= x < M and not flag[y][x]:
        flag[y][x] = True
        if board[y][x] == 1:
            for dx, dy in [(-1, 0), (1,0), (0,-1), (0,1)]:
                nx = x + dx
                ny = y + dy
                dfs(ny, nx)
            return True
    return False


for i in range(T):

    M, N, K = list(map(int, sys.stdin.readline().split()))  # 가로,세로,배추개수
    flag = [[False]*M for _ in range(N)]
    result = 0
    board = [[0]*M for _ in range(N)]
    for _ in range(K):
        xx, yy = list(map(int, sys.stdin.readline().split()))
        board[yy][xx] = 1

    for n in range(N):
        for m in range(M):
            if dfs(n,m):
                result += 1
    print(result)


