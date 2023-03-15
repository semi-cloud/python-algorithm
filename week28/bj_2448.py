# N번째 줄 까지별 찍기
# 배열을 출력할 때 0 이면 공백 " "으로 출력, 1이면 "*" 로 바꿔서 출력

def copy(arr, new_arr, n):    # 총 세 곳에서 이전의 배열을 복사
    cur_r, cur_c = n // 2, (len(new_arr[0]) // 2)   # 현재 배열의 세로 가로 길이
    r, c = len(arr), len(arr[0])  # 이전 배열의 세로 가로 길이

    for i in range(0, r):        # (0, N // 2 - 이전 가로 길이 // 2)
        for j in range(cur_c - (c // 2), cur_c - (c // 2) + c):
            new_arr[i][j] = arr[i][j - c + (c // 2)]

    for i in range(cur_r, cur_r + r):     # (N // 2, 0)
        for j in range(0, c):
            new_arr[i][j] = arr[i - cur_r][j]

    for i in range(cur_r, cur_r + r):     # (N // 2 + 1, 현재 배열 가로 길이 // 2)
        for j in range(cur_c + 1, cur_c + + c + 1):
            new_arr[i][j] = arr[i - cur_r][j - cur_c -1]

def triangle(N):
    if N == 3:    # 가장 작은 삼각형
        return [[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 1, 1, 1, 1]]

    arr = triangle(N // 2)   # 이전 단계에서의 삼각형 배열 반환
    new_arr = [[0 for _ in range(len(arr[0]) * 2 + 1)] for _ in range(N)]   # 새로운 배열 생성
    copy(arr, new_arr, N)
    return new_arr

N = int(input())  # 3 * 2k
res = triangle(N)
for r in res:
    for node in r:
        if node == 0:
            print(" ", end="")
        else:
            print("*", end="")
    print()

