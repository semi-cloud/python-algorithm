# 유저가 탐험할 수 있는 최대 던전 수 반환(던전 입장 순서에 따라 탐험 가능한 수가 달라짐)

def dfs(depth, visit, arr, k):
    global ans
    if depth > ans:   # 최대값 계산
        ans = depth

    for idx, d in enumerate(arr):  # 탐험 가능한 모든 던전에 대해 DFS 수행
        if k >= d[0] and not visit[idx]:  # 현재 피로도가 최소 피로도보다 작거나 이미 방문했다면 던전 탐험 불가능
            visit[idx] = True  # 던전 방문 표시
            dfs(depth + 1, visit, arr, k - d[1])  # 던전 탐험 후 피로도 소모
            visit[idx] = False

    # for idx, d in enumerate(arr):   # 탐험 가능한 모든 던전에 대해 DFS 수행
    #     if k >= d[0] and not visit[idx]:   # 현재 피로도가 최소 피로도보다 작거나 이미 방문했다면 던전 탐험 불가능
    #         visit[idx] = True       # 던전 방문 표시
    #         cnt += 1
    #         dfs(visit, arr, k - d[1])   # 던전 탐험 후 피로도 소모
    #         visit[idx] = False
    #
    # ans = max(ans, cnt)      # 더 이상 갈 곳이 없다면 최대값 계산하고 종료
    # cnt -= 1       # 0으로 초기화 하면 안되고 기존의 값 유지

ans = 0
def solution(k, dungeons):  # 현재 피로도, 던전 별 최소 필요도/ 소모 피로도
    visit = [False for _ in range(len(dungeons))]
    dfs(0, visit, dungeons, k)
    return ans

print(solution(80, [[80, 20], [50, 40], [30, 10]]))
print(solution(100, [[80, 60], [50, 5], [30, 1]]))

# for i in range(len(dungeons)):   # 이중 포문 돌 필요가 없음
#     visit = [False for _ in range(len(dungeons))]
#     if k >= dungeons[i][0]:    # 탐험 가능한 모든 던전에 대해 DFS 수행
#         temp = k
#         visit[i] = True
#         temp -= dungeons[i][1]  # 던전 탐험 후 피로도 소모
#         dfs(visit, dungeons, temp)



