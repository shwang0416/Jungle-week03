# [백준] https://www.acmicpc.net/problem/3055 탈출

# 고슴도치가 비버의 굴로 가는 최단거리
# BFS 문제 => deque를 이용한다

import sys
import collections

sys.stdin = open('test/05.txt')

que = collections.deque([])     # map의 변화 과정을 저장할 덱
wque = collections.deque([])     # map의 변화 과정을 저장할 덱
map = []

# S: 고슴도치   D: 비버의 굴    *: 물    X: 돌
# v: 고슴도치의 시작좌표 (r, c)

R, C = list(sys.stdin.readline().split())
R = int(R)
C = int(C)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# input && map 세팅
for i in range(R):
    tmp = sys.stdin.readline().strip()
    tmp = list(tmp)

    if '*' in tmp:
        for j in range(C):
            if '*' == tmp[j]:
                wque.append([i,j])
    if 'S' in tmp:
        s = tmp.index('S')
        que.append([i, s])

    map.append(tmp)


# 진행상황 확인을 위한 print 함수
# def put():
#     for i in range(R):
#         for j in range(C):
#             print(map[i][j], end='')
#         print()
#     print()


def BFS():
    time = 0

    while len(que) != 0:

        wque_size = len(wque)
        for w in range(wque_size):
            y, x = wque.popleft()
            for i in range(4):
                wx = x + dx[i]
                wy = y + dy[i]
                if 0 <= wx < C and 0 <= wy < R and map[wy][wx] == '.':
                    map[wy][wx] = '*'
                    wque.append([wy, wx])

        que_size = len(que)
        for m in range(que_size):
            y, x = que.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < C and 0 <= ny < R:
                    if map[ny][nx] == 'D':
                        return time+1
                    elif map[ny][nx] == '.':    # .으로 남은 경우에만 진행
                        que.append([ny, nx])
                        map[ny][nx] = 'S'

        time += 1
    return 'KAKTUS'
print(BFS())