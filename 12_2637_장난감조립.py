# [백준] https://www.acmicpc.net/problem/2637 장난감 조립

import sys
import collections
sys.stdin = open('test/12.txt')


N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
a = [[] for _ in range(N+1)]            # 인덱스에 해당하는 간선들을 저장
inDegree = [0 for _ in range(N+1)]      # 진입차수 저장 (
que = collections.deque([])
ans = [[] for _ in range(N)]
d = [[0 for _ in range(N+1)]for _ in range(N+1)]     # 더해진 값을 저장
# 정렬 결과를 저장할 리스트
for i in range(M):
    x, y, k = list(map(int, sys.stdin.readline().split()))     #
    # x를 만드는데 y가 k개 필요한다!
    a[y].append([x, k]) # y에 [x를 만드는데 k개 필요] 저장
    inDegree[x] += 1


def sort():

    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if inDegree[i] == 0:
            que.append(i)
            d[i][i] = 1

    # 정렬이 완전히 수행되려면 정확히 N개의 노드를 방문해야한다.
    # (중간에 멈췄다면 순환적인 구조이므로 위상정렬 불가)
    while len(que) != 0:
        here = que.popleft()

        for tmp in a[here]:    # que에서 나온 부품이 필요한 파트에 ++해줌
            next = tmp[0]
            cost = tmp[1]
            # 1에 5에 쓸만큼을 더해줌
            for i in range(1,N+1):
                d[next][i] += cost * d[here][i]
            inDegree[next] -= 1
            if inDegree[next] == 0:
                que.append(next)

    for an in range(1,N):
        tmp = d[-1][an]
        if tmp != 0:
            print(an, end=' ')
            print(tmp)
sort()
