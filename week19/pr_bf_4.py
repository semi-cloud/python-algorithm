# 전체 카펫의 크기 구하기

def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        if yellow % i == 0:   # 약수 찾기
            x = yellow // i
            y = i

            if (x * 2) + (y * 2) + 4 == brown:  # (노란색 가로 길이 * 2) + (노란색 세로 길이 * 2) + 4 = 브라운 전체 개수
                answer.append(x + 2)   # 가로
                answer.append(y + 2)   # 세로
                break
    return answer

print(solution(24, 24))


