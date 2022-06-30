# N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값 구하기
def solution(N, number):
    answer = -1      # N > 8 => -1 출력
    dp = [set() for _ in range(9)]   # dp 배열 집합으로 초기화

    for i in range(1, 9):             # N의 총 범위만큼 탐색
        dp[i].add(int(str(N) * i))   # 연속된 숫자 먼저 추가

        for j in range(1, i):
            for x in dp[j]:          # 수 j 번 사용했을때 결과의 집합
                for y in dp[i-j]:    # 수 i-j 번 사용했을떄 결과의 집합
                    dp[i].add(x + y)
                    dp[i].add(x * y)
                    dp[i].add(x - y)

                    if y != 0:
                        dp[i].add(x // y)
        if number in dp[i]:    # 구하고자 하는 수 number가 존재하면 결과 저장
            answer = i
            break
    return answer


n, number = map(int, input().split(' '))
print(solution(n, number))


