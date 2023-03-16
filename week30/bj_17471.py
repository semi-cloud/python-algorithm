# 두 선거구에 포함된 인구의 차이의 최솟값 찾기
from collections import deque

def connect_bfs(arr, flag):
    visit = [False for _ in range(N+1)]  # 해당 배열에 체크가 되어 있다면 패스하고 진행
    q = deque([arr[0]])
    visit[arr[0]] = True
    while q:
        n = q.popleft()
        for v in graph[n]:     # 인접 노드 탐색 후 큐에 추가
            if not visit[v] and check[v] == flag:  # 방문하지 않았거나 같은 구역인 노드로만 이동 가능
                visit[v] = True
                q.append(v)

    for a in arr:   # 연결이 되어 있지 않다면 visit 배열 중에 방문하지 않은 노드가 존재
        if not visit[a]:
            return False
    return True

def solution_dfs(idx):  # 인구 수를 애초에 함수의 인자로 넘기면서 더해주기
    global ans
    if idx == N+1:    # 모든 노드의 구역을 분배 했다면
        arr1 = [idx for idx, c in enumerate(check) if c == 1]
        arr2 = [idx for idx, c in enumerate(check) if c == 2]
        if len(set(check)) == 3 and connect_bfs(arr1, 1) and connect_bfs(arr2, 2):   # 그래프 탐색으로 각 구역의 노드가 연결되어 있다면 가능한 방법
            people1 = sum([people[idx] for idx, c in enumerate(check) if c == 1])
            people2 = sum([people[idx] for idx, c in enumerate(check) if c == 2])
            ans = min(ans, abs(people1 - people2))          # 인구 수 차이의 최솟값 업데이트
        return

    for i in range(idx, N+1):  # 방문 체크를 하지 않아야 되돌아와서 해당 위치의 값을 2로 바꾼 후 다시 1, 2 분열 수행
        check[i] = 1           # 해당 노드가 1, 2번 구역으로 들어가는 모든 경우
        solution_dfs(i + 1)
        check[i] = 2
        solution_dfs(i + 1)

N = int(input())   # 10
graph = [[] for _ in range(N+1)]
people = [0] + list(map(int, input().split()))  # 인구 수
check = [0 for _ in range(N+1)]
ans = int(1e9)

temp = 0
for i in range(1, N+1):
    cnt, *node = map(int, input().split())  # 인접한 구역 수, 인접 구역 번호
    if cnt == 0:
        temp += 1

    for n in node:
        graph[i].append(n)
        graph[n].append(i)

if temp >= 2 and N > 2:   # 총 구역이 3개 이상이고 인접하지 않은 구역이 2개 이상 존재하면 2개로 나눌 수 없으므로 불가능
    print(-1)
else:
    solution_dfs(1)
    print(ans)



# def solution_dfs(idx, people1, people2):  # 인구 수를 애초에 함수의 인자로 넘기면서 더해주기
#     global ans
#     if idx == N+1:    # 모든 노드의 구역을 분배 했다면
#         arr1 = [idx for idx, c in enumerate(check) if c == 1]
#         arr2 = [idx for idx, c in enumerate(check) if c == 2]
#         if len(set(check)) == 3 and connect_bfs(arr1, 1) and connect_bfs(arr2, 2):   # 그래프 탐색으로 각 구역의 노드가 연결되어 있다면 가능한 방법
#             print(arr1, arr2, people1, people2)
#             ans = min(ans, abs(people1 - people2))          # 인구 수 차이의 최솟값 업데이트
#         return
#
#     for i in range(idx, N+1):  # 방문 체크를 하지 않아야 되돌아와서 해당 위치의 값을 2로 바꾼 후 다시 1, 2 분열 수행
#         check[i] = 1           # 해당 노드가 1, 2번 구역으로 들어가는 모든 경우
#         solution_dfs(i + 1, people1 + people[i], people2)
#         check[i] = 2
#         solution_dfs(i + 1, people1, people2 + people[i])
