# 부분합, S 이상 되는 것 중에 가장 짧은 것의 길이 구하기

N, S = map(int, input().split())
arr = list(map(int, input().split()))

interval_sum, end, ans = 0, 0, float("inf")
for start in range(N):
    while interval_sum < S and end < N:  # 타겟보다 같거나 커질 때까지 end 포인터 증가 시키기
        interval_sum += arr[end]
        end += 1

    if interval_sum >= S:
        ans = min(ans, end - start)
        interval_sum -= arr[start]

if ans == float("inf"):   # 다 더해도 타겟보다 크지 않은 경우
    print(0)
else:
    print(ans)






