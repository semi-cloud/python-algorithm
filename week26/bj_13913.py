# 수빈이가 동생을 찾을 수 있는 가장 빠른 시간 및 이동 경로(위치) 구하기
# 백트래킹 + DP라 생각 했는데 애초에 DFS 재귀 방식은 시간 초과
# 방문 배열이 필요한 이유: 동생을 빠른 시간 내에 찾아야 하는데 이전에 방문했던 지점으로 다시 돌아갈 필요가 X

from collections import deque

# BFS 에서 가지의 탐색 경로를 기억하는 법 => 다음 이동 위치에 현재의 위치를 기록
def find(n):
    q = deque()
    q.append((n, 0))

    while q:       # 반복문의 시간 복잡도 :
        x, depth = q.popleft()

        if x == K:        # 큐에서 꺼낸 수가 동생 위치라면 종료
            ans.append(K)
            for _ in range(depth):    # 걸리는 시간만큼 반복하면서 부모를 모두 출력
                ans.append(parent[x])
                x = parent[x]
            return depth     # DFS 와 달리 가장 먼저 나온 K가 최단 이동 경로를 가지고 있으므로, 최소 횟수 저장 필요 없이 바로 종료

        for next in [x+1, x-1, x*2]:
            if 0 <= next <= 100000 and parent[next] == -1:  # 범위 안에 있고 방문하지 않았다면 큐에 추가(방문한 배열은 부모 노드가 초기화 되어있음)
                parent[next] = x     # 부모 노드 기록
                q.append((next, depth+1))

N, K = map(int, input().split())
if N == K:       # 시작점과 도착점이 같은 경우 고려
    print(0)
    print(N)
else:
    parent = [-1 for _ in range(100001)]  # 위치 추적 배열을 따로 선언, 시작 지점이 0인 경우를 고려해서 -1로 초기화(방문 체크가 불가능)
    ans = []
    print(find(N))
    print(" ".join(map(str, ans[::-1])))  # 역으로 출력
