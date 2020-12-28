# [백준] https://www.acmicpc.net/problem/11725 트리의 부모찾기
# DFS

import sys
sys.setrecursionlimit(100000)
sys.stdin = open('test/08.txt')

N = int(sys.stdin.readline().strip())

llist = [[] for _ in range(N+1)]
parent = [-1]*(N+1)
visited = [False]*(N+1)

for _ in range(N-1):
    a, b = list(map(int, sys.stdin.readline().split()))
    llist[a].append(b)
    llist[b].append(a)

visited[0] =True


def recur(n):
    visited[n] = True
    for m in llist[n]:
        if not visited[m]:
            parent[m] = n
            recur(m)
    else:
        return
recur(1)

for p in parent[2:]:
    print(p)






