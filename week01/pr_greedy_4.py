limit = int(input())   # 100
people = sorted(list(map(int, input().split())), reverse=True)

count, start, end = 0, 0, len(people)-1

while start <= end:
    if people[start] + people[end] <= limit:    # 구출 가능
        end -= 1
    start += 1
    count += 1

print(count)

