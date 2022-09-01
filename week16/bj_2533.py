# 모든 개인이 새로운 아이디어를 수용하기 위하여 필요한 최소 얼리 어답터의 수를 구하기

import sys
sys.setrecursionlimit(10 ** 9)

def func(x):
    visited[x] = True
    dp[x][1] = 1          # 해당 노드가 얼리 어답터 => 1로 초기화

    for val in d[x]:      # 방문 하지 않은 인접 자식 노드 검사
        if not visited[val]:
            func(val)           # 자식 노드에 대해 재귀 탐색
            dp[x][1] += min(dp[val][0], dp[val][1])      # 부모 노드가 얼리 아답터인 경우, 자식이 얼리 아답터일 경우와 아닐 경우 중 최소깂 더하기
            dp[x][0] += dp[val][1]         # 부모 노드가 얼리 아답터가 아닐 경우 자식이 얼리 아딥터 일때의 값을 모두 더하기


N = int(sys.stdin.readline())
d = [[] for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N+1)]   # 2차원 배열
visited = [False for _ in range(N+1)]     # 방문을 기록할 배열

for i in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    d[u].append(v)
    d[v].append(u)

func(1)
print(min(dp[1][0], dp[1][1]))




