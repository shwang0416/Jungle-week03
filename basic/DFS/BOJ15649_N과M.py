# [백준] https://www.acmicpc.net/problem/15649 N과 M(1)
# 자연수 N과 M이 주어졌을 때, 1부터 N까지의 자연수 중 중복없이 M개를 고른 수열을 모두 출력
# DFS, 백트래킹 기초 문제

import sys

sys.stdin = open('BOJ15649.txt')
N, M = list(map(int, sys.stdin.readline().split()))
flag = [False]*(N+1)        # 1부터 N까지의 수에대해 각각을 방문했는지 표시하는 리스트
num = [0]*M

def put():
    for i in range(M):
        print(num[i], end=' ')
    print()


def dfs(index):
    # 모두 채웠다면 : 출력
    if index == M:
        put()
    # 플래그가 있는지 체크
    else:
        for i in range(1, N+1):
            if flag[i]:
                continue
            else:
            # else: 플래그를 세운다 => dfs(n다음) => 플래그 회수
                flag[i] = True
                num[index] = i
                dfs(index+1)
                flag[i] = False

dfs(0)