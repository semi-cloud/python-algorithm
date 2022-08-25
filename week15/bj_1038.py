# N번째로 감소하는 수 찾기
from collections import deque

N = int(input())
cnt = -1
q = deque()
for i in range(10):
    q.append(i)

while q:
    num = q.popleft()
    cnt += 1
    if cnt == N:           # N번째 감소 하는 수인 경우
        print(num)
        break

    for i in range(num % 10):   # 감소 해야 하므로 애초에 num 보다 작은 수만 가능
        q.append(num * 10 + i)   # 앞 자리 수에 10을 곱한 후 마지막 자리 더해서 수 만들기
else:               # N번째 감소 하는 수가 없는 경우
    print(-1)



