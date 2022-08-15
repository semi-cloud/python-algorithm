# 무게가 양의 정수인 N개의 저울추가 주어질 때, 이 추들을 사용하여 측정할 수 없는 양의 정수 무게 중 최솟값을 구하기

N = int(input())       # 저울 추의 개수
arr = list(map(int, input().split()))   # 무게
arr.sort()             # 오름 차순 정렬

total = 1
for num in arr:
    if total < num:    # 현재 저울추 무게가 누적 무게합 보다 크다면
        break          # 저울추의 총합은 측정할 수 없는 최솟값이므로 종료
    total += num     # 누적합 구하기

print(total)






