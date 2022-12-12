# C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하기

def install(n):    # 최소 거리가 n 일때 설치할 수 있는 공유기의 개수 찾기
    prev_home = house[0]
    cnt = 1        # 첫 번째 집은 무조건 설치한다고 가정
    for i in range(1, N):
        if house[i] - prev_home >= n:   # 공유기를 설치한 집 간의 거리가 최소 거리 n보다 같거나 크다면 설치 가능
            prev_home = house[i]       # 바로 직전에 공유기를 설치한 집의 위치 갱신
            cnt += 1
    return cnt

def binary_search():
    left, right = 1, house[N-1] - house[0]  # 최소 거리 1, 최대 거리 끝집-첫집 으로 초기화

    while left <= right:
        mid = (left + right) // 2
        install_count = install(mid)     # 최소 거리가 mid 일때 설치 가능한 총 공유기의 개수 구하기

        if install_count >= C:   # 설치해야 하는 공유기의 개수와 같거나 많다면 최소 거리를 늘릴 수 있음
            left = mid + 1
        else:                   # 설치해야 하는 공유기의 개수보다 적다면 최소 거리를 더 좁혀야함
            right = mid - 1
    return right

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]   # 집의 위치
house.sort()         # 집 위치 오름차순 정렬
print(binary_search())











