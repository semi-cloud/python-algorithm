# 주어진 추만을 사용하여 구슬의 무게를 확인 할 수 있는지를 결정
# 중복 문제를 만들어내는 경우의 수를 찾고 메모지에이션 기법 사용
# 0 : 왼쪽에 올린다, 1: 오른쪽에 올린다, 2: 올리지 않는다 세 가지 경우가 존재 -> top-down
# dp[i][j] => i 번째 무게까지의 추를 사용했을 때 j 번째 무게를 만들 수 있는지 여부(j번째 무게를 보고 i번째 추를 가져다가 검사하는게 X, 역방향)

def top_down(idx, weight):   # 세 가지 경우에 대해 그냥 재귀 돌리면 3^30 -> 시간 초과 -> 메모지에이션 필요
    if idx > N or dp[idx][weight]: return   # 이미 i 번째 추를 사용했을 때 해당 무게를 만들 수 있는지 계산된 결과
    dp[idx][weight] = True   # idx 번째 까지의 추를 사용했을 때 weight 만큼의 무게를 만들 수 있음

    top_down(idx + 1, weight + chu[idx])    # 왼쪽에 올리는 경우(같은 방향)
    top_down(idx + 1, weight)      # 올리지 않는 경우
    top_down(idx + 1, abs(weight - chu[idx]))  # 오른쪽에 올리는 경우 왼쪽 무게랑 뺀 값이 가능한 구슬 무게 (다른 방향)

N = int(input())
chu = list(map(int, input().split())) + [0]  # 추 정보(맨 끝에 하나 확장은 인덱스 에러 방지)
M = int(input())
marbles = list(map(int, input().split()))  # 구슬 정보 (최대 무게 : 40000)
max_marble = max(marbles)

dp = [[False for _ in range(40001)] for _ in range(31)]
top_down(0, 0)
for j in range(M):   # 확인 해볼 구슬 무게
    for i in range(N+1):  # 추 인덱스
        if dp[i][marbles[j]]:
            print("Y", end="")
            break
    else:
        print("N", end="")
    print(" ", end="")

