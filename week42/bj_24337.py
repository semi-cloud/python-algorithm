# 가희가 a개, 단비가 b개를 볼 수 있는 건물들 사전 순으로 출력
# 3 2 1 => 1 1 2 (1 2 3이 나옴)
# 3 3 2 => -1 (만들 수 X)

# 10 3 2 => 1 1 1 1 1 1 1 2 3 1 (O, 최대한 앞을 미뤄야 함)
# 10 3 3 => 1 1 1 1 1 1 2 3 2 1
# 10 1 9 => 9 1 8 7 6 5 4 3 2 1
# 9 1 5 => 5 1 1 1 1 4 3 2 1
# 6 3 4 => 1 2 4 3 2 1
# 9 3 5 => 1 1 1 2 5 4 3 2 1

# 가희와 단비 둘 중에 더 많은(높은) 건물을 봐야하는 사람부터 채우기
N, a, b = map(int, input().split(" "))  # 100000
res = [1 for _ in range(N)]

if (a + b - 1) > N:  # 답이 없는 경우 (3 3 2)
    print(-1)
else:
    if a < b:   # 단비가 볼 수 있는 개수가 더 많은 경우
        if a == 1:  # 한개만 볼 수 있다 = 해당 건물이 제일 커야함
            res[0] = b
            start_b = N - b + 1  # 높이 하나 제끼고 시작
        else:
            start_b = N - b   # 2 + 4 = 6, N-1 = 5

        for j in range(N - 1, start_b - 1, -1):  # a 번째 건물보다 커야하므로 제외하고 생각
            res[j] = N - j

        if a > 1:
            idx = 1
            start_a = (N - b - a) + 1   # 제일 높은 건물을 a개에 포함해서 구성(최대한 오른쪽으로 밀기)
            for i in range(start_a, start_a + a - 1):
                res[i] = idx
                idx += 1
    else:       # 가희가 볼 수 있는 개수가 더 많은 경우
        start = N - (a + b - 1)
        idx = 1

        for i in range(start, start + a):  # 오른쪽 방향 먼저 사전순 구성(가희)
            res[i] = idx
            idx += 1

        if a != N - 1:   # 둘이 같거나 가희가 볼 수 있는 개수가 더 많은 경우
            for j in range(N - 1, start + a - 1, -1):  # a번째 건물은 겹쳐서 생각
                res[j] = N - j
    print(" ".join(map(str, res)))
