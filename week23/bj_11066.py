# O(N^3) 시간 복잡도
T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]

    # 1. 연속합(누적합) 구하기 : a부터 b 까지의 부분연속합을 구할 때, b 까지합 - (a-1) 까지합 으로 구해주면됨(sum 사용 x)
    sums = {-1: 0}       # 인덱스가 [-1] 일때 처리를 해주지 않는 다면 start = 0 일때 배열의 마지막 원소를 가리키게 됨
    for idx in range(K):
        sums[idx] = sums[idx - 1] + files[idx]

    # 2. 각 파일 size - end 번호 까지의 파일을 합칠 때 최소 비용을 저장
    for size in range(1, K):   # size 크기로 묶은 그룹 들의 최소 파일 합치기 비용 구하기
        for start in range(K-1):  # 각 그룹의 시작 인덱스 범위
            end = start + size

            if end >= K:   # 해당 그룹은 범위를 벗어남
                break

            result = float("inf")
            for k in range(start, end):
                result = min(result, dp[start][k] + dp[k+1][end] + (sums[end] - sums[start - 1]))  # 최소 비용 구하기

            dp[start][end] = result  # 최소 비용 저장
    print(dp[0][-1])