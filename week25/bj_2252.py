# 일부 학생들의 키를 비교한 결과(정확한 키 수치 X)가 주어졌을 때, 줄 세우기(학생 번호는 1부터 시작)
# 문제의 조건에 선후 관계가 표현 : 위상 정렬(그래프 탐색을 이용한 정렬 방법)
# 그래프 간선의 일부 정보만 주어져도 나머지 노드들은 애초에 진입 차수가 0이므로 방문 가능

import sys
from collections import deque

def dfs():
    q = deque()
    for i in range(1, N + 1):  # 진입 차수가 0인 노드들에 대해 DFS 수행
        if indegree[i] == 0:  # 진입 차수가 0인 노드가 여러개 라면 답도 여러개
            q.append(i)

    # 만약 모든 원소를 방문 하기 전에 큐가 빈다면 사이클이 존재
    while q:
        node = q.pop()
        ans.append(node)

        for n in graph[node]:  # 인접한 노드 탐색
            indegree[n] -= 1   # 없는 간선이므로 진입 차수 감소

            # 차수를 감소 시켰는데 진입 차수가 0이 된다면 거기서부터 탐색
            if indegree[n] == 0:
                q.append(n)

N, M = map(int, input().split())  # N : 32000
graph = [[] for _ in range(N+1)]    # 그래프 연결 정보
indegree = [0 for _ in range(N+1)]  # 각 노드의 진입 차수 정보 사용
ans = []     # 줄 세우기 탐색 결과

if N == 1:
    print(M[0][0])
else:
    for i in range(M):    # 진입 차수 및 인접 노드 정보 초기화
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    dfs()
    print(" ".join(map(str, ans)))



# 1. 틀린 풀이
# 매번 순서가 갱신될 때마다 기존의 학생들도 순서가 한칸씩 밀리므로 계속 반영을 해줘야 하는데, 결국 모든 배열을 M번 만큼 탐색해야 하므로 O(N * M)
# ans = [(0, 0) for _ in range(N+1)]  # N개의 배열을 만들어 놓고 각 학생에 키 순서 번호를 매기기 => 나중에 순서 번호 기준으로 정렬 후 출력
# order = 1
# if N > 1:
#     # 1. 일부 학생 줄 세우기
#     for stu_a, stu_b in compares:     # M : 100,000
#         if ans[stu_a][1] > 0:  # 앞선 순서가 이미 이 전에 순서 갱신 기록이 있다면
#             order = ans[stu_a][1]   # 이전의 순서 부터 시작
#
#         if ans[stu_b][1] > 0:  # 뒤의 순서가 이 전에 순서 갱신 기록이 있다면
#             order = ans[stu_b][1]
#
#         ans[stu_a] = (stu_a, order)
#         ans[stu_b] = (stu_b, order + 1)
#         order += 2
#
#     # 2. 나머지 학생이 남는다면 줄 세우기(어디 들어가 던지 상관 X)
#     for i in range(1, N+1):
#         if ans[i] == 0:
#             ans[i] = (i, order)
#             order += 1
#
#     # 3. 순서대로 정렬
#     ans.sort(key=lambda x: x[1])
#     print(" ".join(map(str, map(lambda x: x[0], ans[1:]))))
# else:
#     print(M[0][0])









