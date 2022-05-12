arr = [0, 1]
for i in range(2, 46):      # 피보 나치 리스트 만들기
    arr.append(arr[i - 1] + arr[i - 2])

T = int(input())
for i in range(T):
    results = []
    num = int(input())

    for j in range(len(arr)-1, 1, -1):    # 큰 수부터 확인
        if num == 0:        # 빼고 남은 수가 0이면 종료
            break

        if arr[j] <= num:      # 빼고 남은 수보다 작다면 결과에 추가
            num -= arr[j]         # 빼고 남은 수
            results.append(arr[j])
    results.sort()
    for result in results:
        print(result, end=' ')










