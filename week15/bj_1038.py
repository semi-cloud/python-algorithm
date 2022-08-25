# N번째로 감소하는 수 찾기
from collections import deque

N = int(input())
cnt = -1
q = deque()
for i in range(10):
    q.append(str(i))

while q:
    num = q.popleft()
    cnt += 1
    if cnt == N:           # N번째 감소 하는 수인 경우
        print(num)
        break

    for i in range(0, 10):
        if int(num[-1]) > i:          # 현재 수보다 새로 추가 하려는 수가 더 작으면  432
            q.append(num + str(i))    # 숫자를 문자열로 추가
else:               # N번째 감소 하는 수가 없는 경우
    print(-1)



