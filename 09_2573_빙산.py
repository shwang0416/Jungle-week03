# [백준] https://www.acmicpc.net/problem/2573 빙산

# DFS vs BFS 뭐가 유리??
# 빙하가 동시에 녹게 하는 방법이 고민스러운데 BFS가 맞아보임
# 근데 DFS로 표시되어있으니 일단 DFS로 도전
# => [이전높이, 현재높이]로 저장해뒀다가 해가 바뀌면 pop(0)?


# Q> 빙하가 두 덩어리로 나눠진 시점을 구하는 방법?
# A> 1년(while)동안 높이가 1이상인 빙하지점을 찾아서 dx dy 4방향이동으로 탐색했는데 방문하지 않은 빙하가 있다면 그 지점에서 스톱하면 될 듯
import sys
import copy
sys.setrecursionlimit(100000)
sys.stdin =open('test/09.txt')
N, M = list(map(int, sys.stdin.readline().split()))
# ice=[[[0] for _ in range(M)]for _ in range(N)]
ice = []
visited = [[True for _ in range(M)]for _ in range(N)]
points = [] #바뀐 빙하의 좌표저장


for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    ice.append(tmp)
ice_copy = copy.deepcopy(ice)
# 빙하 시작의 첫 좌표를 찾자


def find_start():        # 값이 0이 아닌 첫번째 좌표 찾기
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                return [i, j]

def set_visited():       # 0은 무조건 방문처리
    visited = [[True for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                visited[i][j] = False
    return visited


def check_visited():     # 하나라도 방문안했다면 False
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                return False
    return True


def check_ice():            # 0이 아닌 ice가 있는지 체크
    for i in range(N):
        for j in range(M):
            if ice[i][j] != 0:
                return False
    return True


def check(y, x):            # 해당 좌표에서 얼음이 얼마나 녹는지 리턴
    cnt = 0
    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
        nx = dx+x
        ny = dy+y
        if 0 <= nx < M and 0 <= y < N and ice[ny][nx] <= 0:  # 0이 아닌데 방문한 적 X
            cnt-=1
    return cnt


def dfs(y, x):
    visited[y][x] = True
    ice_copy[y][x] += check(y,x)
    if ice_copy[y][x] <= 0:
        ice_copy[y][x] = 0
    points.append([y, x])
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx = dx + x
        ny = dy + y
        if 0 <= nx < M and 0 <= y < N and not visited[ny][nx]:
            dfs(ny,nx)


start = find_start()
points.append(start)
year = -1
while True:
    if not check_visited():
        break
    elif check_ice():
        year = 0
        break
    # visited = [[False for _ in range(M)]for _ in range(N)]# 1년
    start = find_start()   # y, x
    visited = set_visited()
    points.clear()
    dfs(start[0],start[1])
    # print(visited)
    for p in points:
        py = p[0]
        px = p[1]
        ice[py][px] = ice_copy[py][px]
    # print(ice)
    year += 1

print(year)




