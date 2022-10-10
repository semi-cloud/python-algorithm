# 특정건물을 가장 빨리 지을 때까지 걸리는 최소시간을 알아내는 프로그램

from collections import defaultdict
from collections import deque


T = int(input())
for i in range(T):
    q = deque()
    build = defaultdict(list)
    N, K = map(int, input().split())          # 건물 개수, 순서 규칙 개수 : 1000, 100,000
    time = list(map(int, input().split()))    # 각 건물당 건설에 걸리는 시간
    in_degree = [0 for _ in range(N+1)]  # 진입 차수 배열
    dp = [0 for _ in range(N+1)]  # 0 1 2 3

    for _ in range(K):
        n, v = map(int, input().split())
        build[n].append(v)      # 건설 순서
        in_degree[v] += 1     # 진입 차수

    W = int(input())            # 건설 해야 할 건물의 번호

    for idx, degree in enumerate(in_degree):      # 진입 차수가 0 인 정점을 모두 큐에 삽입
        if degree == 0:
            q.append(idx)
            dp[idx] = time[idx-1]   # DP 시작 배열 초기화

    while q:
        n = q.popleft()
        for v in build[n]:
            in_degree[v] -= 1
            dp[v] = max(dp[v], dp[n] + time[v-1])   # depth 별로 최댓값을 구하는게 아니라 노드별로 구하기

            if in_degree[v] == 0:
                q.append(v)
    print(dp[W])