# 심사를 받는데 걸리는 시간의 최솟값을 구하기
def binary_search():
    result, start, end = 0, 0, min(arr) * m

    while start <= end:
        total, mid = 0, (start + end) // 2

        for time in arr:       # 해당 시간에 대해 모든 심사대 검사
            total += mid // time       # 심사 가능한 총 인원 수

        if total < m:         # 총 인원보다 작다면 더 큰 범위에서 탐색
            start = mid + 1
        else:
            end = mid - 1      # 총 인원보다 같거나 크다면 더 작은 범위에서 탐색
            result = mid
    return result


n, m = map(int, input().split(' '))
arr = sorted([int(input()) for _ in range(n)])  # 심사 시간 정렬
print(binary_search())
