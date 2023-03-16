# 그려진 선(들)의 총 길이를 구하기(한번 그려진 곳은 동일)
N = int(input())  # 1,000,000(O(N))
arr = [list(map(int, input().split())) for _ in range(N)]  # +- 1,000,000,000
arr.sort(key=lambda x: x[0])  # 왼쪽 정점 기준으로 오름차순 정렬

s, e = arr[0][0], arr[0][1]
ans = 0
for i in range(1, N):
    x, y = arr[i][0], arr[i][1]
    if x <= e:   # 왼쪽 정점이 현재 끝 포인터 보다 작다면 구간 합치기 가능
        e = max(e, y)  # 두 오른쪽 정점 중에 더 큰 값으로 변경
        # s = min(s, x)  # 두 왼쪽 정점 중에 더 작은 값으로 변경 => 오름차순으로 정렬 했으니 새로 추가할 선분이 기존 보다 앞에 오는 경우는 X => 왼쪽 정점 바꿀 필요 X
    else:  # 아니라면 현재 거리 저장하고 포인터 갱신
        ans += e - s
        s, e = x, y
ans += e - s
print(ans)










