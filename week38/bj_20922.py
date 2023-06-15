# 같은 원소가 k개 이하로 들어있는 최장 연속 부분 수열 길이 구하기
# DP 가 아니라 투 포인터 문제("연속 부분 수열")

N, K = map(int, input().split(" "))  # 200,000 / 100
arr = list(map(int, input().split(" ")))
visit = [0 for _ in range(max(arr) + 1)]

i, j = 0, 0
res = 0
while i < N and j < N:
    if visit[arr[j]] < K:  # 특정 원소가 K번 미만으로 나온 경우에만 탐색 더 진행
        visit[arr[j]] += 1  # 방문 표시
        res = max(res, (j - i) + 1)  # 연속 부분 수열 길이의 최대값 구하기(이건 매번 검사 필요)
        j += 1
    else:                  # 특정 원소가 K번 이상 나온 경우
        visit[arr[i]] -= 1
        i += 1           # 해당 위치로부터 연속 수열 탐색 종료, 다음 위치로 넘어감
print(res)




