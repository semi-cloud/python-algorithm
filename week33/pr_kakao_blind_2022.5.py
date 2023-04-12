# 완전 탐색 + 백트래킹 + DFS => 중복되는 경우의 수로 인해 정해는 아님(시간 초과)

# 어려웠던 부분
# 한 경로로 가는 것이 아님이 판명이 나면, 다시 루트로 돌아와 거쳐서 다른 경로로 갔다가 양을 만나고 다시 못갔던 경로로 가야함
# 하지만 굳이 양방향 그래프를 이용해 루트 노드로 돌아가지 않고, 부모 노드를 방문 + 자식 노드를 방문하지 않은 경우의 노드를 매 재귀 마다 탐색해서 가면 됌
# 이미 방문해서 양이나 늑대를 만난 정점은 몇 명을 만났었나의 개수만 중요하지 아무 상관이 X(0 -> 1 -> 0 -> 8 (X) / 0 -> 1 -> 8 (O) )

# 내가 갈림길을 선택한 그 상황(상태)에서 재귀가 돌아가니까 양 개수는 여러 개의 경우 중에 가장 최대로 만날 수 있는 경우의 수로 갱신 필요
# 재귀는 언젠간 해당 상태(문맥)가 종료될 꺼고 그러면 다음 컨텍스트 시작을 위해 방문은 반드시 초기화 필요

max_sheep = 0
def solution(info, edges):
    global max_sheep
    N = len(info)
    graph = [[] for _ in range(N)]
    visit = [False for _ in range(N)]

    for x, y in edges:  # 양방향 그래프로 부모로 다시 올라가 탐색 할 필요 X(재귀 호출 횟수만 증가)
        graph[x].append(y)

    visit[0] = True
    def dfs(sheep, wolf):
        global max_sheep

        if sheep <= wolf: return   # 양보다 늑대 개수가 이상이 되면 잘못된 경로
        max_sheep = max(max_sheep, sheep)  # 모을 수 있는 양의 개수의 최대값 갱신

        for n in range(len(visit)):  # 매번 모든 엣지들을 탐색하면서 검사
            if not visit[n]: continue  # 부모 노드가 방문 되었고 자식 노드가 방문 되지 않은 경우를 찾아서 그 정점 부터 탐색

            for v in graph[n]:
                if visit[v]: continue  # 자식 노드가 이미 방문 했다면 패스

                visit[v] = True
                if info[v] == 0:
                    dfs(sheep + 1, wolf)  # 양을 만나는 경우
                elif info[v] == 1:
                    dfs(sheep, wolf + 1)  # 늑대를 만나는 경우
                visit[v] = False    # 양과 늑대 상관 없이 해당 경우의 수가 끝나면 돌아가는 길 모두 방문 해제
    dfs(1, 0)
    return max_sheep
