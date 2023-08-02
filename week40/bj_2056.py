# 모든 작업을 완료하기 위해 필요한 최소 시간
# 선행 관계가 없으면 동시 수행, 선행 관계가 있다면 먼저 수행 필요
# 위상 정렬: 선행 작업이 n개 라면 진입 차수 통해 뒤로 미룰 수 있음
# 10000 * 100 => 1000000

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    res = 0
    q = deque([])
    visit = [False for _ in range(N+1)]

    # 각 루트 노드 부터 검사(진입 차수 0)
    for i in range(N+1):
        if indegree[i] == 0:
            q.append([i, times[i]])  # 진입 차수, 해당 작업이 끝나는 시간
            visit[i] = True

    while q:
        v, end_time = q.popleft()
        res = max(res, end_time)   # 가장 늦게 끝나는 시점이 모든 작업이 완료된 시간

        for node in works[v]:      # 이웃 노드들에 대해 진입 차수 감소
            indegree[node] -= 1
            dp[node] = max(dp[node], end_time)  # 선행 노드 중 가장 늦게 끝나는 시간 저장(필수)

            if indegree[node] == 0 and not visit[node]:
                visit[node] = True
                q.append([node, dp[node] + times[node]])
    return res

N = int(input())  # 10000
works = [list() for i in range(N+1)]
indegree = [-1] + [0 for _ in range(N)]
times = [0 for _ in range(N+1)]
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):  # 후 선
    time, m, *later = map(int, input().split(" "))
    if m != 0:
        for l in later:
            works[l].append(i)
            indegree[i] += 1   # 진입 차수 계산
    times[i] = time

print(bfs())
