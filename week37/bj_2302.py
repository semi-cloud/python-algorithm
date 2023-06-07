# 좌석에 앉는 서로 다른 방법 가짓수 구하기

# i 번째 입장권을 가진 사람은, i-1 좌석과 i+1 좌석에만 앉을 수 있음
# 고로 앞에서 이미 자리가 교환되었으면, i, i+1 교환 ->
# 아래 코드는 연쇄적으로 자리가 교환됨이 가능한거고 ex) 1 2 3 -> 2 1 3 -> 2 3 1...

# 2. DP 풀이
# 1. N번째 좌석을 옮기지 않고 앉은 경우 : N-1개 있었을 때의 경우와 같음
# 2. N번재 좌석을 옮긴 후 N-1번째 좌석에 앉은 경우 : N-2개 있었을 때의 경우와 같음
# dp[i] = dp[i-1] + dp[i-2]
# 하지만 VIP 좌석을 고려해야 하기 때문에 VIP 기준으로 배열을 나누고, 각각에 대한 경우의 수를 모두 곱하면 답
# 1. 시작점 ~ 첫 VIP석 사이 일반석의 갯수 2. VIP석과 VIP 석들 사이 일반석의 갯수 3. 마지막 VIP석과 마지막 점 사이 일반석의 갯수

N = int(input())  # 9
dp = [0 for _ in range(N + 1)]
res = 1

if N == 1:
    print(1)
else:
    dp[0], dp[1], dp[2] = 1, 1, 2
    for i in range(3, N + 1):
        dp[i] = dp[i-1] + dp[i-2]

    M = int(input())
    prev = 0
    for i in range(M):  # 4, 7   1 2 3 4(0) 5 6 7(0) 8 9
        vip = int(input())
        res *= dp[vip - prev - 1]  # 4 - 1 = 3
        prev = vip
    res *= dp[N - prev]
    print(res)


# 백트래킹 + 시간 초과
# 각 자리마다 3개의 선택이 존재(왼쪽, 오른쪽, 바꾸지 X ) 물론 VIP인 경우 X => 2^40.....
# 무조건 중복이 나옴 => 왜냐면 1<->2에서 1 입장에서 오른쪽 바꿈 = 2입장에서 왼쪽이랑 바꿈 => 방문 처리 필요
# def dfs(idx, seat):  # 현재 좌석 위치
#     if idx == N: return 1  # 끝까지 도달한 경우 가능한 좌석 배치
#
#     res = 0
#     if vips[idx]:   # 본인이 VIP 인 경우 그냥 넘어가기
#         res += dfs(idx + 1, seat)
#     else:           # VIP 가 아니라면 세 가지 경우에 대해 재귀 탐색
#         if idx > 0:
#             if not vips[idx-1] and not visit[idx-1]:    # 왼쪽이 VIP 좌석이거나 이미 방문한 곳이면 패스
#                 seat[idx], seat[idx - 1] = seat[idx - 1], seat[idx]  # 왼쪽이랑 자리 바꾸기
#                 visit[idx - 1] = True
#                 res += dfs(idx + 1, seat)
#                 visit[idx - 1] = False
#                 seat[idx], seat[idx - 1] = seat[idx - 1], seat[idx]  # 백트래킹이므로 자리 원상 복구
#
#         if idx < N-1:
#             if not vips[idx + 1] and not visit[idx + 1]:  # 오른쪽이 VIP 좌석이거나 자리가 없는 경우가 아니면
#                 seat[idx], seat[idx + 1] = seat[idx + 1], seat[idx]  # 오른쪽이랑 자리 바꾸기
#                 visit[idx + 1] = True
#                 res += dfs(idx + 1, seat)
#                 visit[idx + 1] = False
#                 seat[idx], seat[idx + 1] = seat[idx + 1], seat[idx]
#
#         if not visit[idx]:   # 자리를 바꾸지 않는 경우
#             visit[idx] = True    # 해당 자리 방문 처리
#             res += dfs(idx + 1, seat)    # 해당 위치에서 자리 안 바꾸는 경우
#             visit[idx] = False   # 해당 자리 방문 처리 해제
#
#     return res
#
# N = int(input())  # 40
# M = int(input())  # 40
# arr = [str(i+1) for i in range(N)]
# vips = [False for _ in range(N+1)]
# visit = [False for _ in range(N+1)]
# for _ in range(M):
#     n = int(input())
#     vips[n-1] = True
#     visit[n-1] = True
#
# print(dfs(0, arr))


