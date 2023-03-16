# 4번 유사 문제 : 완전탐색 + BFS
# 오름차순 정리된 상태를 만들 수 있는 최소 이동 횟수 구하기
# 메모리 제한 => 딥 카피 배열 복사해 가면서 완전 탐색이 불가능, 다른 방법으로 완전 탐색 해야함(비트 마스킹)
# 보드판의 특정 상황을 탐색한 적이 있는지 확인 => 2차원 배열 전체를 기록하면 메모리 초과

from collections import deque

def bfs(arr):
    a = "".join(map(str, sum(arr, [])))  # 2차원 배열 => 문자열
    q = deque([(0, a)])  # 딕셔너리 key로 사용하기 위해서 문자열로 바꿔서 해싱
    visit = {a: True}  # 방문 표시 : 딕셔너리(해시)를 통해서

    # 1. 메모리를 줄이기 위해서 BFS 상태 노드를 2차원 배열에서 문자열로 변환해서 탐색
    while q:
        cnt, temp = q.popleft()
        if temp == '123456780':
            return cnt

        i = 0
        for idx in range(9):    # 큐 한번 돌때 빈칸이랑 한번 스왑 해야하기 때문에 포문 안에 로직을 넣으면 안됌
            if temp[idx] == '0':  # 빈 칸을 찾은 경우 상하좌우 중에 빈칸이랑 교체할 숫자가 있는지 체크
                i = idx

        x, y = i // 3, i % 3  # 2차원 배열의 좌표로 변환해서 상하좌우 좌표 탐색
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < 3 and 0 <= ny < 3:
                copy = list(temp)       # 파이썬의 문자열 자체는 변경 불가능 하기 때문에, 배열로 변환 필요
                copy[(nx * 3) + ny], copy[i] = copy[i], copy[(nx * 3) + ny]
                copy = "".join(copy)    # 두 수를 교환하고 나면은 다시 문자열로 변환(1차원 배열 => 문자열)

                if visit.get(copy) is None:  # 이미 정렬이 되었던 배열이 아니라면
                    visit[copy] = True
                    q.append((cnt + 1, copy))

    return -1

    # 2. 2차원 배열을 BFS 노드 상태 정보로 저장
    # while q:
    #     cnt, temp = q.popleft()
    #     if "".join(map(str, sum(temp, []))) == '123456780':
    #         return cnt
    #
    #     for x in range(3):
    #         for y in range(3):
    #             if temp[x][y] == 0:
    #                 for k in range(4):  # 상하좌우 중에 빈칸이랑 교체할 숫자가 있는지 체크
    #                     nx, ny = x + dx[k], y + dy[k]
    #
    #                     if 0 <= nx < 3 and 0 <= ny < 3:
    #                         copy = [c[:] for c in temp]
    #                         copy[nx][ny], copy[x][y] = copy[x][y], copy[nx][ny]  # 스왑
    #                         string = "".join(map(str, copy))
    #
    #                         if visit.get(string) is None:  # 이미 정렬이 되었던 배열이 아니라면
    #                             visit[string] = True
    #                             q.append((cnt + 1, copy))


dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
arr = [list(map(int, input().split())) for _ in range(3)]  # 3 * 3 배열  # 큐에서 작업할 때는 2차원 배열이 아닌 문자열로 변경
print(bfs(arr))

