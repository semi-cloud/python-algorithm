from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b, place):
    visited = [[False] * 5 for _ in range(5)]
    q = deque()
    q.append((a, b, 0))      # 맨해튼 거리 정보 저장
    visited[a][b] = True

    while q:
        x, y, d = q.popleft()
        if d >= 2:        # 거리가 2가 넘을때 까지 P가 나타나지 않았다면 탐색 종료
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True

                if place[nx][ny] == "P":    # P를 만나는 경우 거리두기를 지키지 않은 것
                    return False

                if place[nx][ny] == "O":     # 파티션이 없는 빈 자리로만 이동
                    q.append((nx, ny, d + 1))     # 거리 누적 해서 저장
    return True


def solution(places):
    result = [1 for _ in range(len(places))]

    for k, place in enumerate(places):
        arr = [(i, j) for i, p in enumerate(place) for j, char in enumerate(p) if char == 'P']  # 사람 배열
        for people in arr:
            if not bfs(people[0], people[1], place):  # 거리두기 안지킨 사람이 한명이라도 있으면 0
                result[k] = 0
    return result


print(solution(
    [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
))

