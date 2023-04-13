# 범위를 벗어나는 경우를 쉽게 계산하기 위하여 자물쇠 배열의 크기를 늘리는 방법이 존재
# 자물쇠가 모두 1인 경우 자물쇠를 항상 풀 수 있음

def solution(key, lock):
    N, M = len(key), len(lock)

    def rotate_key():  # 회전
        temp = [[0 for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                temp[j][N - i - 1] = key[i][j]
        return temp

    def is_lock(x, y, new_key):   # 2차원 배열에서의 슬라이딩 윈도우
        cnt = 0
        for i in range(x, x + N):
            for j in range(y, y + N):
                if arr[i][j] == 0 and new_key[i - x][j - y] == 0: return -1
                if arr[i][j] == 1 and new_key[i - x][j - y] == 1: return -1
                if arr[i][j] == 0 and new_key[i - x][j - y] == 1: cnt += 1
        return cnt

    # 1. 자물쇠 배열 크기 늘리고 값 복사(가로 세로 + (열쇠 크기 -1)
    total = 0
    K = M + ((N - 1) * 2)
    arr = [[2 for _ in range(K)] for _ in range(K)]  # 원래 영역이 아닌 부분과 원래 자물쇠 영역은 구분 필요
    for i in range(M):
        for j in range(M):
            if lock[i][j] == 0: total += 1
            arr[i + (N - 1)][j + (N - 1)] = lock[i][j]

    # 2. 열쇠 배열의 고정된 크기 만큼(N) 탐색(슬라이딩 윈도우)
    for d in range(4):
        for i in range(0, (K + 1) - N):
            for j in range(0, (K + 1) - N):
                cnt = is_lock(i, j, key)
                if cnt == total:
                    return True  # 해당 상황에서는 풀 수 없어도 결국 하나라도 풀면 성공
        key = rotate_key()
    return False
