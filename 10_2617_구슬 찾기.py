# [백준] https://www.acmicpc.net/problem/2617 구슬 찾기
# [참고] https://jaimemin.tistory.com/950

import sys
sys.stdin = open('test/10.txt')

N, M = list(map(int, sys.stdin.readline().split()))
mid = (N+1)//2 -1

bigger =[[] for _ in range(N+1)]
smaller =[[] for _ in range(N+1)]
bigger_than =[[0,0] for _ in range(N+1)] # 본인보다 큰 수 기록 # deque 사용??
smaller_than = [[0,0] for _ in range(N+1)] # 본인보다 작은 수 기록
visitedB = [False for _ in range(N+1)]
visitedS = [False for _ in range(N+1)]


#  --- input ------------
for i in range(M):
    a, b = list(map(int, sys.stdin.readline().split()))
    bigger[b].append(a)
    smaller[a].append(b)
# -----------------------


def find_bigger(start):
    cnt = 1
    visitedB[start] = True
    for i in range(M):
        if visitedB[i] == False:
            cnt += find_bigger(bigger[i])
    return cnt


def find_smaller(n):
    cnt = 1
    visitedS[n] = True
    for i in range(M):
        if visitedS[i] == False:
            cnt += find_smaller(smaller[i])
    return cnt



ans = 0
for i in range(1, N):  # 자기보다 큰 수 & 작은 수 구하기
    visitedB = [False for _ in range(N+1)]
    visitedS = [False for _ in range(N+1)]
    b = find_bigger(i)
    s = find_smaller(i)
    if b > mid or s > mid:
        ans += 1

print(ans)


