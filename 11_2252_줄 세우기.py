# [백준] https://www.acmicpc.net/problem/2252 줄 세우기
# [참고] https://www.youtube.com/watch?v=C8TuNuBqBPU 나동빈 유튜브
# 위상정렬 기초

# 1. 진입차수가 0인 정점을 미리 큐에 넣어둔다.
# 2. 정점을 큐에서 꺼내고 연결된 간선을 제거한 뒤 정리가 끝난 리스트에 넣는다.
# 3.

import sys
import collections
sys.stdin = open('test/11.txt')


N, M = list(map(int, sys.stdin.readline().split()))
a = [[] for _ in range(N+1)]            # 인덱스에 해당하는 간선들을 저장
inDegree = [0 for _ in range(N+1)]      # 진입차수 저장 (
que = collections.deque([])
ans = []                                 # 정렬 결과를 저장할 리스트
for i in range(M):
    b, c = list(map(int, sys.stdin.readline().split()))     #
    a[b].append(c)
    inDegree[c] += 1



def sort():

    # 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, N+1):
        if inDegree[i] == 0:
            que.append(i)

    # 정렬이 완전히 수행되려면 정확히 N개의 노드를 방문해야한다.
    # (중간에 멈췄다면 순환적인 구조이므로 위상정렬 불가)
    for _ in range(N):
        before = que.popleft()          # 1, 2
        ans.append(before)
        for tmp in a[before]:
            # tmp = a[before][j]
            inDegree[tmp] -= 1
            if inDegree[tmp] == 0:
                que.append(tmp)

    for an in ans:
        print(an, end=' ')
    print()

sort()