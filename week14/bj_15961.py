# 손님이 먹을 수 있는 초밥 가짓수의 "최댓값"을 구하기

from collections import defaultdict

N, d, k, c = map(int, input().split())
foods = [int(input()) for _ in range(N)]
foods.extend(foods)       # 원형 배열 생성
l, r, result = 0, 0, 0
dict_ = defaultdict(int)
dict_[c] = 1  # 접시를 k개 연속해서 먹으면 쿠폰 무조건 발급

# 1. k개의 접시를 먹고 딕셔너리에 저장
while r < k:
    dict_[foods[r]] += 1
    r += 1

# 2. 슬라이딩 윈도우 적용
while r < len(foods):
    result = max(result, len(dict_))   # 딕셔너리의 길이 = 먹을 수 있는 초밥 개수

    # 슬라이딩 1 : 맨 왼쪽 초밥 제거
    dict_[foods[l]] -= 1
    if dict_[foods[l]] == 0:   # 0이 되면 딕셔너리에서 제거
        del dict_[foods[l]]

    # 슬라이딩 2 : 오른쪽 초밥 추가
    dict_[foods[r]] += 1
    l += 1
    r += 1
print(result)







