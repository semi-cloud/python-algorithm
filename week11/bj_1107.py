N = int(input())       # 이동하려는 채널
M = int(input())       # 고장난 버튼 개수
if M != 0:
    break_arr = list(map(int, input().split()))
else:
    break_arr = []

temp = abs(100 - N)           # 현재 채널에서 ++, -- 로만 움직이는 경우
for i in range(1000001):      # 만들 수 있는 채널의 모든 경우의 수
    flag = False
    num = str(i)

    for j in range(len(num)):            # 채널의 각 문자를 체크
        if int(num[j]) in break_arr:     # 버튼이 고장나 만들 수 없는 경우 패스
            flag = True
            break

    if not flag:                         # 채널을 만들 수 있는 경우
        temp = min(temp, abs(N - int(num)) + len(num))      # 이동하려는 채널과 현재 채널을 뺀 값 중 최소값을 구하기

print(temp)















