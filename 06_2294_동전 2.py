# [백준] https://www.acmicpc.net/problem/2294 동전2
# 백준 분류에는 다이나믹 프로그래밍으로 되어있는데, 정글 분류 상에는 BFS 문제로 되어있다. (??)

# [다이나믹 프로그래밍(동적 계획법)이란??]
# => "기억하며 풀기"
# (https://syujisu.tistory.com/147 동적계획법(다이내믹~)과 분할정복의 차이)
# 한마디로, 다이내믹은 중복되는 결과값을 저장해뒀다가 더 큰 단위의 계산에서 재활용하고,
#         (=> 분할된 범위에서 시작해 범위 안까지 값을 저장해나감)
#           분할정복은 그렇지 않다.(애초에 중복되지 않는 부분이라 재활용이 안 될 경우에 분할정복을 쓴다)
#              (=> 구하고자하는 값에서 시작해 재귀로 분할)

import sys
sys.stdin = open('test/06.txt')

n, k = list(map(int,sys.stdin.readline().split()))
typeC = []


# 1부터 100개 이하의 동전을 사용해서 1부터 10000원 이하의 가치를 만든다. 동전값의 범위는 1부터 100000원
# (즉, k원을 초과하는 가치의 동전은 시험해 볼 필요 없음, 동전의 합이 100을 넘어가면 안됨)
for _ in range(n):
    v = int(sys.stdin.readline().strip())
    if v <= k:
        typeC.append(v)

# 아래의 코드는..
# min(typeC) <= k <= 10000 만 생각
anslist = [(k+1) for _ in range(k+1)]   # 동전의 최소개수가 될 수 없는 값으로 초기화(k+1개)
tmp = 0
for t in typeC:
    anslist[t] = 1      # 5원을 만드는 최소동전개수는 1개 (5원짜리!)

for i in range(k):
    a1 = anslist[i]
    if 1 <= a1 < k+1:
        for j in range(k):
            a2 = anslist[j]
            if a2 >= 1:
                tmp = i+j
                if tmp > k:
                    break
                else:
                    ans = min(anslist[tmp], a1 + a2)
                    anslist[tmp] = ans
ans = anslist.pop()
if ans == k+1:
    print(-1)
else:
    print(ans)