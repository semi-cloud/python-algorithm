# n개의 섬 사이에 존재하는 다리에 중량 제한이 있음, 초과하는 양의 물품이 다리를 지나면 무너짐
# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값 구하기

from collections import deque

n, m = map(int, input().split())
arr = [[] for _ in range(n + 1)]
max_w = float('-inf')
for _ in range(m):
    x, y, w = map(int, input().split())
    arr[x].append([y, w])  # 양방향 연결
    arr[y].append([x, w])
    max_w = max(max_w, w)
fac1, fac2 = map(int, input().split())


def find_max_weight(a):  # 이진 탐색 이용
    low, high, result = 1, max_w, 0

    while low <= high:
        mid = (low + high) // 2  # 임시 최댓값
        if bfs(a, mid):        # 갈 수 있는 경로가 존재 하면 더 큰 중량 값에서 탐색
            result = mid
            low = mid + 1
        else:
            high = mid - 1     # 갈 수 있는 경로가 없으면 더 작은 중량 값에서 탐색
    return result


def bfs(start, cost):
    visit = [False] * (n+1)
    q = deque([start])
    visit[start] = True

    while q:
        x = q.popleft()
        if x == fac2:        # 도착 지점을 방문 했다면 True 반환
            return True

        for y, w in arr[x]:  # 연결 정보
            if not visit[y] and w >= cost:  # 갈 수 있는 길이면 큐에 추가
                q.append(y)
                visit[y] = True
    return False

print(find_max_weight(fac1))
