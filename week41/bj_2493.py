# 왼쪽 방향으로 현재 건물보다 가장 "먼저 만나는" 큰 탑 찾기
# DP로 풀려 했으나 풀 수 X => 예시 6 10 8 3 4 9 에서 4는 8 정보를 기억해야 하고 9는 10 정보를 기억해야함
# 현재 노드보다 가장 왼쪽으로 가까이 있는 큰 수 찾기

N = int(input())   # 500,000
tops = list(map(int, input().split(" ")))  # 100,000,000
res = [0 for _ in range(N)]   # 맨 첫번째 건물의 신호는 수신 불가능
st = []

for i in range(1, len(tops)):
    if tops[i-1] > tops[i]:   # 바로 직전 건물이 크면 신호 수신 확정
        st.append((i, tops[i-1]))
        res[i] = i
    elif st and tops[i-1] <= tops[i]:          # 직전 건물이 작다면 신호를 수신할 건물을 찾아야함
        while st and st[-1][1] <= tops[i]:     # 현재 건물보다 커지는 건물이 나올때 까지 pop
            st.pop()

        if len(st) > 0:    # 큰 건물이 있는 경우
            res[i] = st[-1][0]
        else:              # 큰 건물이 없는 경우
            res[i] = 0

print(" ".join(map(str, res)))
