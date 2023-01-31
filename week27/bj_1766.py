# 먼저 푸는 것이 좋은 문제는 먼저 풀고, 그 다음 순서는 쉬운 문제(위상 정렬 + 최소 힙)

def bfs():
    q = []  # 최소 힙 생성

    for i in range(1, N+1):
        if indegree[i] == 0:
            heappush(q, i)

    while q:  # 모든 정점을 돌 때까지 반복
        v = heappop(q)   # 진입 차수가 0 인 것들 중에 최소값 꺼내기
        print(v, end=" ")

        for n in graph[v]:  # 이웃 노드들 진입 차수 차감
            indegree[n] -= 1
            if indegree[n] == 0:      # 힙에 진입 차수가 0인 것들만 넣으면 더 쉬운 문제가 앞에 와야 하는 조건까지 적용 가능
                heappush(q, n)

import sys
from heapq import heappush, heappop

N, M = map(int, input().split())
orders = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
indegree = [0 for _ in range(N+1)]
graph = [[] for _ in range(N+1)]

for a, b in orders:
    graph[a].append(b)
    indegree[b] += 1

bfs()
