# 두 팀의 능력치 차이의 최소값 구하기
# 8 => 1/7, 2/6, 3/5, 4/4 (각각 8Cn) =>  조합(C) 처럼 뽑으면 더 복잡해짐
# 비트마스킹으로 1011001으로 서로 같은 집합에 있음 표시
# 1. 해당 사람이 팀을 선택 2. 해당 사람이 팀을 선택하지 X 재귀(백트래킹) => N개가 되었을 때 최소값 검사

# 1. 백트래킹 풀이
def calculate_power(team):
    global res
    start, link = 0, 0
    for i in range(N):
        for j in range(N):
            if team[i] == 1 and team[j] == 1:
                start += arr[i][j]
            elif team[i] == 0 and team[j] == 0:
                link += arr[i][j]

    res = min(res, abs(start - link))

def back_tracking(i, team):  # cnt 뽑기 X
    global N
    if i == N:
        calculate_power(team)
        return

    team[i] = 1   # i 번째 사람이 팀을 선택
    back_tracking(i + 1, team)
    team[i] = 0   # i 번째 사람이 팀을 선택하지 않는 경우
    back_tracking(i + 1, team)

def solution():
    global N, arr
    team = [0 for _ in range(N)]
    back_tracking(0, team)
    return res

N = int(input())
res = float("inf")
arr = [list(map(int, input().split(" "))) for _ in range(N)]
print(solution())

# 2. 비트마스킹 방법: 모든 경우의 수에 대해 최소값 계산
def calculate(team):
    ans = 0
    for i in range(len(team)):
        for j in range(len(team)):
            ans += arr[team[i]][team[j]]
    return ans

def split_team(team):  # 1110
    start, link = [], []
    for i in range(N):
        if (team & (1 << i)) == 0:   # i 번째 사람이 스타트 팀에 들어가 있느냐
            start.append(i)
        else:     # 0이 아닌 경우 다른 팀
            link.append(i)
    return abs(calculate(start) - calculate(link))

# N = int(input())
# res = float("inf")
# arr = [list(map(int, input().split(" "))) for _ in range(N)]
for i in range(1, 1 << N):  # 0001 ~ 1110(1-15): 한쪽으로 쏠리는 경우(최소 한명 존재 해야함) 패스
    res = min(res, split_team(i))
print(res)


# 3. 처음 시도한 방법
# for team_size in range(N//2):   # 1/7, 2/6, 3/5, 4/4
#     visit = [False for _ in range(N)]
#     team = [0 for _ in range(N)]
#     teams = list((
#     get_combs(0, 0, team_size, team, visit, teams)  # 만들어질 수 있는 모든 팀 조합 구하기

# def get_combs(start, depth, team, visit):  # 조합
#     global N, arr
#     if depth == cnt:
#         calculate_power(team)
#         return
#
#     for i in range(start, N):
#         if not visit[i]:
#             visit[i] = True
#             team[i] = 1
#             get_combs(i + 1, depth + 1, team, visit)
#             team[i] = 0
#             visit[i] = False
