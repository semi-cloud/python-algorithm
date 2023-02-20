# 재귀 함수에서 시간 절약하는 방법은 메모지에이션(DP), 같은 수를 여러번 계산 하는 것을 방지
# dp[a][b][c] = 인자가 a, b, c 일 때의 함수 결과값 저장(w(a,b,c))

def w(a, b, c):
    # 위에서 두 조건문이 바텀업 방식 에서의 초기화 코드(dp 범위 정하기)
    if a <= 0 or b <= 0 or c <= 0:   # 음수는 모두 1 리턴
        return 1         # dp[a][b][c] = 1 : 여기서 바로 리턴 안 시키면 맨 아래의 줄을 실행시키므로 바로 리턴
    if a > 20 or b > 20 or c > 20:   # 20 이상 수는 모두 같은 값 리턴
        return w(20, 20, 20)

    if dp[a][b][c]:     # 음수 부분과 20이 넘는 수에서 인덱스 에러가 나므로 이 부분이 맨 처음으로 가면 안됌
        return dp[a][b][c]
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

# dp 배열이 매 테스트 케이스 마다 새로 생성되면 안되는게 테스트 케이스 내부 에서도 같은 값에 대한 계산이 나올 것이기 때문에 최적화가 불가능 해짐
# 20보다 크면 같은 값을 리턴 시키기 때문에 50까지가 아닌 20 전 까지만 초기화 해 놓으면 됌
dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
while True:
    x, y, z = map(int, input().split())  # 50
    if x == -1 and y == -1 and z == -1:
        break
    print("w(%d, %d, %d) = %d" % (x, y, z, w(x, y, z)))
