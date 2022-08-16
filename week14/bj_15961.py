# 손님이 먹을 수 있는 초밥 가짓수의 "최댓값"을 구하기
from collections import defaultdict

N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]
canEat = defaultdict(int)
cnt, canEat[c] = 1, 1      # cnt : 먹을 수 있는 초밥의 종류의 개수

for i in range(k):         # k개의 접시를 먹고 딕셔너리에 저장
    if canEat[arr[i]] == 0:
        cnt += 1
    canEat[arr[i]] += 1

answer = cnt
for left in range(N):
    right = (left + k) % N     # 원형 배열 인덱스
    canEat[arr[left]] -= 1     # 왼쪽 포인터

    if canEat[arr[left]] == 0:   # 아예 해당 원소가 없는 경우
        cnt -= 1
    if canEat[arr[right]] == 0:   # 새로운 원소인 경우
        cnt += 1
    canEat[arr[right]] += 1     # 오른쪽 포인터 이동

    answer = max(answer, cnt)   # 먹을 수 있는 종료 개수의 최댓값 저장
print(answer)






