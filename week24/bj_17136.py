# 종이가 주어졌을 때, 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최소 개수 구하기

def can_attach(x, y, num, temp):  # 색종이 크기
    for i in range(x, x + num):      # 해당 범위 내의 모든 수가 1이라면 색종이로 덮을 수 있음
        for j in range(y, y + num):
            if (0 > i or i >= 10 or 0 > j or j >= 10) or temp[i][j] == 0:    # 범위를 넘어가는 경우도 색종이를 붙힐 수 없음
                return False
    return True

def attach(x, y, k, temp):  # 색종이 붙이기
    for i in range(x, x + k):
        for j in range(y, y + k):
            temp[i][j] = 0

def solution(temp, size):
    global result
    if paper[size] > 5:  # 같은 색종이를 5개 이상 사용한 경우라면 바로 가지 탐색 종료
        return

    if sum(paper) >= result:  # 최소 값을 이미 넘어가는 경우 해당 가지는 바로 탐색 종료
        return

    # 색종이 삽입할 위치 찾기
    x, y = -1, -1
    for i in range(10):
        for j in range(10):
            if temp[i][j] == 1:
                x, y = i, j
                break
        if x != -1 and y != -1:
            break

    if x == -1 and y == -1:   # 새로 삽입할 위치가 없다면 모든 곳에 색종이를 붙였다는 의미
        result = min(result, sum(paper))  # 더이상 붙일 곳이 없다면 최소 개수 체크
        return

    # 붙일 수 있는 색종이 크기 구하고 붙이기
    for k in range(1, 6):
        copy = [t[:] for t in temp]  # 각 종이의 선택 마다 복사본을 생성

        if can_attach(x, y, k, copy):
            attach(x, y, k, copy)  # 색종이 붙히기
            paper[k] += 1  # 색종이 개수 증가
            solution(copy, k)
            paper[k] -= 1   # 한 경로(가지)가 끝나고 돌아오면 색종이 개수 원래대로 되돌려놓기

    # for i in range(10): # 이 부분(붙일 수 있는 공간 찾기)이랑 아래 k(색종이 크기) 탐색을 분리 하는게 해결 방법
    #     for j in range(10):
    #         if temp[i][j] == 0:  # 이미 방문했거나 색종이로 덮히면 안되는 칸이라면 패스
    #             continue
    #
    #         # 현재 위치에서 덮을 수 있는 모든 색종이의 경우에 대해 재귀 형태로 배열을 인자로 전달
    #         for k in range(1, 6):
    #             copy = [t[:] for t in temp]    # 각 종이의 선택 마다 복사본을 생성
    #
    #             if can_attach(i, j, k, copy) and not visited[i][j][k]:
    #                 attach(i, j, k, copy)  # 색종이 붙히기
    #                 paper[k] += 1    # 색종이 개수 증가
    #                 visited[i][j][k] = True
    #                 solution(copy, k)  # 재귀 형태로 배열 인자로 전달
    #                 paper[k] -= 1     # 한 경로(가지)가 끝난 다면 돌아오면서 색종이 개수 원래대로 되돌려놓기
    #                 visited[i][j][k] = False

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
arr = [list(map(int, input().split())) for _ in range(10)]
paper = [0 for _ in range(6)]   # 크기별 색종이의 개수 관리
result = float("inf")
solution(arr, 0)

if result == float("inf"):   # 색종이 붙이기를 아예 실패하는 경우 -1 출력
    print(-1)
else:
    print(result)


