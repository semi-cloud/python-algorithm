# 1. 시간 초과
# 1-1. 제거할 바위 2개 조합으로 생성
# 1-2. 포문 탐색으로 매 경우마다 바위 사이 거리를 구하고, 그 중에 가장 큰 값을 갱신

# 2. 이분 탐색
# 최적화 문제 : 바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 가장 큰 값, 결정 문제 : 각 지점 사이의 거리의 최솟값 중에 가장 큰 값이 되는 제거해야할 바위 찾기
# 특정한 조건을 만족하는 가장 알맞은 값을 범위를 조절해가며(이때 이진탐색) 빠르게 찾기
# 어느 바위를 제거하면 조건을 만족할 수 있는가를 체크 : 조건은 거리 최솟값의 최대값

# 역방향으로 생각해야함 = 답이 최소값이니까 "최소값을 중간값으로 미리 정해두고 이 값을 조절" 하면서
# 바위 사이 최소 간격을 특정 값으로 정했을 때 n개 이하로 바위를 제거 가능한지 체크
# 1. 답에서 구해야 하는 최소 거리 기준 값을 (0 + 최대 거리) // 2 로 설정
# 2. 최소 거리 기준값이 12 == 나머지 바위 사이의 간겨들은 12보다 커야지 성립, 이 때 12보다 작은 거리가 없도록 제거해야 하는 돌의 개수를 구한다.
# 3. 제거해야 하는 돌의 개수가 최대 N개여야하므로, N개를 넘어간다는 것은 돌을 더 적게 제거해야 한다는 것이므로 돌 사이 간격의 기준을 낮춰야 함 = 0 + 11의 중간값인 5로 낮춘다.(right = mid - 1)
# 4. N개를 넘어가게 돌을 제거하지 않고도 최소 기준을 맞출 수 있다면, 돌을 더 제거했을 때 간격의 최대값이 나올 수 있으므로 간격의 기준을 높인다 = 13 + 25의 중간값인 19로 올린다. (left = mid + 1)

def solution(distance, rocks, n):  # 조합 = O(2^N) = 시간 초과
    rocks.sort()  # 거리 순으로 정렬
    rocks.append(distance)

    s, e = 0, distance
    res = float("inf")
    while s <= e:
        target = (s + e) // 2
        rock_cnt = 0

        # 돌 사이 거리의 최소가 target일 경우 제거 해야할 돌 개수 구하기
        cur = 0
        for rock in rocks:
            if rock - cur >= target:  # 최소여야 하는 거리보다 값이 크거나 같다면 다음 돌로 넘어감
                cur = rock
            else:       # 최소여야 하는 거리보다 값이 작다면 돌 제거
                rock_cnt += 1

        if rock_cnt > n:  # 최대로 제거해야할 돌 개수보다 많다면
            e = target - 1  # 돌을 더 적게 제거해야 함으로 최소 거리 기준을 낮춤
        else:
            s = target + 1  # 돌을 더 제거할 수 있으므로 최소 거리 기준을 높임
            res = target    # 이 거를 위쪽 if 문으로 올리면 일부 테스트 케이스 실패
    return res

print(solution(25, [2, 14, 11, 21, 17], 2))