# T번 회전 시킨 후 원판에 적힌 수의 합 구하기
# 인접한 수를 바로바로 삭제 해 버리면 그 삭제된 수와 인접한 수는 제거 하지 못하게 되므로 미래에 삭제될 수라고 체크 표시만 하기

N, M, T = map(int, input().split())
circles = [list(map(int, input().split())) for _ in range(N)]  # 50

for _ in range(T):  # x 번째 원판을 d 방향으로 K칸 회전(d = 0 : 시계,d = 1 : 반시계)  50
    x, d, k = map(int, input().split())  # x의 배수인 모든 원판들 회전
    # 1. 원판 해당 방향으로 회전 시키기
    for cnt in range(x, N+1, x):
        temp = [0 for _ in range(M)]   # 새로운 임시 배열 생성
        if d == 0:  # 시계 방향
            for idx, c in enumerate(circles[cnt-1]):
                temp[(idx + k) % M] = c
        else:       # 반시계 방향
            for idx, c in enumerate(circles[cnt-1]):
                temp[(idx - k + M) % M] = c
        circles[cnt-1] = temp   # 회전된 배열로 바꿔치기

    # 2-1. 원판에 수가 남아 있다면 인접하면서 수가 같은 거 찾고 0으로 제거(모든 원판에 대해 탐색)
    visit, total = [[False for _ in range(M)] for _ in range(N)], 0
    flag = False
    for i in range(N):
        for j in range(M):
            temp = False
            if circles[i][j] == 0: continue

            if i != 0 and circles[i - 1][j] == circles[i][j]:  # i = 0
                visit[i - 1][j], flag = True, True
            elif i != N - 1 and circles[i + 1][j] == circles[i][j]:  # i = N
                visit[i + 1][j], flag = True, True
            elif circles[i][(j - 1 + M) % M] == circles[i][j]:  # j = 0
                visit[i][(j - 1 + M) % M], flag = True, True
            elif circles[i][(j + 1) % M] == circles[i][j]:  # j = M
                visit[i][(j + 1) % M], flag = True, True
            else:
                temp = True    # 인접한 것이 없는 경우에는 True

            if not temp: visit[i][j] = True  # 인접한 수가 있었다면 방문 표시
            total += 1

    if not flag:  # 2-2. 인접 하거나 같은 수가 없는 경우에는 원판에 적힌 수의 평균을 구하기
        total_num = sum(sum(circles, []))
        if total_num == 0:
            break
        eval_num = total_num / total  # 남아 있는 수의 개수(평균이 소수일 수도 있네)
        for i in range(N):
            for j in range(M):
                if circles[i][j] == 0: continue
                if circles[i][j] > eval_num:  # 평균 보다 큰 수에서 1을 빼기
                    circles[i][j] -= 1
                elif circles[i][j] < eval_num:
                    circles[i][j] += 1
    else:   # 인접하고 같았던 수들이 있었다면 실제 제거
        for i in range(N):
            for j in range(M):
                if visit[i][j]: circles[i][j] = 0

print(sum(sum(circles, [])))


