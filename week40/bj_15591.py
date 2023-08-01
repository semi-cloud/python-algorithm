# 동영상과 USADO가 K 값 이상인 동영상 추천 => 몇 개인지 구하기
# 플로이드 워샬로 하면 O(N^3) => N이 500개 이하로 설정되어야 하는데 5000이므로 시간 초과

from collections import deque

# 바로 연결되어 있는 것들은 최소값 상관 X
def bfs(start, target):
    cnt = 0
    visit = [False for _ in range(N+1)]
    q = deque([[start, float("inf")]])
    visit[start] = True

    while q:
        n, weight = q.popleft()

        if weight >= target:  # k 값 이상으로 큰 경우 추천
            if weight != float("inf"):
                cnt += 1

            # 맨 처음 유사도가 애초에 k 미만이라면 해당 노드와 연결된 모든 하위 노드도 탐색할 필요 X(최소값이므로)
            for new, new_wight in graph[n]:  # 이웃 노드 값
                if not visit[new]:
                    visit[new] = True
                    min_dist = min(weight, new_wight)  # 직전 까지 만나는 모든 간선들의 최소값 구하기
                    q.append((new, min_dist))
    return cnt


N, Q = map(int, input().split(" "))   # 5,000, 5,000
graph = [list() for _ in range(N+1)]
record = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N-1):
    a, b, w = map(int, input().split(" "))
    graph[a].append((b, w))
    graph[b].append((a, w))

for i in range(Q):
    k, v = map(int, input().split(" "))
    print(bfs(v, k))  # 시작 노드

# 시간 초과 코드
# # 미리 각 노드 간의 USADO 저장(시간 효율)
# for i in range(1, N+1):  # 5000
#     for j in range(i+1, N+1):  # 5000
#         if record[i][j] == 0 and record[j][i] == 0:  # USADO가 정해져 있지 않으면 새로 구하기
#             bfs(i, j)
#
# for i in range(Q):  # 5000
#     cnt = 0
#     k, v = map(int, input().split(" "))
#
#     for j in range(1, N + 1):
#         if j == v: continue
#         if record[v][j] >= k and record[j][v] >= k:  # v와의 USADO가 k 이상인 영상 추천
#             cnt += 1
#     print(cnt)
