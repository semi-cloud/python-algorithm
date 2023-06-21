# 가장 가까운 공통 조상 : 두 노드를 모두 자손으로 가지면서, 가장 가까이 있는 부모 노드

def dfs(n, visited):
    st = [n]
    visited[n] = True

    while st:
        v = st.pop()

        for node in graph[v]:
            if visited[node]:  # 다른 노드가 올라가면서 이미 방문 표시가 되어 있는 곳이 있다면 공통 조상
                return node
            else:
                visited[node] = True  # 한쪽이 부모를 따라 올라가면서 방문 표시를 하고
                st.append(node)
    return n


T = int(input())
for _ in range(T):
    N = int(input())  # 10,000
    graph = [list() for _ in range(N + 1)]

    for _ in range(N - 1):
        p, c = map(int, input().split(" "))
        graph[c].append(p)  # 자식 => 부모

    visit = [False for _ in range(N + 1)]
    x, y = map(int, input().split(" "))
    if x == y:
        print(dfs(x, visit))
    else:
        dfs(x, visit)
        print(dfs(y, visit))
