# 모든 미사일 범위를 관통 하는 최소 미사일 개수 구하기
# 그리디 => 가장 많이 겹치는 최소 공통 구간 찾는 문제

def solution(targets):
    N = len(targets)  # 목표 폭격 미사일 개수
    targets.sort(key=lambda x: x[1])  # 끝나는 시간 기준으로 정렬, 끝나는 시점 기준으로 폭격 미사일 위치 정함

    res, shoot_pos = 0, -1  # 최소 미사일 개수 존재해야 하는 위치 계속해서 갱신
    for i in range(N):
        if shoot_pos <= targets[i][0]:  # 폭격 미사일 위치가 다음 시작 지점보다 작은 경우 공통 구간 존재 X
            res += 1  # 새로운 미사일 추가
            shoot_pos = targets[i][1]  # 다음 구간의 끝 위치로 폭격 미사일 위치 변경
    return res

# 이분 탐색 풀이 : 시간 초과 + 테케 몇 개 틀림
# def binary_search(N, targets, visited):
#     s, e = targets[0][0], max(map(max, targets))
#     res = []
#
#     while s <= e:  # 100,000,000 : O(LogN)
#         mid = (s + e) / 2.0  # 실수 고려
#         left, right, center = 0, 0, 0
#         ans = []
#
#         for i in range(N):
#             if visited[i]: continue
#             target = targets[i]
#
#             if target[0] < mid < target[1]:  # 걸쳐져 있는 경우
#                 center += 1
#                 ans.append(i)
#             elif mid >= target[1] > s:  # 끝 위치 > start 위치
#                 left += 1
#             elif mid <= target[0] < e:  # 시작 위치 < end 위치
#                 right += 1
#
#         if mid > 0 and left == 0 and right == 0:  # 해당 위치에서 가장 많이 커버 가능한 경우
#             res = ans
#             break
#         elif left >= right:  # 왼쪽에 더 커버하지 못한 미사일이 많다면 범위 이동
#             e = mid - 0.01
#         elif left < right:  # 오른쪽에 더 커버하지 못한 미사일이 많은 경우
#             s = mid + 0.01
#     return res
#
#
# def solution(targets):
#     N = len(targets)  # 목표 폭격 미사일 개수
#     visited = [False for _ in range(N)]
#     targets.sort(key=lambda x: (x[0], x[1]))
#
#     cnt, res = 0, 0
#     while cnt < N:     # 모든 미사일이 폭격되면 종료
#         pos = binary_search(N, targets, visited)  # 일단 가장 커버하는 위치 선정
#         for p in pos:  # 폭격된 미사일 방문 표시
#             visited[p] = True
#             cnt += 1
#         res += 1
#     return res
#
# print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))