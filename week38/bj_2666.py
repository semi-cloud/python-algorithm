# 사용할 벽장 순서에 따라서 문 이동 하는 최소 횟수 구하기
# 매 벽장 마다 왼/오 가장 가까운 열린 벽장 찾고 문 이동 -> 앞에서 선택한 값이 뒤에 영향을 주기 때문에 그리디 X
# 무조건 현재 상태에서 가까운거 찾는게 최선의 선택 보장 X

# 1. 백트래킹 + 완전 탐색 풀이 :  A / B 중 어떤 문을 여는가에 따라 재귀 분기 (N = 20)
res = float("inf")
def bt(idx, cnt):
    global res, door1, door2

    if idx == M:   # 끝까지 모두 탐색 했다면 최소값 갱신하고 종료
        res = min(res, cnt)
        return

    temp1 = door1
    door1 = arr[idx]    # 왼쪽 문하고 스왑
    bt(idx + 1, cnt + abs(arr[idx] - temp1))   # 왼쪽 벽장 사용하는 경우
    door1 = temp1     # 원래 값으로 복구

    temp2 = door2
    door2 = arr[idx]    # 오른쪽 문하고 스왑
    bt(idx + 1, cnt + abs(arr[idx] - temp2))   # 오른쪽 벽장 사용하는 경우
    door2 = temp2

N = int(input())
door1, door2 = map(int, input().split(" "))
M = int(input())
arr = [int(input()) for _ in range(M)]

bt(0, 0)
print(res)

# 2. DP 풀이(메모지에이션)
# dp[x][y][k] : k 번째 단계에서 방 x/y 를 여는(열려 있는 방) 최소 이동 횟수
# 타겟 = 3 1 6 이라 했을 때
# [2, 5] -> [2,3] / [3,5] -> [1,2] [1,3](중복) / [1,3](중복) [1,5] -> [6,1] [6,2] [6,1] [6,3] / [6,1] [6,3] [6,1] [6,5]
dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]

def memoization(step, x, y):
    if step > M: return 0
    if dp[step][x][y] != -1: return dp[step][x][y]

    dp[step][x][y] = min(   # 돌아 오면서 거리 최소값 계산
        dp[step + 1][arr[step]][x] + abs(arr[step] - x),   # 왼쪽문을 선택 하는 경우
        dp[step + 1][arr[step]][y] + abs(arr[step] - y))    # 오른족 문을 선택 하는 경우

    return dp[step][x][y]

# 처음 접근 방식 : 하나씩 인덱스를 이동
# def bt(idx, n, cnt):
#     global res
#     if n < 0 or n > N: return  # 범위를 벗어나는 경우
#
#     if idx == N:        # 모든 벽장을 열었다면 총 문 이동 횟수 갱신
#         res = min(res, cnt)
#         return
#
#     for i in range(idx, N-2):    # 열려는 벽장 순서 3 1 6 5
#         if cupboard[n] == 1:    # 열려 있는 벽장의 경우
#             bt(idx + 1, n, cnt)  # 다음 열려는 벽장 탐색
#         else:                   # 닫혀 있는 벽장의 경우
#             bt(idx, n-1, cnt + 1)  # 왼쪽 벽장 탐색
#             bt(idx, n+1, cnt + 1)  # 오른쪽 벽장 탐색
