def solution(n, build_frame):
    res = []  # 최종 구조물의 상태
    # 한 좌표에 기둥과 보가 모두 설치되어 있는 경우 고려해서 배열을 따로 만들어줘야함
    bo = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    pillar = [[False for _ in range(n + 1)] for _ in range(n + 1)]

    def set_struct(x, y, a):
        if a == 0:
            pillar[x][y] = True
        else:
            bo[x][y] = True

    def remove_struct(x, y, a):
        if a == 0:
            pillar[x][y] = False
        else:
            bo[x][y] = False

    def validate(x, y, a):  # 설치는 그냥 오른쪽 / 위쪽 방향으로 진행(기둥 세울 때도 조건 만족해야함)
        if a == 0:  # 기둥
            if y == 0 or pillar[x][y - 1]: return True
            if (x > 0 and bo[x - 1][y]) or bo[x][y]: return True
        elif a == 1:  # 보
            if pillar[x][y - 1] or pillar[x + 1][y - 1]: return True  # 아래에서 기둥이 어느 쪽에도 받쳐 주지 않는 경우
            if (x > 0 and bo[x - 1][y]) and bo[x + 1][y]: return True  # 무조건 양쪽에 보가 존재해야함
        return False

    for x, y, a, b in build_frame:  # 좌표, 구조물 종, 설치/삭제 여부
        if b == 1:
            if validate(x, y, a):  # 조건을 만족하면 구조물 설치
                set_struct(x, y, a)
                res.append([x, y, a])
        else:  # 구조물 삭제
            if [x, y, a] not in res:  # 만약 설치를 실패한 구조물을 뒤에서 다시 삭제하려 하는 경우가 있는 경우
                continue

            remove_struct(x, y, a)  # 삭제 후 설치되어 있는 모든 구조물들이 조건을 만족하는지 다시 체크(or 이웃 구조물들만 체크)
            for tx, ty, ta in res:
                if tx == x and ty == y and ta == a: continue  # 삭제하려는 구조물 자신
                if not validate(tx, ty, ta):  # 하나라도 조건을 만족하지 못하는 경우 복구
                    set_struct(x, y, a)
                    break
            else:
                res.remove([x, y, a])  # 조건을 만족 = 삭제
    return sorted(res)