# 야구 경기에서 타순을 결정함에 따라 얻을 수 있는 최대 점수를 출력
# 3 아웃 으로 인해 1이닝이 끝나고 2이닝이 시작될 때는 마지막 타자의 다음 사람 부터 다시 시작(타순은 변경 불가능)
# arr = [0 for _ in range(3)] 과 같은 각 위치에 타수가 존재하는지 체크하는 배열로 하면 시간 초과(변수 세 개 필요)
# 한 루에 여러 타수가 올라올 수는 X

from itertools import permutations

def play(order):  # 타순 => 1번 타자의 결과값은 result[i]
    i, ans = 0, 0
    for inning in result:  # 각 이닝 진행
        out = 0
        one, two, three = False, False, False
        while out < 3:     # 아웃이 3개가 되면 1이닝 종료
            if inning[order[i]-1] == 0:
                out += 1

            elif inning[order[i]-1] == 4:      # 홈런인 경우 배열에 있던 모든 주자들이 홈으로 들어옴
                if three: ans += 1
                if two: ans += 1
                if one: ans += 1
                ans += 1
                one, two, three = False, False, False

            elif inning[order[i]-1] == 1:
                if three: ans += 1
                one, two, three = True, one, two

            elif inning[order[i]-1] == 2:
                if three: ans += 1
                if two: ans += 1
                one, two, three = False, True, one

            elif inning[order[i]-1] == 3:
                if three: ans += 1
                if two: ans += 1
                if one: ans += 1
                one, two, three = False, False, True
            i += 1
            i %= 9
    return ans

path = []
visit = [False for _ in range(10)]
def dfs(depth):  # 타순 결정을 순열로 구현
    global res
    if len(path) >= 4 and path[3] != 1:  # 1번 타자는 무조건 4번 자리에 있어야 함
        return

    if depth == 10:
        res = max(res, play(path))      # 각 경기가 끝난 후 점수 최대값 갱신
        return

    for i in range(10):
        if not visit[i]:
            visit[i] = True
            path.append(i)
            dfs(depth + 1)
            path.pop()
            visit[i] = False  # 순열을 구할 때는 방문 체크를 다시 풀어주는 것이 무조건 필요

N = int(input())   # 이닝 수
result = [list(map(int, input().split())) for _ in range(N)]  # 9명의 선수가 각 이닝에서 얻을 수 있는 결과
res = 0

temp = [i+1 for i in range(9)]
for order in list(permutations(temp, 9)):
    if order[3] == 1:   # 4번째 자리는 1번 타자
        res = max(res, play(order))

print(res)
