# 완전 탐색으로 하면 최악의 경우 1024 * 100000
# 1 2 3  1            3(1+2)                    6(1+2+3)
# 4 5 6  5(1+4)  12(5 + 1+1+2+4) - 1(중복)   (6 + 1+2+4+1+2+3) - (1+2)(중복)

N, M = map(int, input().split(" "))  # 1024, 100,000
arr = [list(map(int, input().split(" "))) for _ in range(N)]
task = [list(map(int, input().split(" "))) for _ in range(M)]
sum = [[0 for _ in range(N+1)] for _ in range(N+1)]

sum[1][1] = arr[0][0]
# 맨 위쪽 행 계산
for i in range(2, N+1):
    sum[1][i] = arr[0][i-1] + sum[1][i-1]

# 맨 왼쪽 행 계산
for i in range(2, N+1):
    sum[i][1] = arr[i-1][0] + sum[i-1][1]

# 1. 미리 2차원 누적합 계산
for i in range(2, N+1):
    for j in range(2, N+1):
        sum[i][j] = arr[i-1][j-1] + sum[i][j-1] + sum[i-1][j] - sum[i-1][j-1]  # 이렇게 하면 인덱스 에러

# 2. 필요한 부분만 빼기 연산을 통해 구하기
# 전체 영역(x2,y2) - 왼쪽 영역 - 위쪽 영역 + 겹치는 영역
for x1, y1, x2, y2 in task:
    if x1 == x2 and y1 == y2:
        print(arr[x1-1][y1-1])
    else:
        print(sum[x2][y2] - sum[x2][y1-1] - sum[x1-1][y2] + sum[x1-1][y1-1])


# 이렇게 안하고 애초에 칸을 여유롭게 하나 더 만들어두면 인덱스 에러 방지 가능
# arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         sum[i][j] = arr[i-1][j-1] + sum[i][j-1] + sum[i-1][j] - sum[i-1][j-1]  # 이렇게 하면 인덱스 에러

