from collections import defaultdict

N = int(input())
start = defaultdict(int)
result = 0

for i in range(N):
    start[input()] = i                      # 출발 순서

out = [input() for _ in range(N)]          # 도착 순서
for i in range(N):                         # 나보다 뒤에 있는 차가 나보다 앞에 있던 차인 경우 추월
    for j in range(i+1, N):
        if start[out[i]] > start[out[j]]:
            result += 1
            break

print(result)






