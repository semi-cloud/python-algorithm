# 위와 아래 숫자들의 집합이 같도록 최대 몇개의 숫자를 뽑을 수 있는가

def dfs(n):  # 사이클 찾기
    temp = []
    visit = [False for _ in range(N + 1)]
    st = [[n, 1, n]]
    visit[n] = True

    while st:
        v, cnt, prev = st.pop()  # 탐색 시작 노드를 기억
        temp.append(v)

        for node in graph[v]:  # 이웃 노드 체크
            if v == node and cnt == 1: return temp, cnt  # 시작 노드와 이웃 노드가 같은 경우
            if prev == node: return temp, cnt   # 시작 노드와 그 이후 노드가 같다면 종료

            if not visit[node]:
                visit[node] = True
                st.append([node, cnt + 1, prev])
    return [], 0    # 사이클이 발생하지 않은 경우

N = int(input())
graph = [list() for _ in range(N+1)]
res = 0
res_num = []

for i in range(1, N+1):
    num = int(input())
    graph[i].append(num)

for j in range(1, N + 1):
    if j not in res_num:   # 이미 결과 집합에 없을때 탐색 진행
        arr, total = dfs(j)
        res += total       # 사이클 개수 모두 더하기
        res_num.extend(arr)

print(res)
res_num.sort()
for num in res_num:
    print(num)