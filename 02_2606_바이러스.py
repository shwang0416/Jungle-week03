# [백준] https://www.acmicpc.net/problem/2606 바이러스

# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서
# 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

# DFS에서, 만약 해당 노드를 탐색했다면 탐색한 노드는 방문했다는 표시를 해 두어야 다시 탐색하는 불상사가 없다.
#  => Flag

import sys

sys.stdin = open('BOJ2606.txt')
N = int(input()) + 1        # 컴퓨터 번호는 1부터 시작함
conn = int(input())
computer =[[0]*N for _ in range(N)]
visit =[False]*N

for _ in range(conn):
    x, y = list(map(int, input().split()))
    computer[x][y] = 1
    computer[y][x] = 1

cnt = 0


def dfs(start):
    global cnt
    global N

    visit[start] = True
    cnt +=1

    for i in range(N):
        if computer[start][i]==1 and visit[i]==False:
            dfs(i)


dfs(1)

print(cnt-1)        # 자기 자신 제외