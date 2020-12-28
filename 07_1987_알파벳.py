# [백준] https://www.acmicpc.net/problem/1987 알파벳
# [참고] https://it-garden.tistory.com/272
# DFS, 백트래킹
import sys
sys.stdin = open('test/07.txt')
sys.setrecursionlimit(100000)
# input
Y, X = map(int, sys.stdin.readline().split())
alpha = [list(map(lambda x : ord(x)-65, sys.stdin.readline()))for i in range(Y)]
#     방문한 적이 없어야하고, 갖고 있지 않은 알파벳이어야 한다.
visited = [0 for _ in range(26)]
ans = 1
dy = [-1,0,1,0]
dx = [0,-1,0,1]


def find_len(y,x,cnt):
    visited[alpha[y][x]] = 1
    global ans
    ans = max(ans, cnt)

    # for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
    #     nx = dx+x
    #     ny = dy+y
    # 이거 대신에 dx dy 배열로 바꿨더니 시간초과가 안나고 통과됨!!
    for i in range(4):
        ny = y + dy[i]; nx = x + dx[i]

        if 0 <= nx < X and 0 <= ny < Y:
            if visited[alpha[ny][nx]] == 0:
                find_len(ny,nx,cnt+1)
                visited[alpha[ny][nx]] = 0

find_len(0,0,ans)
sys.stdout.write(str(ans))




