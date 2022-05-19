# 진입 지점과 나간 지점 사이에 카메라 설치 되어 있음
# 모든 차량이 만나야 하는 경우, 최소 카메라 몇 대?

a = [list(map(int, input().split())) for _ in range(4)]
arr = sorted(a, key=lambda x: x[1])  # 종료 시간 기준 오름차순 정렬

count, latest_camera = 0, 0
for i in range(len(arr)-1):
    if i == 0:                       # 카메라 초기값을 종료 시간으로 설정
        latest_camera = arr[i][1]
        count += 1

    if latest_camera < arr[i+1][0]:   # 현재 카메라 값보다, 더 늦게 시작한다면 카메라 갱신 필요
        latest_camera = arr[i+1][1]
        count += 1

print(count)




