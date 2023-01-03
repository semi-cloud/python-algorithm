# 다른 수 두개의 합으로 나타낼 수 있는 좋은 수 개수 출력

N = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 오름차순 정렬
ans = 0

# 1. 투 포인터 이용 : O(N^2)
def good_num(pos):
    global ans

    lis = arr[:pos] + arr[pos + 1:]  # 타겟을 제외한 배열을 탐색 : 0이 포함 된다면 자기 자신이 좋은 수가 되므로
    start, end = 0, len(lis) - 1
    while start < end:
        temp = lis[start] + lis[end]
        target = arr[pos]

        if temp == target:
            ans += 1
            return
        elif temp > target:
            end -= 1
        else:
            start += 1

for i in range(len(arr)):
    good_num(i)
print(ans)

# 시간 초과 코드
# flag = False
# ans = 0
# for i in range(N):  # 2000
#     for j in range(i):  # 2000
#         sub = arr[i] - arr[j]  # 뺀값
#         for k in range(j+1, i):                  # 2000
#             if arr[k] == sub:
#                 ans += 1
#                 flag = True
#                 break
#         if flag:
#             break

