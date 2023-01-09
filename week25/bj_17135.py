# 궁수에 위치에 따른 공격으로 제거할 수 있는 적의 최대 수 구하기

from itertools import combinations

def enemy_attack(row, archer, copy):
    info = [list() for _ in range(M)]
    dead_lis = set()
    cnt = 0

    for col_a in archer:  # 세 명 궁수의 위치 (열), 하나의 적에 대해서 세 명 중 가장 거리가 짧은 궁수가 픽
        for i in range(row-1, -1, -1):  # 궁수의 위치 하나 위부터 탐색
            for j in range(M):
                if copy[i][j] == 0:  # 적이 없는 빈 칸 이라면 패스, 같은 적을 한번 더 공격할 수 있음
                    continue

                d = abs(row - i) + abs(col_a - j)  # 공격 범위 계산
                if d <= D:        # 공격 범위 이내인 모든 적을 배열에 넣기
                    info[col_a].append([i, j, d])

        if len(info[col_a]) > 0:     # 공격할 대상이 있다면
            info[col_a].sort(key=lambda x: (x[2], x[1]))   # 1. 거리가 가장 짧은 순 2. 가장 왼쪽에 있는 순으로 적을 배열
            x, y, d = info[col_a][0]   # 가장 왼쪽에 해당하는 적을 가져와서 제거
            if copy[x][y] == 1:     # 이미 죽였던 적이 아닌 경우
                copy[x][y] = -1     # 여러 공격수가 같은 적을 공격할 수 있는 조건 도입
                cnt += 1            # 죽인 적의 개수 증가
                dead_lis.add((x, y))

    for x, y in dead_lis:    # 다른 턴으로 넘어가기 전에 아예 죽은것 으로 처리
        copy[x][y] = 0

    return cnt

def is_all_dead(row, copy):   # 현재 궁수가 위치해 있는 행 위의 배열만 탐색
    for i in range(row):
        for j in range(M):
            if copy[i][j] == 1:
                return False
    return True

def play(archer, copy):
    attack, row = 0, N   # row : 궁수가 위치해 있는 행
    while True:
        if is_all_dead(row, copy):   # 적이 격자판에 존재하지 않을때까지 반복, 공격한 적의 개수 반환
            return attack

        attack += enemy_attack(row, archer, copy)
        row -= 1   # 적의 위치 한 칸 아래로 이동 = 공격수의 행을 위로 한칸 이동

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]  # 격자
archers = [i for i in range(M)]  # 열의 개수 만큼 궁수 위치 지정
ans = 0

# 궁수 3명의 위치 완전 탐색(모든 경우의 수에 대해 시행)
for archer_pos in list(combinations(archers, 3)):  # 궁수 세명 위치의 모든 조합을 담은 배열(열)
    ans = max(ans, play(archer_pos, [a[:] for a in arr]))  # 원본의 복사본 전달

print(ans)






