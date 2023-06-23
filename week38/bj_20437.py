from collections import defaultdict

T = int(input())
for _ in range(T):  # 100
    w = input()  # 10,000
    k = int(input())
    res1, res2 = float("inf"), 0
    d = defaultdict(list)

    for i in range(len(w)):    # 각 문자 별로 위치 인덱스 저장
        d[w[i]].append(i)

    has_k = False
    for key, value in d.items():
        if len(value) >= k:      # k 개 이상의 리스트인 경우 : 최소 길이 찾기
            has_k = True
            for i in range(0, len(value)-(k-1)):  # k개씩 확인(슬라이딩 윈도우 사용 가능)
                temp = (value[i+(k-1)] - value[i]) + 1
                res1 = min(res1, temp)
                res2 = max(res2, temp)
    if has_k:
        print(res1, res2)
    else:             # 만족하는 연속 문자열이 없는 경우
        print(-1)


# i, j = 0, 0
# d = defaultdict(int)
# d[j] += 1
# while j < len(w):
#     if d[w[j]] < k:     # k개 포함될 때 까지 탐색 진행
#         j += 1
#         d[w[j]] += 1
#     else:
#         res1 = min(res1, (j - i) + 1)  # 가장 짧은 연속 문자열 길이
#         res2 = max(res1, (j - i) + 1)  # 가장 긴 연속 문자열 길이
#         d[w[i]] -= 1
#         i += 1
