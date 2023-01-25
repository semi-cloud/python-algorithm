# 1. 다익스트라(오직 양의 간선) : O(ELogV), 벨만-포드(음의 간선 존재) : O(VE)
# 인접 정점까지 오는데 필요한 최단 거리(dist[next]) > 현재 정점까지 오는데 필요한 최단 거리(dist[cur]) + 인접 정점까지 가는데 필요한 비용 => 갱신 필요

def bellman_ford(start):
    # 벨만 포드 : 특정 노드에서 다른 모든 노드로 가는 최단 거리 구하기
    # for start in range(1, N+1):      # 모든 노드에 대해 벨만 포드 수행 == dist[cur] != float("inf") 조건 추가 X
    dist = [INF for _ in range(N + 1)]       # 무한대로 초기화
    dist[start] = 0          # 시작 노드 초기화

    for i in range(N):  # 모든 정점을 돌면서 탐색 => 이 부분이 왜 있는거?
        for cur in range(1, N+1):
            for next, cost in roads[cur]:   # 인접 정점들에 대해 간선 탐색
                if dist[next] > dist[cur] + cost:  # 현재 정점을 거쳐가는 경우가 더 작다면 최단 거리 갱신
                    dist[next] = dist[cur] + cost

                    if i == N - 1:  # N번째 반복에서 갱신이 된다면(더 최단 경로가 나온다면) 음수 순환이 존재
                        return True    # 순환을 반복하면서 계속 음수 값으로 작아진다는 것은 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능하다는 의미
    return False


TC = int(input())
INF = int(1e9)
for _ in range(TC):
    N, M, W = map(int, input().split())

    roads = [list() for _ in range(N+1)]
    for _ in range(M):       # 도로 정보
        s, e, t = map(int, input().split())   # 연결된 지점 번호 / 도로 이동 시간
        roads[s].append([e, t])
        roads[e].append([s, t])

    for _ in range(W):    # 웜홀 정보
        s, e, t = map(int, input().split())   # 연결
        roads[s].append([e, -t])

    if bellman_ford(1):
        print("YES")
    else:
        print("NO")


    # O(V) * O(VE) => 모든 정점에서 출발해봐야함.
    # 모든 노드가 연결되어 있는 것이 아니기에 1번 노드로만 시작을 했을 떄 웜홀에 아예 도착하지 못하는 것을 막으려면 모든 정점에서 벨만 포드 알고리즘을 수행해야함
    # 만약 1에서 시작함을 가정하고 웜홀에 도착할 수
    # 어떤 지점에서 출발하든 가장 돌아올 때 걸리는 가장 최소 거리를 체크하고, 만약 이 거리가 음수가 나온 경우 YES, 아닌 경우 NO
    # 되돌아오는 거까지 구하면 특정 정점까지의 최단 거리 + 현재 정점 - 특정 정점까지의 거리
    # 정점 사이에 도로와 웜홀이 같이 있다면 도로는 무시하고 웜홀을 타야함
    # 시간여행이 모든 노드를 거치지 않고, 특정 지점까지를 찍고 돌고 와도 상관없어야겠네
    # 탐색 시 거리 비용을 저장(+)하고, 지점 사이에 웜홀이 있다면 - (웜홀이 여러개일 때 무조건 다 돌아야하나?)
    # 현채 출발 시간보다 돌아왔을 때 시간이 적어지려면 -가 들어가니까 당연히 최소 거리로만 다녀야겠지?


