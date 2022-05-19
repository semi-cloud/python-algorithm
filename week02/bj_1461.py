# 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산

n, m = map(int, input().split())
book_list = list(map(int, input().split()))

book_list.sort()
left_list = list()
right_list = list()
result = 0
high = max(max(book_list), min(book_list) * -1)

for i in book_list:
    if i < 0:
        left_list.append(i * -1)
    else:
        right_list.append(i)

left_list.sort()
right_list.sort()

while left_list:
    result += left_list[-1]
    for i in range(m):
        if left_list:
            left_list.pop()

while right_list:
    result += right_list[-1]
    for i in range(m):
        if right_list:
            right_list.pop()

result = result * 2 - high
print(result)



